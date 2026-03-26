#!/usr/bin/env python3
"""
GEMS QR Code Generator
======================
Generates 40 PNG QR codes — one per quality — for the book v2.

Each QR code encodes the direct GitHub URL to the quality's content folder
in gems-core. This allows any AI agent or QR scanner to navigate directly
to the quality content.

Requirements:
    pip install qrcode[pil]

Output:
    ./qr_codes/GEMS-QR-[quality-id].png
"""

import os

try:
    import qrcode
    from qrcode.image.styledpil import StyledPilImage
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    print("ERROR: Install dependencies first: pip install qrcode[pil]")
    print("Then run: python3 generate_qr_codes.py")
    exit(1)


BASE_URL = "https://github.com/Arcee11/gems-core/tree/main/qualities"
OUTPUT_DIR = "qr_codes"

QUALITIES = [
    {"id": "resilient",      "page": 1,  "title": "Resilient"},
    {"id": "confident",      "page": 2,  "title": "Confident"},
    {"id": "empowered",      "page": 3,  "title": "Empowered"},
    {"id": "purpose-driven", "page": 4,  "title": "Purpose-Driven"},
    {"id": "peaceful",       "page": 5,  "title": "Peaceful"},
    {"id": "ambitious",      "page": 6,  "title": "Ambitious"},
    {"id": "authentic",      "page": 7,  "title": "Authentic"},
    {"id": "grounded",       "page": 8,  "title": "Grounded"},
    {"id": "mindful",        "page": 9,  "title": "Mindful"},
    {"id": "courageous",     "page": 10, "title": "Courageous"},
    {"id": "grateful",       "page": 11, "title": "Grateful"},
    {"id": "disciplined",    "page": 12, "title": "Disciplined"},
    {"id": "creative",       "page": 13, "title": "Creative"},
    {"id": "focused",        "page": 14, "title": "Focused"},
    {"id": "joyful",         "page": 15, "title": "Joyful"},
    {"id": "connected",      "page": 16, "title": "Connected"},
    {"id": "self-aware",     "page": 17, "title": "Self-Aware"},
    {"id": "determined",     "page": 18, "title": "Determined"},
    {"id": "generous",       "page": 19, "title": "Generous"},
    {"id": "humble",         "page": 20, "title": "Humble"},
    {"id": "hopeful",        "page": 21, "title": "Hopeful"},
    {"id": "adaptable",      "page": 22, "title": "Adaptable"},
    {"id": "loving",         "page": 23, "title": "Loving"},
    {"id": "energized",      "page": 24, "title": "Energized"},
    {"id": "patient",        "page": 25, "title": "Patient"},
    {"id": "honest",         "page": 26, "title": "Honest"},
    {"id": "worthy",         "page": 27, "title": "Worthy"},
    {"id": "present",        "page": 28, "title": "Present"},
    {"id": "accountable",    "page": 29, "title": "Accountable"},
    {"id": "wise",           "page": 30, "title": "Wise"},
    {"id": "curious",        "page": 31, "title": "Curious"},
    {"id": "forgiving",      "page": 32, "title": "Forgiving"},
    {"id": "expressive",     "page": 33, "title": "Expressive"},
    {"id": "still",          "page": 34, "title": "Still"},
    {"id": "trusting",       "page": 35, "title": "Trusting"},
    {"id": "growing",        "page": 36, "title": "Growing"},
    {"id": "committed",      "page": 37, "title": "Committed"},
    {"id": "open",           "page": 38, "title": "Open"},
    {"id": "free",           "page": 39, "title": "Free"},
    {"id": "legendary",      "page": 40, "title": "Legendary"},
]


def generate_qr(quality):
    url = f"{BASE_URL}/{quality['id']}"

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Add label below QR
    qr_width, qr_height = img.size
    label_height = 60
    final = Image.new("RGB", (qr_width, qr_height + label_height), "white")
    final.paste(img, (0, 0))

    draw = ImageDraw.Draw(final)

    # Try to use a font, fall back to default
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    except Exception:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Title
    title_text = quality["title"]
    title_bbox = draw.textbbox((0, 0), title_text, font=font_title)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(((qr_width - title_w) // 2, qr_height + 8), title_text, fill="black", font=font_title)

    # Sub URL
    sub_text = f"gems://quality/{quality['id']}"
    sub_bbox = draw.textbbox((0, 0), sub_text, font=font_sub)
    sub_w = sub_bbox[2] - sub_bbox[0]
    draw.text(((qr_width - sub_w) // 2, qr_height + 34), sub_text, fill="#666666", font=font_sub)

    return final


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Generating {len(QUALITIES)} QR codes → ./{OUTPUT_DIR}/\n")

    for q in QUALITIES:
        filename = f"{OUTPUT_DIR}/GEMS-QR-p{q['page']:02d}-{q['id']}.png"
        img = generate_qr(q)
        img.save(filename)
        print(f"  ✓ Page {q['page']:2d} | {q['title']:20s} → {filename}")

    print(f"\n✅ All {len(QUALITIES)} QR codes generated in ./{OUTPUT_DIR}/")
    print("\nEach QR code encodes:")
    print(f"  {BASE_URL}/[quality-id]")
    print("\nPlace qr_codes/ folder in gems-core repo for reference.")
    print("Use qr-generator.html (in gems-signup) for browser-based generation.")


if __name__ == "__main__":
    main()
