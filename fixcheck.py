#!/usr/bin/env python3
"""Post-fix adjudication probe for CAFETO 21 (t_27e55913).
a) header CTA pill color at both viewports (must be white on berry post-fix)
b) coffee-matcha lab->panel gap + scoop-dot right inset (::before)
c) our-story main-children junction gaps (0px prose-wall trap)"""
import asyncio, json, time, urllib.request
import websockets

O = "https://cafeto-21-demo.up.railway.app"

PROBE = """(() => {
  var out = {};
  function rect(e){ if(!e) return null; var r=e.getBoundingClientRect(); return {x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)}; }
  out.vw = document.documentElement.clientWidth;
  var hb = document.querySelector('header.site nav a.btn');
  if (hb) { var cs = getComputedStyle(hb);
    out.headerBtn = {label: hb.textContent.trim(), color: cs.color, bg: cs.backgroundColor, box: rect(hb)}; }
  var lab = document.querySelector('.lab');
  var plate = document.querySelector('.plate');
  if (lab && plate) {
    var lr = rect(lab), pr = rect(plate);
    out.labGap = pr.y - (lr.y + lr.h);
    out.lab = lr; out.plate = pr;
    var pb = getComputedStyle(plate, '::before');
    var prr = rect(plate.querySelector('h3') || plate);
    out.dotStyle = {content: pb.content, width: pb.width, height: pb.height, right: pb.right, top: pb.top, position: pb.position, bg: pb.backgroundColor};
    out.platePadRight = getComputedStyle(plate).paddingRight;
  }
  var main = document.querySelector('main');
  if (main) {
    out.junctions = [];
    var kids = main.children; var prev = null;
    for (var i = 0; i < kids.length; i++) {
      var r = rect(kids[i]);
      if (!r) continue;
      var cs = getComputedStyle(kids[i]);
      if (cs.display === 'none') continue;
      if (prev) out.junctions.push({cls: (kids[i].tagName + '.' + (kids[i].className || '')).slice(0, 26), gap: r.y - prev.bot});
      prev = {bot: r.y + r.h, cls: kids[i].tagName};
    }
  }
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
        try:
            await send("Network.enable"); await send("Network.setCacheDisabled", {"cacheDisabled": True})
        except Exception:
            pass
        for (pg, w, h, mob) in [("visit", 1280, 900, False), ("visit", 390, 844, True),
                                ("coffee-matcha", 1280, 900, False), ("our-story", 1280, 900, False),
                                ("our-story", 390, 844, True)]:
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
            await asyncio.sleep(1.0)
            ev = await send("Runtime.evaluate", {"expression": PROBE, "returnByValue": True})
            d = json.loads(ev["result"]["value"])
            print("=== %s @%s" % (pg, w))
            if "headerBtn" in d:
                print(" headerBtn:", json.dumps(d["headerBtn"]))
            if "labGap" in d:
                print(" lab->panel gap:", d["labGap"], "lab:", d["lab"], "plate:", d["plate"], "padRight:", d.get("platePadRight"))
                print(" dot ::before:", json.dumps(d.get("dotStyle")))
            for j in d.get("junctions", []):
                print(" JUNCTION %-28s gap=%s" % (j["cls"], j["gap"]))
        try:
            await send("Target.closeTarget", {"targetId": tid})
        except Exception:
            pass
    print("FIXCHECK_DONE")

asyncio.run(main())
