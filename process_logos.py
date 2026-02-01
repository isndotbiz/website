#!/usr/bin/env python3
from PIL import Image
import numpy as np
import os

OUTPUT_DIR = "D:/workspace/ISNBIZ_Files/assets/premium_v2/logos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

CIRCULAR_LOGO = "D:/workspace/ISNBIZ_Files/assets/premium_v2/logos/source_9(1).png"
ISS_JPG = "D:/workspace/ISNBIZ_Files/assets/premium_v2/logos/source_ISS.jpg"


def save_png_and_webp(img, base_name):
    png_path = os.path.join(OUTPUT_DIR, base_name + ".png")
    webp_path = os.path.join(OUTPUT_DIR, base_name + ".webp")
    img.save(png_path, "PNG", optimize=True)
    img.save(webp_path, "WEBP", quality=85)
    png_size = os.path.getsize(png_path)
    webp_size = os.path.getsize(webp_path)
    print("  %s.png  = %s bytes (%dx%d)" % (base_name, format(png_size, ','), img.size[0], img.size[1]))
    print("  %s.webp = %s bytes" % (base_name, format(webp_size, ',')))
    return png_path, webp_path


def crop_top_half_and_remove_black(iss_jpg_path):
    img = Image.open(iss_jpg_path)
    arr = np.array(img)
    h = arr.shape[0]
    mid = h // 2
    top = arr[:mid].copy()

    r = top[:,:,0].astype(float)
    g = top[:,:,1].astype(float)
    b = top[:,:,2].astype(float)
    brightness = r + g + b
    content_mask = brightness > 25
    rows_with_content = np.any(content_mask, axis=1)
    cols_with_content = np.any(content_mask, axis=0)
    content_rows = np.where(rows_with_content)[0]
    content_cols = np.where(cols_with_content)[0]

    if len(content_rows) == 0 or len(content_cols) == 0:
        raise ValueError("No content found in top half")

    pad_y = max(10, int((content_rows[-1] - content_rows[0]) * 0.02))
    pad_x = max(10, int((content_cols[-1] - content_cols[0]) * 0.02))
    y1 = max(0, content_rows[0] - pad_y)
    y2 = min(top.shape[0], content_rows[-1] + pad_y + 1)
    x1 = max(0, content_cols[0] - pad_x)
    x2 = min(top.shape[1], content_cols[-1] + pad_x + 1)

    cropped = top[y1:y2, x1:x2].copy()
    print("  Cropped: (%d:%d, %d:%d) = %dx%d" % (y1, y2, x1, x2, cropped.shape[1], cropped.shape[0]))

    r = cropped[:,:,0].astype(float)
    g = cropped[:,:,1].astype(float)
    b = cropped[:,:,2].astype(float)
    max_channel = np.maximum(np.maximum(r, g), b)

    low_thresh = 12
    high_thresh = 45
    alpha = np.zeros_like(max_channel)
    mask_mid = (max_channel >= low_thresh) & (max_channel < high_thresh)
    alpha[mask_mid] = ((max_channel[mask_mid] - low_thresh) / (high_thresh - low_thresh)) * 255
    alpha[max_channel >= high_thresh] = 255
    alpha = alpha.clip(0, 255).astype(np.uint8)

    semi_mask = (alpha > 0) & (alpha < 255)
    alpha_factor = alpha[semi_mask].astype(float) / 255.0
    for ch_idx in range(3):
        ch = cropped[:,:,ch_idx].astype(float)
        ch_vals = ch[semi_mask]
        unpremultiplied = np.minimum(ch_vals / np.maximum(alpha_factor, 0.01), 255)
        ch[semi_mask] = unpremultiplied
        cropped[:,:,ch_idx] = ch.clip(0, 255).astype(np.uint8)

    rgba = np.dstack([cropped, alpha])
    return Image.fromarray(rgba, "RGBA")


def resize_maintain_aspect(img, width=None, height=None):
    orig_w, orig_h = img.size
    if width and not height:
        ratio = width / orig_w
        new_h = int(orig_h * ratio)
        return img.resize((width, new_h), Image.LANCZOS)
    elif height and not width:
        ratio = height / orig_h
        new_w = int(orig_w * ratio)
        return img.resize((new_w, height), Image.LANCZOS)
    elif width and height:
        return img.resize((width, height), Image.LANCZOS)
    return img


print("\n[1] favicon.png - 32x32")
circular = Image.open(CIRCULAR_LOGO).convert("RGBA")
save_png_and_webp(circular.resize((32, 32), Image.LANCZOS), "favicon")

print("\n[2] favicon_16.png - 16x16")
save_png_and_webp(circular.resize((16, 16), Image.LANCZOS), "favicon_16")

print("\n[3] apple_touch_icon.png - 180x180")
save_png_and_webp(circular.resize((180, 180), Image.LANCZOS), "apple_touch_icon")

print("\n[4] navbar_logo.png - height=100px, transparent")
wordmark = crop_top_half_and_remove_black(ISS_JPG)
print("  Full wordmark: %dx%d" % wordmark.size)
navbar = resize_maintain_aspect(wordmark, height=100)
save_png_and_webp(navbar, "navbar_logo")

print("\n[5] hero_logo.png - width=1000px, transparent")
hero = resize_maintain_aspect(wordmark, width=1000)
save_png_and_webp(hero, "hero_logo")

print("\n[6] footer_logo.png - height=50px, transparent")
footer = resize_maintain_aspect(wordmark, height=50)
save_png_and_webp(footer, "footer_logo")

print("\n[7] square_icon.png - 180x180")
save_png_and_webp(circular.resize((180, 180), Image.LANCZOS), "square_icon")

print("\n" + "=" * 60)
print("ALL LOGOS PROCESSED SUCCESSFULLY")
print("=" * 60)

output_files = [
    "favicon.png", "favicon.webp",
    "favicon_16.png", "favicon_16.webp",
    "apple_touch_icon.png", "apple_touch_icon.webp",
    "navbar_logo.png", "navbar_logo.webp",
    "hero_logo.png", "hero_logo.webp",
    "footer_logo.png", "footer_logo.webp",
    "square_icon.png", "square_icon.webp",
]

print("\nGenerated %d files:" % len(output_files))
total_size = 0
for f in output_files:
    path = os.path.join(OUTPUT_DIR, f)
    if os.path.exists(path):
        size = os.path.getsize(path)
        total_size += size
        print("  %-30s %10s bytes" % (f, format(size, ',')))
    else:
        print("  %-30s MISSING!" % f)
print("\nTotal: %s bytes (%.1f KB)" % (format(total_size, ','), total_size/1024))
