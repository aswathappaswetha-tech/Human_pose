import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parents[1]
LABELS = ROOT / "labels"

def convert_file(path: pathlib.Path):
    text = path.read_text().strip()
    if not text:
        return False
    parts = text.split()
    # class + bbox(4) = 5 tokens
    if len(parts) < 5:
        return False
    kpt_tokens = parts[5:]
    if len(kpt_tokens) % 3 != 0:
        print(f"Skipping {path}: keypoints malformed")
        return False
    K = len(kpt_tokens) // 3
    if K == 15:
        return False
    if K != 17:
        print(f"Skipping {path}: unexpected keypoint count {K}")
        return False
    # keep first 15 keypoints
    new_kpt = kpt_tokens[:15*3]
    new_parts = parts[:5] + new_kpt
    # backup
    bak = path.with_suffix(path.suffix + '.bak')
    if not bak.exists():
        shutil.copy(path, bak)
    path.write_text(" ".join(new_parts) + "\n")
    return True

if __name__ == '__main__':
    changed = 0
    for sub in ("train", "val"):
        d = LABELS / sub
        if not d.exists():
            continue
        for f in d.glob("*.txt"):
            if convert_file(f):
                print(f"Converted {f}")
                changed += 1
    print(f"Done. Converted {changed} files.")
