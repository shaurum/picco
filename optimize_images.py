import re
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

QUALITY = 85
DOCS_DIR = Path("docs")
RASTER_EXTS = {'.png', '.jpg', '.jpeg'}


def convert_to_webp(filepath):
    img = Image.open(filepath)
    webp_path = filepath.with_suffix('.webp')
    kwargs = {'quality': QUALITY, 'method': 6}
    if filepath.suffix.lower() == '.png' and img.mode in ('RGBA', 'LA', 'P'):
        img = img.convert('RGBA')
    img.save(webp_path, 'webp', **kwargs)
    old_size = filepath.stat().st_size
    new_size = webp_path.stat().st_size
    filepath.unlink()
    return old_size, new_size


def optimize_webp(filepath):
    old_size = filepath.stat().st_size
    img = Image.open(filepath)
    img.save(filepath, 'webp', quality=QUALITY, method=6)
    new_size = filepath.stat().st_size
    return old_size, new_size


def minify_svg(filepath):
    content = filepath.read_text(encoding='utf-8')
    updated = content
    updated = re.sub(r'<!--.*?-->', '', updated, flags=re.DOTALL)
    updated = re.sub(r'<!DOCTYPE[^>]*>', '', updated, flags=re.DOTALL)
    updated = re.sub(r'>\s+<', '><', updated)
    updated = re.sub(r'^\s+', '', updated, flags=re.MULTILINE)
    updated = re.sub(r'\s+$', '', updated, flags=re.MULTILINE)
    updated = re.sub(r'\n{2,}', '\n', updated)
    updated = updated.strip()
    if updated != content:
        filepath.write_text(updated, encoding='utf-8')
        return True
    return False


def update_refs_in_file(filepath):
    content = filepath.read_text(encoding='utf-8')
    updated = content
    for ext in ('.png', '.jpg', '.jpeg'):
        e = ext.lstrip('.')
        updated = re.sub(r'(\]\()([^)]+?)\.' + re.escape(e) + r'(\))', r'\1\2.webp\3', updated)
        updated = re.sub(r'(src=")([^"]+?)\.' + re.escape(e) + r'(")', r'\1\2.webp\3', updated)
        updated = re.sub(r"(src=')([^']+?)\." + re.escape(e) + r"(')", r'\1\2.webp\3', updated)
        updated = re.sub(r'(poster=")([^"]+?)\.' + re.escape(e) + r'(")', r'\1\2.webp\3', updated)
        updated = re.sub(r"(poster=')([^']+?)\." + re.escape(e) + r"(')", r'\1\2.webp\3', updated)
        updated = re.sub(r'(avatar:\s*)([^\s]+?)\.' + re.escape(e) + r'(\s*)$', r'\1\2.webp\3', updated, flags=re.MULTILINE)
    if updated != content:
        filepath.write_text(updated, encoding='utf-8')
        return True
    return False


def main():
    total_old = 0
    total_new = 0

    print("=== Converting PNG/JPG to WebP ===")
    count = 0
    for fp in sorted(DOCS_DIR.rglob('*')):
        if not fp.is_file() or fp.suffix.lower() not in RASTER_EXTS:
            continue
        old_s, new_s = convert_to_webp(fp)
        total_old += old_s
        total_new += new_s
        count += 1
        print(f"  {fp.relative_to(DOCS_DIR.parent)}: {old_s//1024}K -> {new_s//1024}K")
    print(f"  Converted {count} images\n")

    print("=== Re-optimizing WebP ===")
    wcount = 0
    for fp in sorted(DOCS_DIR.rglob('*')):
        if not fp.is_file() or fp.suffix.lower() != '.webp':
            continue
        old_s, new_s = optimize_webp(fp)
        total_old += old_s
        total_new += new_s
        wcount += 1
        if new_s < old_s:
            print(f"  {fp.relative_to(DOCS_DIR.parent)}: {old_s//1024}K -> {new_s//1024}K")
    print(f"  Processed {wcount} WebP files\n")

    print("=== Minifying SVG ===")
    scount = 0
    for fp in sorted(DOCS_DIR.rglob('*')):
        if not fp.is_file() or fp.suffix.lower() != '.svg':
            continue
        if minify_svg(fp):
            scount += 1
    print(f"  Minified {scount} SVG files\n")

    print("=== Updating references ===")
    rcount = 0
    for fp in sorted(DOCS_DIR.rglob('*')):
        if not fp.is_file() or fp.suffix.lower() not in {'.md', '.yml', '.yaml', '.js'}:
            continue
        if update_refs_in_file(fp):
            rcount += 1
    print(f"  Updated {rcount} files\n")

    if total_old > 0:
        saved = total_old - total_new
        pct = saved / total_old * 100
        print(f"=== Summary ===")
        print(f"  Before: {total_old//1024//1024} MB ({total_old//1024} KB)")
        print(f"  After:  {total_new//1024//1024} MB ({total_new//1024} KB)")
        print(f"  Saved:  {saved//1024//1024} MB ({saved//1024} KB) — {pct:.1f}%")
    else:
        print("No raster images to optimize.")


if __name__ == '__main__':
    main()
