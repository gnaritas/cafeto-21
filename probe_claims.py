#!/usr/bin/env python3
"""Adjudication probes for CAFETO 21 sweep claims (t_27e55913).
Measures live-DOM rects/gaps/computed styles the vision battery flagged.
Local headless Chrome CDP :9333; sets its own viewport per pass."""
import asyncio, json, os, time, urllib.request
import websockets

O = "https://cafeto-21-demo.up.railway.app"

PROBE = """(() => {
  var out = {};
  function q(sel){ return document.querySelector(sel); }
  function rect(e){ if(!e) return null; var r=e.getBoundingClientRect(); return {x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)}; }
  function textRect(e){ if(!e||!e.firstChild) return null; var rn=document.createRange(); rn.selectNodeContents(e); var r=rn.getBoundingClientRect(); return {x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)}; }
  // header CTA buttons
  out.btns = [];
  var bs = document.querySelectorAll('header .btn, .hero-cta .btn, a.btn');
  for (var i=0;i<bs.length;i++){
    var b=bs[i]; var cs=getComputedStyle(b);
    out.btns.push({label:b.textContent.trim().slice(0,24), btn:rect(b), text:textRect(b),
      color:cs.color, bg:cs.backgroundColor, wrap:cs.whiteSpace, td:cs.textDecorationLine,
      innerScroll: b.scrollWidth + '/' + b.clientWidth});
  }
  // nav links adjacency (desktop)
  out.nav = [];
  var ns = document.querySelectorAll('header.site nav a');
  for (var i=0;i<ns.length;i++){ var r=rect(ns[i]); r.label=ns[i].textContent.trim().slice(0,18); out.nav.push(r); }
  // footer link styles
  out.flinks = [];
  var fs = document.querySelectorAll('footer a');
  for (var i=0;i<fs.length;i++){ var cs=getComputedStyle(fs[i]);
    out.flinks.push({t:fs[i].textContent.trim().slice(0,26), td:cs.textDecorationLine, color:cs.color}); }
  // panels + labels + decorative dots rhythm (generic)
  out.panels = [];
  var ps = document.querySelectorAll('main section, main .panels > *, .plate');
  for (var i=0;i<Math.min(ps.length,14);i++){
    var p=ps[i]; var cs=getComputedStyle(p);
    var prev = p.previousElementSibling;
    var gap = prev ? Math.round(rect(p).y - (rect(prev).y + rect(prev).h)) : null;
    out.panels.push({cls:(p.className||'').slice(0,24), box:rect(p), gapPrev:gap, ovf: p.scrollWidth+'/'+p.clientWidth });
  }
  out.vw = document.documentElement.clientWidth;
  out.hs = document.documentElement.scrollHeight;
  return JSON.stringify(out);
})()"""

async def main():
    with urllib.request.urlopen("http://127.0.0.1:9333/json/version", timeout=10) as r:
        ver = json.load(r)
    async with websockets.connect(ver["webSocketDebuggerUrl"], max_size=60 * 1024 * 1024) as ws:
        mid = [0]; events = {}; sess = [None]
        async def send(method, params=None):
            mid[0] += 1
            payload = {"id": mid[0], "method": method, "params": params or {}}
            if sess[0] and not method.startswith("Target."):
                payload["sessionId"] = sess[0]
            await ws.send(json.dumps(payload))
            while True:
                msg = json.loads(await ws.recv())
                if msg.get("method") == "Page.loadEventFired":
                    events["load"] = True
                if msg.get("id") == mid[0]:
                    if "error" in msg:
                        raise RuntimeError(method + ": " + json.dumps(msg["error"])[:200])
                    return msg.get("result", {})
        tid = (await send("Target.createTarget", {"url": "about:blank"}))["targetId"]
        sess[0] = (await send("Target.attachToTarget", {"targetId": tid, "flatten": True}))["sessionId"]
        await send("Page.enable"); await send("Runtime.enable")
        passes = [("visit", 1280, 900, False), ("visit", 390, 844, True),
                  ("privacy", 390, 844, True), ("contact", 390, 844, True),
                  ("coffee-matcha", 1280, 900, False), ("crepes", 1280, 900, False)]
        for (pg, w, h, mob) in passes:
            await send("Emulation.setDeviceMetricsOverride",
                       {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": mob})
            events.pop("load", None)
            await send("Page.navigate", {"url": O + ("/" if pg == "index" else "/" + pg)})
            t0 = time.time()
            while not events.get("load") and time.time() - t0 < 30:
                try:
                    msg = json.loads(await asyncio.wait_for(ws.recv(), timeout=2))
                    if msg.get("method") == "Page.loadEventFired":
                        events["load"] = True
                except asyncio.TimeoutError:
                    pass
            await asyncio.sleep(1.2)
            ev = await send("Runtime.evaluate", {"expression": PROBE, "returnByValue": True})
            data = json.loads(ev["result"]["value"])
            print("=== %s @%s vw=%s hs=%s" % (pg, w, data["vw"], data["hs"]))
            for b in data["btns"]:
                inside = b["text"] and b["btn"] and b["text"]["x"] >= b["btn"]["x"] and b["text"]["x"] + b["text"]["w"] <= b["btn"]["x"] + b["btn"]["w"] + 1
                fits = b["text"] and b["text"]["w"] <= b["btn"]["w"]
                offscreen = b["btn"] and (b["btn"]["x"] + b["btn"]["w"] > data["vw"] + 2)
                print(" BTN %-24s btn=%s text=%s inside=%s fits=%s offscreen=%s scroll=%s color=%s bg=%s" % (
                    b["label"], b["btn"], b["text"], inside, fits, offscreen, b["innerScroll"], b["color"], b["bg"]))
            if pg == "visit" and w == 1280:
                prev = None
                for n in data["nav"]:
                    gap = (n["x"] - (prev["x"] + prev["w"])) if prev else None
                    print(" NAV %-18s x=%s w=%s gapPrev=%s cy=%s" % (n["label"], n["x"], n["w"], gap, n["y"] + n["h"] // 2))
                    prev = n
            if pg == "visit":
                print(" FLINKS:", json.dumps(data["flinks"]))
            if pg == "coffee-matcha":
                for p in data["panels"]:
                    print(" PANEL %-24s box=%s gapPrev=%s ovf=%s" % (p["cls"], p["box"], p["gapPrev"], p["ovf"]))
        try:
            await send("Target.closeTarget", {"targetId": tid})
        except Exception:
            pass
    print("PROBE_DONE")

asyncio.run(main())
