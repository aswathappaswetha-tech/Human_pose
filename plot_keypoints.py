import sys
import csv
import argparse
from pathlib import Path

def read_csv(path):
    pts = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                x = float(row.get('x', '').strip())
                y = float(row.get('y', '').strip())
            except Exception:
                continue
            pts.append((x, y))
    return pts

def main():
    p = argparse.ArgumentParser(description='Overlay keypoints on an image')
    p.add_argument('--csv', default='keypoints_output.csv')
    p.add_argument('--image', default='test_images/human6.avif')
    p.add_argument('--out', default='output_keypoints.png')
    args = p.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        print('CSV not found:', csv_path)
        sys.exit(1)

    pts = read_csv(csv_path)
    if not pts:
        print('No points found in', csv_path)
        sys.exit(1)

    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception as e:
        print('Pillow is required. Install with: pip install pillow pillow-avif-plugin')
        raise

    img_path = Path(args.image)
    if not img_path.exists():
        print('Image not found:', img_path)
        sys.exit(1)

    try:
        im = Image.open(img_path).convert('RGB')
    except Exception as e:
        print('PIL could not open image directly, trying imageio fallback:', e)
        try:
            import imageio
            arr = imageio.v3.imread(str(img_path))
            im = Image.fromarray(arr)
        except Exception as e2:
            print('Fallback read failed:', e2)
            raise

    draw = ImageDraw.Draw(im)
    r = max(3, int(round(min(im.size) * 0.01)))
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None

    for i, (x, y) in enumerate(pts):
        x0, y0 = float(x), float(y)
        bbox = [x0 - r, y0 - r, x0 + r, y0 + r]
        draw.ellipse(bbox, outline='red', width=2)
        label_pos = (x0 + r + 2, y0 - r - 2)
        draw.text(label_pos, str(i), fill='yellow', font=font)

    out_path = Path(args.out)
    im.save(out_path)
    print('Saved overlay image to', out_path)

if __name__ == '__main__':
    main()
