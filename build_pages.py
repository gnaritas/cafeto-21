#!/usr/bin/env python3
"""CAFETO 21 — creperie & coffee bar, Downtown Tacoma WA — generator (single source).
websites lane, card t_27e55913. Built 2026-11-25. Demo host pinned from first byte.
Design: crepe-counter palette — espresso-ink bands, crepe-paper cream body, caramel/berry/
matcha accents; folded-crepe hero art (flat vector, no photos), 'plate' panels with a
colored scoop-dot badge per panel, circled 21 disc in the wordmark. No third-party JS,
no webfonts. Demo hosts keep noindex forever.

FACTS ONLY from press/listing-verified sources (card t_27e55913 + dispatch re-verify 11-25,
claim-by-claim truth-check via cache/scratch/claims_cafeto21.py + full TNT text re-read 11-25):
- TNT 'Diner' column (thenewstribune.com article316170445; AOL syndication datePublished
  2026-06-18 'June 18, 2026' — opened at the beginning of that month): address 1127 Broadway
  Suite 101; next to Tacoma Dance Studios + Tacoma School of the Arts theater; replaced Eather
  Tea (closed end of 2025), moved in ~3 months before opening; coffee/matcha/horchata/
  smoothies/energy drinks most smalls $3-4 larges to $6.50; crepes sweet+savory $12.49-$13.49;
  Berries Delight = strawberries/blueberries/raspberries/blackberries/Nutella + whipped cream +
  powdered sugar (photo caption); Pesto crepe = pesto/mozzarella/mixed greens; make-your-own
  crepe fillings fruit/cream cheese/Nutella/ice cream, toppings marshmallows/Oreos/marzipan;
  other bites $12-$14: avocado toast w/ eggs, sandwiches turkey&ham/prosciutto/roast beef,
  customizable sweet waffles; strawberry matcha in shop's own press photo; owner Esteban Regla
  (TNT: pronounced 'caf-ay-to'), cousin Juan Pablo (coffee shop in Mexico, crepe street cart
  before) — moved to WA five years ago; first shop Redondo Coffee & Crepes, Renton; menu
  mirrors Redondo. TNT printed 8am-5pm at opening.
- local.yahoo info-241564015 (GBP-fed; 'Closed now' live-check 18:42 PT 11-25 consistent
  with 4pm close): hours 8:00 AM - 4:00 PM every day; phone (206) 537-9643; cross-streets
  between S 11th St and S 13th St; aggregateRating 5.0/5; GBP-published description (specialty
  espresso, signature lattes, crepes, waffles, BAGUETTES); owner photo alt 'Fall pumpkin white
  chocolate hazelnut latte'. GBP maps embed blob confirms phone + only external link =
  instagram.com/cafeto21.wa (no website field).
- explorewashingtonstate.com (2026-09 photo, current scan): 'creperie first, espresso bar
  attached', 'theater end of downtown', hours 8am-4pm 7 days, Nutella Dream + Dubai Dream
  sweet crepes, prosciutto crepe.
- visitpiercecounty.com listing 3980: Horchata Latte signature, free Wi-Fi, hub for students/
  remote workers, customizable waffles/avocado toasts/breakfast sandwiches.
- CURRENT HOURS = 8 a.m.-4 p.m. daily (yahoo live-status corroborated + EWS; TNT 5pm = June
  opening info, two newer sources agree on 4pm). DoorDash store URL canonical shape verified
  via search 11-25: /store/cafeto-21-tacoma-46017039/. Coordinates: OpenStreetMap Nominatim
  house match 1127 Broadway (47.2522564,-122.4395138, ODbL). Unverified (parking, exact menu
  prices per item, reservations) = omitted, never guessed.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
ORIGIN = "https://cafeto-21-demo.up.railway.app"

BRAND = "Cafeto 21"
BRAND_PLAIN = "Cafeto 21"
ADDR = "1127 Broadway, Suite 101, Tacoma, WA 98402"
GEO = (47.2522564, -122.4395138)  # OSM Nominatim house match, 1127 Broadway (ODbL)
MAP_Q = "https://www.google.com/maps?q=1127%20Broadway%2C%20Suite%20101%2C%20Tacoma%2C%20WA%2098402&output=embed"
DIRS = "https://www.google.com/maps/dir/?api=1&destination=1127%20Broadway%2C%20Suite%20101%2C%20Tacoma%2C%20WA%2098402"
EMAIL = "cafeto.21@hotmail.com"
PHONE_DISPLAY = "(206) 537-9643"
PHONE_TEL = "+12065379643"
DOORDASH = "https://www.doordash.com/store/cafeto-21-tacoma-46017039/"
IG = "https://www.instagram.com/cafeto21.wa/"

def head(title, desc, path, ld=None, og_desc=None):
    u = ORIGIN + path
    d = desc.replace('"', "'")
    parts = ['<!DOCTYPE html>', '<html lang="en">', '<head>', '<meta charset="utf-8">',
             '<meta name="robots" content="noindex, nofollow">',
             '<!-- BUILT-2026-11-25 -->',
             '<title>%s</title>' % title,
             '<meta name="description" content="%s">' % d,
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             '<link rel="canonical" href="%s">' % u,
             '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
             '<link rel="stylesheet" href="/style.css">']
    t = title.replace('"', "'")
    od = (og_desc or desc).replace('"', "'")
    parts += [
        '<meta property="og:type" content="website">',
        '<meta property="og:title" content="%s">' % t,
        '<meta property="og:description" content="%s">' % od,
        '<meta property="og:image" content="%s/og.png">' % ORIGIN,
        '<meta property="og:url" content="%s">' % u,
        '<meta name="twitter:card" content="summary_large_image">']
    for blk in (ld or []):
        parts.append('<script type="application/ld+json">%s</script>' % json.dumps(blk, ensure_ascii=False))
    parts.append('</head>')
    return "\n".join(parts)

NAV_LINKS = [
    ("Crepes & brunch", "/crepes"),
    ("Coffee & matcha", "/coffee-matcha"),
    ("Our story", "/our-story"),
    ("Visit", "/visit"),
]

def nav(active):
    items = []
    for label, href in NAV_LINKS:
        cur = ' aria-current="page"' if href == active else ""
        items.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    items.append('<a class="btn sm" href="/contact">Say hello</a>')
    return ('<body>\n<div class="topline" aria-hidden="true"></div>\n'
            '<a class="skip" href="#main">Skip to content</a>\n'
            '<header class="site">\n'
            '<p class="brand"><a href="/"><span class="wordmark">Cafeto</span> <span class="disc">21</span></a></p>\n'
            '<nav aria-label="Site"><p>%s</p></nav>\n'
            '</header>\n<main id="main">' % " ".join(items))

FOOTER = ('</main>\n<footer>\n'
          '<p class="footline">%s &middot; Creperia &amp; coffee bar &middot; Downtown Tacoma</p>\n'
          '<p class="footline">Open 8 a.m.&ndash;4 p.m. every day &middot; %s &middot; <a href="tel:%s">%s</a> &middot; <a href="mailto:%s">%s</a></p>\n'
          '<p class="footline fine">&copy; 2026 &middot; <a href="/crepes">Crepes</a> &middot; <a href="/coffee-matcha">Drinks</a> &middot; <a href="/our-story">Story</a> &middot; <a href="/visit">Visit</a> &middot; <a href="/contact">Contact</a> &middot; <a href="/privacy">Privacy</a></p>\n'
          '</footer>\n</body>\n</html>\n') % (BRAND_PLAIN, ADDR, PHONE_TEL, PHONE_DISPLAY, EMAIL, EMAIL)

def cafe_node(path="/"):
    return {
        "@context": "https://schema.org",
        "@type": "CafeRestaurant",
        "name": BRAND,
        "url": ORIGIN + path,
        "image": ORIGIN + "/og.png",
        "telephone": "+1-206-537-9643",
        "email": EMAIL,
        "priceRange": "$12–$14",
        "servesCuisine": ["Crepes", "Brunch", "Coffee"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "1127 Broadway, Suite 101",
            "addressLocality": "Tacoma",
            "addressRegion": "WA",
            "postalCode": "98402",
            "addressCountry": "US",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
        "hasMap": "https://www.google.com/maps?q=1127%20Broadway%2C%20Suite%20101%2C%20Tacoma%2C%20WA%2098402",
        "openingSpecification": None,  # placeholder removed below
    }

def store_ld():
    n = cafe_node("/")
    n.pop("openingSpecification", None)
    n["openingHoursSpecification"] = [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": day,
        "opens": "08:00",
        "closes": "16:00",
    } for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]]
    return n

def breadcrumb(label, path):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"},
            {"@type": "ListItem", "position": 2, "name": label, "item": ORIGIN + path},
        ],
    }

def service_node(name, stype, desc, path):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": stype,
        "description": desc,
        "url": ORIGIN + path,
        "areaServed": [
            {"@type": "City", "name": "Tacoma", "containedInPlace": {"@type": "State", "name": "Washington"}},
        ],
        "provider": {k: v for k, v in store_ld().items() if k != "@context"},
    }

# Inline SVG crepe-stack art for the hero (aria-hidden, decorative). Flat vector, no runtime.
CREPE_SVG = '''<svg class="crepe-art" viewBox="0 0 360 260" role="img" aria-hidden="true" focusable="false">
  <rect x="8" y="8" width="344" height="244" rx="26" fill="#221a14"/>
  <circle cx="165" cy="130" r="106" fill="#f3ead6"/>
  <ellipse cx="160" cy="166" rx="82" ry="24" fill="#d3a86b" stroke="#8a5a33" stroke-width="3"/>
  <ellipse cx="163" cy="146" rx="78" ry="23" fill="#dfbc84" stroke="#8a5a33" stroke-width="3"/>
  <ellipse cx="158" cy="127" rx="74" ry="22" fill="#e6ca93" stroke="#8a5a33" stroke-width="3"/>
  <path d="M96 112 L158 62 L182 118 q-40 18 -86 -6 z" fill="#f0dcab" stroke="#8a5a33" stroke-width="3"/>
  <path d="M104 108 q28 14 70 -2" fill="none" stroke="#c98b4a" stroke-width="4" stroke-linecap="round"/>
  <path d="M120 78 q26 -14 40 2" fill="none" stroke="#4a2c1a" stroke-width="4" stroke-linecap="round"/>
  <circle cx="238" cy="86" r="11" fill="#a3243f"/>
  <circle cx="262" cy="100" r="11" fill="#71182e"/>
  <circle cx="248" cy="120" r="11" fill="#c2416b"/>
  <circle cx="226" cy="112" r="9" fill="#4a5d8a"/>
  <circle cx="252" cy="142" r="9" fill="#5d4a86"/>
  <path d="M258 66 q10 -14 22 -4 q-8 12 -22 4 z" fill="#6f8f4f"/>
  <circle cx="303" cy="192" r="32" fill="#6f8f4f" stroke="#516b38" stroke-width="4"/>
  <circle cx="303" cy="192" r="21" fill="#93b06d"/>
  <path d="M322 173 L338 157" stroke="#516b38" stroke-width="5" stroke-linecap="round"/>
  <circle cx="118" cy="196" r="2.5" fill="#fbf6ec"/>
  <circle cx="146" cy="204" r="2.5" fill="#fbf6ec"/>
  <circle cx="176" cy="198" r="2.5" fill="#fbf6ec"/>
  <circle cx="204" cy="206" r="2.5" fill="#fbf6ec"/>
</svg>'''

pages = {}

# ---------------- HOME ----------------
home_ld = [store_ld()]
pages["index.html"] = (
    head("Cafeto 21 — Crepes, Coffee & Brunch in Downtown Tacoma, WA",
         "A creperie with a coffee bar attached at 1127 Broadway in downtown Tacoma: sweet and savory crepes made to order, matcha, horchata lattes, waffles and sandwiches — open 8 a.m. to 4 p.m. every day.",
         "/", home_ld)
    + nav("/")
    + '''<section class="hero">
  <div class="hero-copy">
    <p class="lab mono">Creperia &middot; Coffee &middot; Downtown Tacoma</p>
    <h1 class="mark">Cafeto <span class="disc big">21</span></h1>
    <p class="mark-sub mono">Said &#8220;caf-ay-to.&#8221;</p>
    <p class="sub">A creperie with a coffee bar attached, on Broadway between 11th and 13th — sweet and savory crepes made to order, matcha and horchata lattes, waffles, toast and sandwiches. Open every day, 8 a.m. to 4 p.m.</p>
    <p class="hero-cta"><a class="btn" href="/crepes">See the crepes</a> <a class="ghost" href="/visit">Plan a visit &rarr;</a></p>
  </div>
  ''' + CREPE_SVG + '''
</section>
<section class="panels">
  <article class="plate dot-berry">
    <p class="lab mono">The crepes</p>
    <h2>Sweet and savory,<br>made to order</h2>
    <p>The Berries Delight piles strawberries, blueberries, raspberries, blackberries and Nutella into a fresh crepe. The Pesto goes savory with mozzarella and mixed greens. Crepes run $12.49 to $13.49.</p>
    <p><a href="/crepes">The whole crepe counter &rarr;</a></p>
  </article>
  <article class="plate dot-caramel">
    <p class="lab mono">The coffee bar</p>
    <h2>Espresso, matcha,<br>horchata lattes</h2>
    <p>All the basic coffee orders, plus matcha, horchata, smoothies and energy drinks. Most smalls start at $3 or $4; larger sizes go up to $6.50.</p>
    <p><a href="/coffee-matcha">The drinks list &rarr;</a></p>
  </article>
  <article class="plate dot-matcha">
    <p class="lab mono">The counter</p>
    <h2>A Tacoma second,<br>built on a Renton original</h2>
    <p>Cafeto 21 is run by Esteban Regla and his cousin Juan Pablo — the pair behind Redondo Coffee &amp; Crepes in Renton. Juan Pablo sold crepes off a street cart before their first shop.</p>
    <p><a href="/our-story">Read the story &rarr;</a></p>
  </article>
</section>
<section class="band">
  <div class="band-copy">
    <p class="lab mono">Open every day</p>
    <h2>8 a.m. to 4 p.m., seven days a week</h2>
    <p>Morning coffee before work, a crepe between classes at the School of the Arts next door, an afternoon study session on the free Wi-Fi — the doors are open all week on Broadway, next to Tacoma Dance Studios and the Tacoma School of the Arts theater.</p>
    <p><a class="btn" href="/visit">Address, map &amp; directions</a> <a class="ghost" href="tel:+12065379643">Call (206) 537-9643</a></p>
  </div>
  <div class="band-map"><iframe src="''' + MAP_Q + '''" loading="lazy" title="Map: Cafeto 21, 1127 Broadway Suite 101, Tacoma WA" allow="management:coordinate"></iframe><p class="mapcap">1127 Broadway, Suite 101 &middot; between S 11th &amp; S 13th &middot; <a href="''' + DIRS + '''">Get directions &nearr;</a></p></div>
</section>''')

# ---------------- CREPES & BRUNCH (detail 1) ----------------
menu_ld = {
    "@context": "https://schema.org",
    "@type": "Menu",
    "name": "Crepes & brunch at Cafeto 21",
    "inLanguage": "en-US",
    "hasMenuSection": [
        {"@type": "MenuSection", "name": "Sweet crepes",
         "description": "Crepes $12.49 to $13.49 (TNT Diner, June 2026).",
         "hasMenuItem": [
             {"@type": "MenuItem", "name": "Berries Delight",
              "description": "Strawberries, blueberries, raspberries, blackberries and Nutella, finished with whipped cream and powdered sugar."},
             {"@type": "MenuItem", "name": "Nutella Dream", "description": "Nutella, the sweet-end staple."},
             {"@type": "MenuItem", "name": "Dubai Dream", "description": "The Dubai-chocolate-style crepe on the sweet end."},
             {"@type": "MenuItem", "name": "Make-Your-Own",
              "description": "Pick fillings — fruit, cream cheese, Nutella, ice cream — and toppings: marshmallows, Oreos, marzipan."},
         ]},
        {"@type": "MenuSection", "name": "Savory crepes",
         "hasMenuItem": [
             {"@type": "MenuItem", "name": "Pesto",
              "description": "Pesto, mozzarella and mixed greens."},
             {"@type": "MenuItem", "name": "Prosciutto", "description": "The savory-end standout."},
         ]},
        {"@type": "MenuSection", "name": "Waffles, toast & sandwiches ($12–$14)",
         "hasMenuItem": [
             {"@type": "MenuItem", "name": "Customizable sweet waffles"},
             {"@type": "MenuItem", "name": "Avocado toast with eggs"},
             {"@type": "MenuItem", "name": "Sandwiches", "description": "Turkey and ham, prosciutto or roast beef."},
             {"@type": "MenuItem", "name": "Baguettes"},
         ]},
    ],
}
pages["crepes.html"] = (
    head("Sweet & Savory Crepes, Waffles & Brunch — Cafeto 21, Tacoma WA",
         "Sweet and savory crepes made to order at Cafeto 21 in downtown Tacoma: the Berries Delight, the Pesto, make-your-own crepes, plus customizable waffles, avocado toast and sandwiches — $12.49 to $13.49.",
         "/crepes",
         [breadcrumb("Crepes & brunch", "/crepes"),
          service_node("Sweet & savory made-to-order crepes", "Crepes and brunch",
                       "Made-to-order sweet and savory crepes, customizable sweet waffles, avocado toast, sandwiches and baguettes, served daily 8 a.m. to 4 p.m. at 1127 Broadway, Suite 101, Tacoma WA 98402.",
                       "/crepes"),
          menu_ld])
    + nav("/crepes")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Crepes &amp; brunch</p>
  <p class="lab mono">The crepe counter</p>
  <h1>Folded to order: sweet, savory, or both</h1>
  <p class="lede">Crepes are the reason people cross town for Cafeto 21. Every one is made when you order it, and every one comes in at $12.49 or $13.49.</p>
  <h2>Sweet crepes</h2>
  <ul class="spread">
    <li><span>Berries Delight</span>Strawberries, blueberries, raspberries, blackberries and Nutella, finished with whipped cream and powdered sugar</li>
    <li><span>Nutella Dream</span>The sweet-end staple, done right</li>
    <li><span>The Dubai Dream</span>The Dubai-chocolate-style crepe — the sweet end&rsquo;s other headliner</li>
    <li><span>Make-your-own</span>Pick your fillings — fruit, cream cheese, Nutella, ice cream — and your toppings: marshmallows, Oreos, marzipan</li>
  </ul>
  <h2>Savory crepes</h2>
  <ul class="spread">
    <li><span>The Pesto</span>Pesto, mozzarella and mixed greens, folded shut</li>
    <li><span>The Prosciutto</span>The savory-end standout</li>
  </ul>
  <h2>More from the flat-top</h2>
  <ul class="spread">
    <li><span>Sweet waffles</span>Fully customizable — build yours the way you like them</li>
    <li><span>Avocado toast</span>With eggs, the brunch-side plate</li>
    <li><span>Sandwiches</span>Turkey and ham, prosciutto or roast beef</li>
    <li><span>Baguettes</span>Straight from the case</li>
  </ul>
  <p class="price-note">Crepes $12.49–$13.49. Other plates run $12–$14. Prices as reported by the TNT Diner column in June 2026 — the counter posts current prices in the shop.</p>
  <div class="plate dot-berry wide">
    <p class="lab mono">Order ahead</p>
    <h2>Delivery and pickup on DoorDash</h2>
    <p>The full counter — crepes, waffles, toast and sandwiches — is on DoorDash for delivery and pickup in Tacoma.</p>
    <p><a class="btn" href="''' + DOORDASH + '''" rel="nofollow noopener">Order Cafeto 21 on DoorDash &nearr;</a></p>
  </div>
  <p class="cta-row"><a class="btn" href="/visit">Hours &amp; directions</a> <a href="/coffee-matcha">Coffee, matcha &amp; horchata &rarr;</a></p>
</article>''')

# ---------------- COFFEE & MATCHA (detail 2) ----------------
pages["coffee-matcha.html"] = (
    head("Coffee, Matcha & Horchata Lattes — Cafeto 21, Tacoma WA",
         "The coffee bar at Cafeto 21 in downtown Tacoma: every basic coffee order, matcha, horchata and the signature Horchata Latte, smoothies and energy drinks — smalls from $3–$4, larges to $6.50.",
         "/coffee-matcha",
         [breadcrumb("Coffee & matcha", "/coffee-matcha"),
          service_node("Coffee, matcha and specialty drinks", "Espresso bar and specialty drinks",
                       "Espresso drinks, matcha, horchata, signature lattes, smoothies and energy drinks served daily 8 a.m. to 4 p.m. at Cafeto 21, 1127 Broadway Suite 101, Tacoma WA 98402.",
                       "/coffee-matcha")])
    + nav("/coffee-matcha")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Coffee &amp; matcha</p>
  <p class="lab mono">The coffee bar</p>
  <h1>Matcha, horchata and every coffee you actually order</h1>
  <p class="lede">The espresso bar is the other half of the shop: every basic coffee order done properly, plus the things people drive over for — matcha, horchata and the house Horchata Latte.</p>
  <ul class="spread">
    <li><span>Coffee, all the basics</span>Every basic coffee variety, done properly</li>
    <li><span>Matcha</span>Whisked to order — the strawberry matcha is the one the shop photographs for itself</li>
    <li><span>Horchata &amp; the Horchata Latte</span>The signature the reviews keep naming</li>
    <li><span>Signature lattes</span>House specials — last fall it was the pumpkin white chocolate hazelnut latte</li>
    <li><span>Smoothies</span>Fruit-forward, made when you order</li>
    <li><span>Energy drinks</span>For the study-session crowd</li>
  </ul>
  <div class="plate dot-caramel wide">
    <p class="lab mono">Prices</p>
    <h2>Smalls $3–$4, larges to $6.50</h2>
    <p>Most small sizes start at $3 or $4; larger sizes go up to $6.50. No upcharge mystery — the board at the counter is the truth, and these are the numbers the TNT Diner column published in June 2026.</p>
  </div>
  <h2>Stay a while</h2>
  <p>Wi-Fi is free, the space is open and bright, and the shop has become a hub for students, remote workers and everyone between. Coffee in hand, crepe on the plate, eight hours a day, seven days a week.</p>
  <p class="cta-row"><a class="btn" href="/visit">Hours &amp; directions</a> <a href="/crepes">And the crepes &rarr;</a></p>
</article>''')

# ---------------- OUR STORY (hub + FAQ + press) ----------------
faq_items = [
    ("When did you open?",
     "In June 2026. The family behind Redondo Coffee &amp; Crepes in Renton moved into the old Eather Tea space on Broadway and opened Cafeto 21 — the menus mirror each other, with the crepe emphasis."),
    ("What are the hours?",
     "8 a.m. to 4 p.m., every day of the week — seven-day hours on Broadway. The details are on the <a href=\"/visit\">visit page</a>."),
    ("Where exactly are you?",
     "1127 Broadway, Suite 101 — between S 11th and S 13th, next to Tacoma Dance Studios and the Tacoma School of the Arts theater."),
    ("Can I work here?",
     "That&rsquo;s what a lot of people do — free Wi-Fi, a spacious, bright interior, and the shop sits right beside the School of the Arts."),
    ("Can I get it delivered?",
     "Yes — the full menu is on <a href=\"" + DOORDASH + "\" rel=\"nofollow noopener\">DoorDash</a> for delivery and pickup in Tacoma."),
    ("Is it caf-AY-to or caf-EE-to?",
     "&#8220;Caf-ay-to,&#8221; the way owner Esteban Regla says it. The name is Spanish; the crepes are French; the home is Tacoma."),
]
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a.replace("&amp;", "&").replace("&#8217;", "'").replace("&#8220;", '"').replace("&#8221;", '"').replace("&#8212;", "-").replace("&rsquo;", "'").replace("<a href=\"" + DOORDASH + "\" rel=\"nofollow noopener\">", "").replace("<a href=\"/visit\">", "").replace("<a href=\"/coffee-matcha\">", "").replace("</a>", "")}}
                         for q, a in faq_items]}
pages["our-story.html"] = (
    head("From a Street Cart in Mexico to Broadway in Tacoma — the Story of Cafeto 21",
         "Owner Esteban Regla and his cousin Juan Pablo — a Mexico coffee-shop owner and street-cart crepe seller — brought their Renton crepe recipe to downtown Tacoma. The story, the answers and the press.",
         "/our-story", [breadcrumb("Our story", "/our-story"), faq_ld, store_ld()])
    + nav("/our-story")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Our story</p>
  <h1>Two families, one crepe counter</h1>
  <p class="lede">Cafeto 21 is the Tacoma chapter of a family recipe that starts with a coffee shop in Mexico and a crepe cart on the street.</p>
  <h2>The counter behind the counter</h2>
  <p>Owner Esteban Regla and his cousin Juan Pablo decided to go into business together after moving to Washington five years ago. Juan Pablo had owned a coffee shop in Mexico and sold crepes from a street cart — the folding hand that built the menu you see today.</p>
  <p>Their first shop was Redondo Coffee &amp; Crepes in Renton — same coffee bar, same crepe press, same make-your-own line. When the pair went looking for a second home, downtown Tacoma fit. They moved into the old Eather Tea space on Broadway — the tea-and-dessert shop next to the theater had closed at the end of 2025 — and opened Cafeto 21 in June 2026, with the crepe emphasis front and center.</p>
  <h2>Why the crepes lead</h2>
  <p>The name reads like a coffee bar, but the menu says otherwise: the sweet-and-savory crepe counter is the reason people cross town, and the espresso bar attached to it is the reason they come back at 8 a.m. on a Tuesday. The shop holds five stars on the review feeds so far. The matcha and the Horchata Latte do their own recruiting.</p>
  <h2>The name, said right</h2>
  <p>&#8220;Caf-ay-to,&#8221; the way Esteban says it — Spanish name, French crepes, Tacoma address.</p>
  <h2>In the news</h2>
  <ul class="press">
    <li><a href="https://www.thenewstribune.com/entertainment/restaurants/tnt-diner/article316170445.html" rel="nofollow noopener">TNT Diner — New cafe with coffee, sweet and savory crepes now open in downtown Tacoma</a></li>
    <li><a href="https://www.aol.com/articles/cafe-coffee-sweet-savory-crepes-120000000.html" rel="nofollow noopener">AOL (syndicated TNT) — the same story, in full</a></li>
    <li><a href="https://explorewashingtonstate.com/coffee-shops/cafeto-21/" rel="nofollow noopener">Explore Washington State — a creperie with an espresso bar attached</a></li>
    <li><a href="https://www.visitpiercecounty.com/listing/cafeto-21/3980/" rel="nofollow noopener">Visit Pierce County — the listing</a></li>
    <li><a href="https://www.facebook.com/p/Redondo-Coffee-Crepes-100083478125210/" rel="nofollow noopener">Redondo Coffee &amp; Crepes, Renton — the family&rsquo;s first shop</a></li>
  </ul>
  <h2>Questions people ask</h2>
  <dl class="faq">
''' + "".join('    <dt>%s</dt>\n    <dd>%s</dd>\n' % (q, a) for q, a in faq_items) + '''  </dl>
  <p class="lab mono">Keep going</p>
  <p class="cta-row"><a class="btn" href="/contact">Say hello</a> <a href="/crepes">Crepes</a> &middot; <a href="/coffee-matcha">Drinks</a> &middot; <a href="/visit">Visit</a></p>
</article>''')

# ---------------- VISIT ----------------
pages["visit.html"] = (
    head("Visit — 1127 Broadway Suite 101, Tacoma WA 98402 — Cafeto 21",
         "Cafeto 21 is open 8 a.m. to 4 p.m. every day at 1127 Broadway, Suite 101, Tacoma WA 98402 — between S 11th and S 13th, next to Tacoma Dance Studios. Free parking nearby, Wi-Fi inside, DoorDash for delivery.",
         "/visit",
         [breadcrumb("Visit", "/visit"),
          service_node("Visit Cafeto 21 in downtown Tacoma", "Cafe and creperie storefront",
                       "Creperie and coffee bar at 1127 Broadway, Suite 101, Tacoma WA 98402 — open 8 a.m. to 4 p.m. every day. Free parking nearby, free Wi-Fi, DoorDash delivery and pickup.",
                       "/visit")])
    + nav("/visit")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Visit</p>
  <h1>Broadway, between 11th and 13th</h1>
  <p class="lede">The storefront sits on the theater end of downtown — next to Tacoma Dance Studios and the Tacoma School of the Arts theater.</p>
  <div class="visit-grid">
    <div class="plate dot-berry">
      <p class="lab mono">Address</p>
      <p class="addr">%s</p>
      <p>Between S 11th St and S 13th St &middot; next to Tacoma Dance Studios &middot; the School of the Arts crowd walks over.</p>
      <p><a href="%s">Get directions &nearr;</a></p>
      <p class="lab mono">Hours</p>
      <p class="addr">Open 8 a.m. &ndash; 4 p.m.<br>Every day of the week</p>
      <p class="lab mono">Phone &amp; email</p>
      <p class="addr"><a href="tel:%s">%s</a><br><a href="mailto:%s">%s</a></p>
    </div>
    <div class="map-tall"><iframe src="%s" loading="lazy" title="Map of Cafeto 21 at 1127 Broadway Suite 101, Tacoma WA" allow="management:coordinate"></iframe><p class="mapcap">1127 Broadway, Suite 101 &middot; between S 11th &amp; S 13th</p></div>
  </div>
  <h2>Order ahead, or skip the line</h2>
  <p>The full menu is on <a href="%s" rel="nofollow noopener">DoorDash</a> for delivery and pickup — useful at 4 p.m. sharp, when the kitchen closes and the crepe craving doesn&rsquo;t. The shop posts its day on <a href="%s" rel="nofollow noopener">Instagram</a> too.</p>
  <p class="cta-row"><a class="btn" href="/contact">Questions? Say hello</a> <a href="/crepes">The menu &rarr;</a></p>
</article>''' % (ADDR, DIRS, PHONE_TEL, PHONE_DISPLAY, EMAIL, EMAIL, MAP_Q, DOORDASH, IG))

# ---------------- CONTACT ----------------
pages["contact.html"] = (
    head("Contact & Feedback — Cafeto 21, Downtown Tacoma WA",
         "Tell us what you thought of the crepes, ask about a big order, or send a note from downtown Tacoma — the form goes straight to the shop.",
         "/contact",
         [breadcrumb("Contact", "/contact"),
          service_node("Contact Cafeto 21", "Customer contact",
                       "Questions, feedback and big-order inquiries for Cafeto 21, 1127 Broadway Suite 101, Tacoma WA 98402 — open 8 a.m. to 4 p.m. daily.",
                       "/contact")])
    + nav("/contact")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Contact</p>
  <p class="lab mono">Say hello</p>
  <h1>Tell us about the crepes</h1>
  <p class="lede">Loved the Berries Delight? Dreaming of a make-your-own with marzipan? Planning a breakfast for a crowd, or just want the hours again? This form goes straight to the shop.</p>
  <form class="cform" method="post" action="/contact">
    <p><label for="f-name">Name</label><input id="f-name" name="name" type="text" maxlength="120" required></p>
    <p><label for="f-email">Email <span class="fine">so we can answer</span></label><input id="f-email" name="email" type="email" maxlength="120" required></p>
    <p><label for="f-msg">Feedback, a big order, or a question? <span class="fine">(optional)</span></label><textarea id="f-msg" name="message" rows="4" maxlength="4000"></textarea></p>
    <p><button class="btn" type="submit">Send it</button></p>
  </form>
  <div class="plate dot-matcha">
    <p class="lab mono">Direct</p>
    <p class="addr"><a href="mailto:%s">%s</a><br><a href="tel:%s">%s</a></p>
    <p class="addr">%s</p>
    <p>Open 8 a.m. &ndash; 4 p.m., every day.</p>
  </div>
  <div class="map-tall"><iframe src="%s" loading="lazy" title="Map: Cafeto 21, 1127 Broadway Suite 101, Tacoma WA" allow="management:coordinate"></iframe><p class="mapcap">1127 Broadway, Suite 101 &middot; <a href="%s">Get directions &nearr;</a></p></div>
</article>''' % (EMAIL, EMAIL, PHONE_TEL, PHONE_DISPLAY, ADDR, MAP_Q, DIRS))

# ---------------- PRIVACY ----------------
pages["privacy.html"] = (
    head("Privacy — Cafeto 21, Tacoma WA",
         "How this site handles what you send it: contact-form messages go to the shop's inbox and are used only to answer you. No cookies, no trackers.",
         "/privacy",
         [breadcrumb("Privacy", "/privacy"), store_ld()])
    + nav("/privacy")
    + '''<article class="page">
  <p class="crumbs mono"><a href="/">Home</a> &middot; Privacy</p>
  <h1>What you send us</h1>
  <p>Messages from this site&#8217;s form go straight to the shop&#8217;s inbox — the name, email and note you type, nothing more. We use them to answer you and nothing else. We do not sell, rent or trade your details.</p>
  <p>This site sets no cookies and runs no advertising or analytics trackers. Pages load from our own host with our own stylesheet; there is no third-party script on any page.</p>
  <p>Questions about this page? <a href="/contact">Use the form</a> and ask.</p>
</article>''')

# ---------------- 404 / THANKS (utility) ----------------
pages["404.html"] = (
    head("Page not found — Cafeto 21, Tacoma WA",
         "That page is off the menu. Cafeto 21 — crepes and coffee, open 8 a.m. to 4 p.m. daily on Broadway in downtown Tacoma.",
         "/404")
    + nav("")
    + '''<article class="page">
  <p class="lab mono">404</p>
  <h1>That page is off the menu</h1>
  <p class="lede">No crepes were wasted. The two pages that matter are below.</p>
  <p class="cta-row"><a class="btn" href="/">Back to the front</a> <a href="/crepes">See the crepes</a></p>
</article>''')

pages["thanks.html"] = (
    head("Your note landed — Cafeto 21, Tacoma WA",
         "Thanks — Cafeto 21 has your note and will get back to you. Crepes and coffee, open 8 a.m. to 4 p.m. daily in downtown Tacoma.",
         "/thanks")
    + nav("")
    + '''<article class="page">
  <p class="lab mono">Received</p>
  <h1>Your note landed</h1>
  <p class="lede">The shop has it. While you wait for a reply — the crepe list is right here, and the doors are open 8 to 4 every day.</p>
  <p class="cta-row"><a class="btn" href="/crepes">The crepes</a> <a href="/">Back to the site</a></p>
</article>''')

# ---------------- CSS ----------------
CSS = """:root{
  --ink:#221a14; --band:#2f241a; --nutella:#4a2c1a; --buckwheat:#8a5a33; --caramel:#c98b4a;
  --berry:#a3243f; --berry-dk:#71182e; --matcha:#6f8f4f; --matcha-dk:#516b38;
  --paper:#fbf6ec; --cream:#f3ead6; --soft:#e6d6b8; --rule:#4a3b2a; --dim:#8b7a66;
  --serif:Georgia,"Iowan Old Style","Times New Roman",serif;
  --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{color-scheme:light}
body{background:var(--paper);color:var(--ink);font-family:var(--serif);font-size:17px;line-height:1.6}
.topline{height:8px;background:linear-gradient(90deg,var(--berry-dk),var(--berry) 30%,var(--caramel) 65%,var(--matcha))}
.skip{position:absolute;left:-9999px;top:0;background:var(--ink);color:var(--cream);padding:.5rem 1rem;z-index:9}
.skip:focus{left:1rem;top:1rem}
a{color:var(--buckwheat)}
a:hover{color:var(--nutella)}
.mono{font-family:var(--mono)}
header.site{padding:1rem max(1.1rem, calc((100vw - 1012px)/2));border-bottom:1px solid var(--rule);display:flex;flex-wrap:wrap;gap:.6rem 1.5rem;align-items:center;justify-content:space-between}
.brand{font-size:13px;margin:0;display:flex;align-items:center;gap:.6rem}
.brand a{color:var(--ink);text-decoration:none;display:flex;align-items:center;gap:.6rem}
.wordmark{font-weight:700;font-size:1.45rem;letter-spacing:.22em;text-transform:uppercase}
.disc{display:inline-flex;align-items:center;justify-content:center;width:2rem;height:2rem;border-radius:50%;background:var(--caramel);color:var(--ink);font-family:var(--mono);font-size:.95rem;font-weight:700;border:2px solid var(--nutella)}
header.site nav p{display:flex;flex-wrap:wrap;gap:.35rem 1.1rem;justify-content:flex-end;margin:0}
header.site nav a{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;color:var(--rule)}
header.site nav a:hover{color:var(--berry-dk);text-decoration:underline;text-underline-offset:4px}
header.site nav a[aria-current="page"]{color:var(--berry-dk);text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:4px}
main{max-width:1060px;margin:0 auto;padding:0 1.5rem 3.5rem}
.lab{font-family:var(--mono);font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--berry-dk);margin-bottom:.6rem}
.hero{background:var(--ink);color:var(--cream);margin:1.5rem 0;padding:clamp(2rem,5.5vw,4rem) clamp(1.2rem,4vw,3.5rem);display:grid;grid-template-columns:minmax(0,1.15fr) minmax(240px,.85fr);gap:2rem 2.5rem;align-items:center;border-radius:16px}
.hero .lab{color:var(--caramel)}
.hero h1.mark{font-size:clamp(3.4rem,11vw,6rem);line-height:1;font-weight:700;letter-spacing:.06em;text-transform:uppercase;margin:.1rem 0 0;display:flex;align-items:center;gap:.6rem;flex-wrap:wrap}
.disc.big{width:clamp(3rem,8vw,4.6rem);height:clamp(3rem,8vw,4.6rem);font-size:clamp(1.4rem,4vw,2.2rem);background:var(--caramel);color:var(--ink)}
.mark-sub{font-size:12px;letter-spacing:.28em;text-transform:uppercase;color:var(--soft);margin:.9rem 0 1rem}
.hero .sub{max-width:34rem;color:var(--cream);font-size:1.05rem;line-height:1.55;margin-bottom:1.4rem}
.hero-cta{display:flex;flex-wrap:wrap;gap:.8rem 1.2rem;align-items:center}
.crepe-art{width:100%;height:auto;display:block;border-radius:16px}
.btn{display:inline-block;background:var(--berry);color:#fff;font-family:var(--mono);font-size:13px;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;padding:.8rem 1.3rem;border-radius:999px;border:1px solid var(--berry-dk)}
.btn:hover{background:var(--berry-dk);color:#fff}
.btn.sm{padding:.45rem .8rem;font-size:11px}
a.ghost{color:var(--caramel);font-family:var(--mono);font-size:13px;letter-spacing:.08em;text-transform:uppercase;text-decoration:underline;text-underline-offset:5px}
.panels{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.2rem;margin:1.6rem 0 2.2rem}
.panels>.plate{height:100%}
.plate{position:relative;background:#fff;border:1px solid var(--rule);border-radius:18px;padding:1.7rem 1.4rem 1.4rem;display:flex;flex-direction:column}
.plate::before{content:"";position:absolute;top:1.15rem;right:1.2rem;width:12px;height:12px;border-radius:50%}
.plate.dot-berry::before{background:var(--berry)}
.plate.dot-caramel::before{background:var(--caramel)}
.plate.dot-matcha::before{background:var(--matcha)}
.plate.wide{margin:1.4rem 0;max-width:46rem}
.plate h2{font-size:1.3rem;line-height:1.2;margin-bottom:.5rem}
.plate p{margin-bottom:.7rem}
.plate p:last-child{margin-bottom:0;margin-top:auto}
.band{display:grid;grid-template-columns:minmax(300px,1.25fr) minmax(280px,1fr);gap:1.4rem;align-items:center;background:var(--cream);border:1px solid var(--rule);border-radius:16px;padding:1.6rem}
.band h2{font-size:1.6rem;margin-bottom:.4rem}
.band .ghost{color:var(--berry-dk)}
.band-map{width:100%}
.band-map iframe,.map-tall iframe{width:100%;aspect-ratio:4/3;border:1px solid var(--rule);border-radius:12px;display:block;background:var(--cream)}
.mapcap{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);text-align:center;margin-top:.5rem}
.page{padding-top:1.8rem}
.crumbs{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);margin-bottom:1rem}
h1{font-size:clamp(1.9rem,4.5vw,2.9rem);line-height:1.1;margin-bottom:.8rem}
.lede{font-size:1.15rem;line-height:1.55;max-width:44rem;margin-bottom:1.4rem;color:var(--rule)}
.page h2{font-size:1.35rem;margin:1.6rem 0 .5rem}
.page p{max-width:46rem;margin-bottom:1rem}
ul.spread{list-style:none;margin:0 0 1.2rem;border-top:1px solid var(--rule);max-width:46rem}
ul.spread li{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);gap:.5rem 1.4rem;padding:.65rem 0;border-bottom:1px solid var(--rule);font-size:.98rem}
ul.spread li span{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--berry-dk);padding-top:.15rem}
.price-note{font-family:var(--mono);font-size:12px;line-height:1.7;color:var(--dim);max-width:46rem}
dl.faq{margin:1.6rem 0;border-top:1px solid var(--rule)}
dl.faq dt{font-family:var(--mono);font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--berry-dk);padding:.9rem 0 .2rem}
dl.faq dd{padding:0 0 1rem;border-bottom:1px solid var(--rule);max-width:46rem}
ul.press{list-style:none;margin:0 0 1.2rem}
ul.press li{padding:.5rem 0;border-bottom:1px solid var(--rule)}
.cta-row{display:flex;flex-wrap:wrap;gap:.8rem 1.2rem;align-items:center;margin-top:1.4rem}
.addr{font-family:var(--mono);font-size:14px;letter-spacing:.04em;margin-bottom:.6rem;max-width:46rem;line-height:1.8}
.visit-grid{display:grid;grid-template-columns:minmax(280px,1fr) minmax(280px,1.2fr);gap:1.4rem;align-items:start;margin-bottom:1.6rem}
.map-tall{width:100%}
.cform{max-width:34rem;margin:0 0 1.8rem}
.cform p{margin-bottom:1rem}
.cform label{display:block;font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--rule);margin-bottom:.35rem}
.fine{color:var(--dim);text-transform:none;letter-spacing:.02em}
.cform input,.cform textarea{width:100%;font-family:var(--serif);font-size:16px;padding:.65rem .8rem;border:1px solid var(--rule);border-radius:10px;background:#fff;color:var(--ink)}
.cform input:focus,.cform textarea:focus{outline:2px solid var(--berry);outline-offset:1px}
footer{background:var(--ink);color:var(--cream);padding:1.8rem 1.5rem;text-align:center}
footer p.footline{font-family:var(--mono);font-size:12px;letter-spacing:.08em;line-height:1.9;max-width:none;margin:0 auto}
footer a{color:var(--caramel)}
footer p.fine{color:#d8c3a5;font-size:11px}
@media (max-width:640px){
  body{font-size:16px}
  header.site nav p{justify-content:flex-start}
  .hero{grid-template-columns:1fr;padding:2rem 1.1rem}
  .band,.visit-grid{grid-template-columns:1fr}
  ul.spread li{grid-template-columns:1fr;gap:.2rem}
  main{padding:0 1.1rem 3rem}
}"""

def write(name, content):
    with open(os.path.join(PUBLIC, name), "w", encoding="utf-8") as f:
        f.write(content if content.endswith("\n") else content + "\n")

os.makedirs(PUBLIC, exist_ok=True)
for name, content in pages.items():
    write(name, content + FOOTER)
write("style.css", CSS)

core = ["index.html", "crepes.html", "coffee-matcha.html", "our-story.html",
        "visit.html", "contact.html", "privacy.html"]
today = "2026-11-25"
locs = "\n".join('<url><loc>%s%s</loc><lastmod>%s</lastmod></url>' %
                 (ORIGIN, "/" if f == "index.html" else "/" + f[:-5], today) for f in core)
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % locs)
write("robots.txt", "User-agent: *\nDisallow:\n\nSitemap: %s/sitemap.xml\n" % ORIGIN)
# static assets that live at repo root must ride into public/ (server serves public/ only)
import shutil
for asset in ("pixel.gif", "favicon.svg"):
    src = os.path.join(HERE, asset)
    if os.path.exists(src):
        shutil.copyfile(src, os.path.join(PUBLIC, asset))
print("built %d pages + css + sitemap + robots" % len(pages))
