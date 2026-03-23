#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MalibuTechTeam — GitHub Profile SVG Generator
Run this script to regenerate all SVG assets for the README.

Color palette (from mbt_tebexSite):
  --bg-primary:      #000000
  --bg-card:         #1c1c1c
  --accent-violet:   #7C3AED  (primary brand)
  --accent-violet-l: #8b5cf6  (scripts category / lighter violet)
  --accent-blue:     #3b82f6  (secondary accent)
  --accent-rose:     #f43f5e  (destructive / highlight)
  --text-primary:    #ffffff
  --text-muted:      rgba(255,255,255,0.7)
"""

# ── Palette (from logo: navy bg + emerald/mint green) ─────────────────────────
BG        = "#0a1018"   # deep navy (darker than logo bg, for full-bleed sections)
BG_CARD   = "#102038"   # logo background navy (card surfaces)
PRIMARY   = "#4DD9A2"   # bright mint — logo highlight / main accent
MID       = "#208868"   # mid emerald — logo M body
DARK_G    = "#085848"   # deep green — logo M shadow
ROSE      = "#f43f5e"   # rose — stars / destructive (from website)
WHITE     = "#ffffff"
MUTED     = "#ffffffb3"

# aliases kept for internal use
VIOLET   = MID
VIOLET_L = PRIMARY
BLUE     = PRIMARY


def generate_banner():
    svg = f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="880" height="180" viewBox="0 0 880 180">
  <defs>
    <style><![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;900&display=swap');
    ]]></style>
    <pattern id="dots" x="0" y="0" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="1" fill="#ffffff" fill-opacity="0.04"/>
    </pattern>
    <radialGradient id="g1" cx="22%" cy="45%" r="55%">
      <stop offset="0%" stop-color="{MID}" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="{BG}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="g2" cx="78%" cy="55%" r="55%">
      <stop offset="0%" stop-color="{PRIMARY}" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="{BG}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="{MID}"/>
      <stop offset="48%"  stop-color="{WHITE}"/>
      <stop offset="100%" stop-color="{PRIMARY}"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Base + dot grid -->
  <rect width="880" height="180" fill="{BG}" rx="14"/>
  <rect width="880" height="180" fill="url(#dots)" rx="14"/>

  <!-- Colour glows -->
  <rect width="880" height="180" fill="url(#g1)" rx="14"/>
  <rect width="880" height="180" fill="url(#g2)" rx="14"/>

  <!-- Outer border -->
  <rect width="878" height="178" x="1" y="1" fill="none"
        stroke="{VIOLET}" stroke-width="1" stroke-opacity="0.55" rx="14"/>

  <!-- Top accent lines + corner dots -->
  <line x1="44" y1="38" x2="290" y2="38" stroke="{MID}"     stroke-width="0.7" stroke-opacity="0.6"/>
  <line x1="590" y1="38" x2="836" y2="38" stroke="{PRIMARY}" stroke-width="0.7" stroke-opacity="0.6"/>
  <circle cx="37"  cy="38"  r="3.5" fill="{MID}"     opacity="0.9"/>
  <circle cx="843" cy="38"  r="3.5" fill="{PRIMARY}" opacity="0.9"/>

  <!-- Bottom accent lines + corner dots -->
  <line x1="44" y1="142" x2="290" y2="142" stroke="{PRIMARY}" stroke-width="0.7" stroke-opacity="0.6"/>
  <line x1="590" y1="142" x2="836" y2="142" stroke="{MID}"     stroke-width="0.7" stroke-opacity="0.6"/>
  <circle cx="37"  cy="142" r="3.5" fill="{PRIMARY}" opacity="0.9"/>
  <circle cx="843" cy="142" r="3.5" fill="{MID}"     opacity="0.9"/>

  <!-- Main title -->
  <text x="440" y="101"
        font-family="Outfit, sans-serif" font-weight="900" font-size="52"
        fill="url(#titleGrad)" text-anchor="middle"
        letter-spacing="10" filter="url(#glow)">MALIBU TECH TEAM</text>

  <!-- Subtitle -->
  <text x="440" y="130"
        font-family="Outfit, sans-serif" font-weight="400" font-size="13"
        fill="{PRIMARY}" text-anchor="middle" letter-spacing="5" opacity="0.85">
    PREMIUM FIVEM RESOURCES  \u2022  SCRIPTS &amp; MAPS
  </text>
</svg>"""
    with open("banner.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("banner.svg OK")


def generate_about():
    svg = f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="430" height="226" viewBox="0 0 430 226">
  <defs>
    <style><![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');
    ]]></style>
    <radialGradient id="ag" cx="0%" cy="0%" r="70%">
      <stop offset="0%" stop-color="{VIOLET}" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="{BG_CARD}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="430" height="226" fill="{BG_CARD}" rx="14"/>
  <rect width="430" height="226" fill="url(#ag)"   rx="14"/>
  <rect width="428" height="224" x="1" y="1" fill="none"
        stroke="{VIOLET}" stroke-width="1" stroke-opacity="0.45" rx="14"/>

  <!-- Label -->
  <rect x="20" y="20" width="108" height="25" fill="{VIOLET}" fill-opacity="0.15" rx="5"/>
  <rect x="20" y="20" width="108" height="25" fill="none"
        stroke="{VIOLET}" stroke-width="0.8" stroke-opacity="0.5" rx="5"/>
  <text x="74" y="37"
        font-family="Outfit, sans-serif" font-weight="700" font-size="11"
        fill="{VIOLET_L}" text-anchor="middle" letter-spacing="2">WHO WE ARE</text>

  <line x1="20" y1="62" x2="410" y2="62"
        stroke="{VIOLET}" stroke-width="0.5" stroke-opacity="0.35"/>

  <!-- Body -->
  <text x="20" y="88"
        font-family="Outfit, sans-serif" font-weight="700" font-size="15"
        fill="{WHITE}">Born from passion. Built with precision.</text>

  <text x="20" y="115" font-family="Outfit, sans-serif" font-size="12.5" fill="{MUTED}">
    A team of developers with 3+ years in FiveM,
  </text>
  <text x="20" y="133" font-family="Outfit, sans-serif" font-size="12.5" fill="{MUTED}">
    combining originality with optimal performance.
  </text>
  <text x="20" y="161" font-family="Outfit, sans-serif" font-size="12.5" fill="{MUTED}">
    We craft scripts &amp; maps that bring a breath of
  </text>
  <text x="20" y="179" font-family="Outfit, sans-serif" font-size="12.5" fill="{MUTED}">
    fresh air to every serious FiveM server.
  </text>

  <line x1="20" y1="204" x2="410" y2="204"
        stroke="{BLUE}" stroke-width="0.5" stroke-opacity="0.35"/>
  <text x="20" y="218"
        font-family="Outfit, sans-serif" font-size="10"
        fill="{BLUE}" letter-spacing="1" opacity="0.7">malibutechteam.com  \u2022  MBT</text>
</svg>"""
    with open("about.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("about.svg OK")


def generate_divider(filename: str, label: str):
    svg = f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="880" height="50" viewBox="0 0 880 50">
  <defs>
    <style><![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@700&display=swap');
    ]]></style>
  </defs>
  <rect width="880" height="50" fill="{BG}"/>
  <line x1="20"  y1="25" x2="338" y2="25" stroke="{VIOLET}" stroke-width="0.7" stroke-opacity="0.5"/>
  <text x="440" y="30"
        font-family="Outfit, sans-serif" font-weight="700" font-size="12"
        fill="{VIOLET_L}" text-anchor="middle" letter-spacing="5">{label}</text>
  <line x1="542" y1="25" x2="860" y2="25" stroke="{BLUE}" stroke-width="0.7" stroke-opacity="0.5"/>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"{filename} OK")


def generate_reviews():
    reviews = [
        {
            "text1": "Absolutely AMAZING and everyone loves it!!",
            "text2": "The support was 10/10!",
            "author": "Oomen",
            "product": "MBT Halloween",
        },
        {
            "text1": "The guys do their job 11/10!",
            "text2": "I will buy even more of their scripts.",
            "author": "uajdumbass",
            "product": "MBT Logo HUD",
        },
        {
            "text1": "Config is straightforward, support is top notch",
            "text2": "— very helpful and patient.",
            "author": "sonofabitchcolumbo",
            "product": "MBT Elevator",
        },
        {
            "text1": "Great customer service. Polite and attentive.",
            "text2": "The MLOs themselves are top tier.",
            "author": "makvely",
            "product": "MBT Elevator",
        },
    ]

    PAD   = 12
    GAP   = 16
    CW    = 420
    CH    = 122
    ROW1  = 52
    ROW2  = ROW1 + CH + GAP
    TOTAL = ROW2 + CH + PAD

    positions = [
        (PAD,           ROW1),
        (PAD + CW + GAP, ROW1),
        (PAD,           ROW2),
        (PAD + CW + GAP, ROW2),
    ]

    cards = ""
    for i, (r, (cx, cy)) in enumerate(zip(reviews, positions)):
        cards += f"""
  <rect x="{cx}" y="{cy}" width="{CW}" height="{CH}" fill="{BG_CARD}" rx="12"/>
  <rect x="{cx}" y="{cy}" width="{CW}" height="{CH}" fill="none"
        stroke="{VIOLET}" stroke-width="0.8" stroke-opacity="0.28" rx="12"/>
  <text x="{cx + CW - 16}" y="{cy + 54}" font-family="Outfit, sans-serif" font-size="64"
        fill="{VIOLET}" opacity="0.10" text-anchor="end">\u201c</text>
  <text x="{cx + 14}" y="{cy + 22}" font-family="Outfit, sans-serif" font-size="12"
        fill="{ROSE}">\u2605 \u2605 \u2605 \u2605 \u2605</text>
  <text x="{cx + 14}" y="{cy + 46}" font-family="Outfit, sans-serif" font-size="12.5"
        fill="{WHITE}" opacity="0.88">{r['text1']}</text>
  <text x="{cx + 14}" y="{cy + 63}" font-family="Outfit, sans-serif" font-size="12.5"
        fill="{WHITE}" opacity="0.88">{r['text2']}</text>
  <line x1="{cx + 14}" y1="{cy + 80}" x2="{cx + CW - 14}" y2="{cy + 80}"
        stroke="{VIOLET}" stroke-width="0.5" stroke-opacity="0.28"/>
  <text x="{cx + 14}" y="{cy + 100}" font-family="Outfit, sans-serif" font-weight="700"
        font-size="11" fill="{VIOLET_L}">\u2014 {r['author']}</text>
  <text x="{cx + CW - 14}" y="{cy + 100}" font-family="Outfit, sans-serif" font-size="10"
        fill="{BLUE}" text-anchor="end" opacity="0.75">{r['product']}</text>"""

    svg = f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="880" height="{TOTAL}" viewBox="0 0 880 {TOTAL}">
  <defs>
    <style><![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&display=swap');
    ]]></style>
  </defs>
  <rect width="880" height="{TOTAL}" fill="{BG}"/>
  <rect x="296" y="8" width="288" height="26" fill="{VIOLET}" fill-opacity="0.15" rx="5"/>
  <rect x="296" y="8" width="288" height="26" fill="none"
        stroke="{VIOLET}" stroke-width="0.8" stroke-opacity="0.45" rx="5"/>
  <text x="440" y="25" font-family="Outfit, sans-serif" font-weight="700" font-size="11"
        fill="{VIOLET_L}" text-anchor="middle" letter-spacing="3">VERIFIED CUSTOMER REVIEWS</text>
{cards}
</svg>"""
    with open("reviews.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("reviews.svg OK")


if __name__ == "__main__":
    generate_banner()
    generate_about()
    generate_divider("divider_team.svg",  "THE  TEAM")
    generate_divider("divider_stack.svg", "TECH  STACK")
    generate_reviews()
    print("\nAll SVGs generated successfully!")
