from PIL import Image
import os

SRC = "/home/jdmal/workspace/ISNBIZ_Files/assets/premium_v2/logos"
OUT = "/home/jdmal/workspace/ISNBIZ_Files/assets/premium_v3/logos"
os.makedirs(OUT, exist_ok=True)

# 1. Circular logo -> favicon sizes
circular = Image.open(f"{SRC}/source_9(1).png").convert("RGBA")
# favicon 32x32
circular.resize((32, 32), Image.LANCZOS).save(f"{OUT}/favicon.png")
circular.resize((32, 32), Image.LANCZOS).save(f"{OUT}/favicon.webp", "WebP", quality=90)
# favicon 16x16
circular.resize((16, 16), Image.LANCZOS).save(f"{OUT}/favicon_16.png")
# apple touch icon 180x180
circular.resize((180, 180), Image.LANCZOS).save(f"{OUT}/apple_touch_icon.png")
circular.resize((180, 180), Image.LANCZOS).save(f"{OUT}/apple_touch_icon.webp", "WebP", quality=90)
# square icon 180x180
circular.resize((180, 180), Image.LANCZOS).save(f"{OUT}/square_icon.png")
circular.resize((180, 180), Image.LANCZOS).save(f"{OUT}/square_icon.webp", "WebP", quality=90)
print("Circular logo variants created")

# 2. High-res wordmark ISS.jpg -> crop top half (white on black) -> remove black bg
iss = Image.open(f"{SRC}/source_ISS.jpg").convert("RGB")
w, h = iss.size  # 4096x3112
# Top half has white text on black
top_half = iss.crop((0, 0, w, h // 2))  # 4096x1556

# Remove black background - make black pixels transparent
top_rgba = top_half.convert("RGBA")
data = top_rgba.getdata()
new_data = []
for r, g, b, a in data:
    # If pixel is very dark (close to black), make transparent
    if r < 40 and g < 40 and b < 40:
        new_data.append((r, g, b, 0))
    else:
        new_data.append((r, g, b, 255))
top_rgba.putdata(new_data)

# Crop to content (remove transparent edges)
bbox = top_rgba.getbbox()
if bbox:
    top_rgba = top_rgba.crop(bbox)

# Hero logo: width=1000px
hero_w = 1000
hero_h = int(top_rgba.height * (hero_w / top_rgba.width))
hero = top_rgba.resize((hero_w, hero_h), Image.LANCZOS)
hero.save(f"{OUT}/hero_logo.png")
hero.save(f"{OUT}/hero_logo.webp", "WebP", quality=85)
print(f"Hero logo: {hero_w}x{hero_h}")

# Navbar logo: height=100px
nav_h = 100
nav_w = int(top_rgba.width * (nav_h / top_rgba.height))
nav = top_rgba.resize((nav_w, nav_h), Image.LANCZOS)
nav.save(f"{OUT}/navbar_logo.png")
nav.save(f"{OUT}/navbar_logo.webp", "WebP", quality=85)
print(f"Navbar logo: {nav_w}x{nav_h}")

# Footer logo: height=50px
foot_h = 50
foot_w = int(top_rgba.width * (foot_h / top_rgba.height))
foot = top_rgba.resize((foot_w, foot_h), Image.LANCZOS)
foot.save(f"{OUT}/footer_logo.png")
foot.save(f"{OUT}/footer_logo.webp", "WebP", quality=85)
print(f"Footer logo: {foot_w}x{foot_h}")

# 3. Horizontal wordmark with transparency (for alternate use)
horiz = Image.open(f"{SRC}/source_ISS2500.png").convert("RGBA")
# Already has transparency, just resize
horiz_100 = horiz.resize((int(horiz.width * (100 / horiz.height)), 100), Image.LANCZOS)
horiz_100.save(f"{OUT}/horizontal_wordmark.png")
horiz_100.save(f"{OUT}/horizontal_wordmark.webp", "WebP", quality=85)
print(f"Horizontal wordmark: {horiz_100.size}")

# Report
print("\n--- Output Files ---")
for f in sorted(os.listdir(OUT)):
    if not f.startswith("source_"):
        path = os.path.join(OUT, f)
        size = os.path.getsize(path)
        print(f"  {f}: {size/1024:.1f} KB")
