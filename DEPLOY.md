# DEPLOY.md — Cafeto 21 (Tacoma WA) — card t_27e55913

Co-hosted demo, built 2026-11-25. Facts-only from TNT Diner column (2026-06-18) + local.yahoo (GBP-fed) + explorewashingtonstate + visitpiercecounty; ledger in build_pages.py header.

## Topology (live state, verified 2026-11-25)
- Railway project: **the-plain-bar** (id 604a72a9…, shell co-host — account project cap hit 11-23; this site is a SERVICE inside it, teardown = `railway service delete -s <id> -y --json`, NEVER project delete — capitol-locksmith-demo + the-stamina-bar siblings must survive)
- Service: cafeto-21-demo (id b19081c2…) · Deployment latest verified live 2026-11-25 (style.css md5 parity 9/9)
- Domain: https://cafeto-21-demo.up.railway.app (renamed to -demo; canonical/og/sitemap/robots pinned to it; noindex forever on demo)
- GitHub: github.com/gnaritas/cafeto-21 (public, no secrets)
- Form relay: server.js → Brevo HTTP API v3 (htmlContent), BREVO_API_KEY set from xkeysib onward (~/.hermes/secrets/brevo_smtp_key.txt line 2) — MAILSENT proven in service logs. Pixel: GET /open?t=<token> (43B gif). CLICK logged when query has utm_.
- Registry: lane.db deploys+services rows written via sites_agency_state.py set + export/verify IDENTICAL.

## Redeploy recipe
`cd sites/cafeto-21 && python3 build_pages.py && python3 /Users/rleon/sites/_verify.py public https://cafeto-21-demo.up.railway.app && railway up -d -y -s cafeto-21-demo` (service already exists; plain `railway up` in this multi-service project needs -s).

## Sweep lineage (this dir)
sweep.py (CDP at :9333, 1280/390 full-page, cache-disabled, DOM bleed/overflow gates) → run_battery.py (OpenRouter vision pass) → probe_claims.py + fixcheck.py (live-DOM adjudication of every vision claim; ZoneInfo-free, pure measurement) → renders/ evidence. Two real defects fixed 2026-11-25: header CTA pill color cascade (scoped nav a.btn white rule) and short-page footer float (body flex column + main flex:1). Both verified live by computed-style probe + pixel scan.

## Pitch state
Send staged (not yet sent): _pitch_cafeto-21.md/.envelope.json/.send.py at projects/websites root. v7 arm (coin sha256 mod 2 = 1), founder bundle canonical link 14A14ockBahRdfIcb93ks09, token cafeto-21-t1, followup_due 2026-12-07, pilot mature_on 2026-12-14, age tag older (press proxy 2026-06-01). Parked SCHEDULED_UNTIL 2026-11-30T07:30:00-08:00 PT.
