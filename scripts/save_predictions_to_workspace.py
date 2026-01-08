from ultralytics import YOLO
import pathlib
import pandas as pd

MODEL_PATH = r"C:/Users/Swetha/runs/pose/pose_human_run12/weights/best.pt"
ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "predictions"
OUT.mkdir(exist_ok=True)

model = YOLO(MODEL_PATH)
results = model(str(ROOT / "test_images"), save=True, save_dir=str(OUT))

# Save keypoints per image
for i, r in enumerate(results):
    if hasattr(r, 'keypoints') and r.keypoints is not None:
        # r.keypoints.xy is [num_instances, K, 2]
        kpts_all = []
        for inst_idx in range(r.keypoints.xy.shape[0]):
            kpts = r.keypoints.xy[inst_idx].cpu().numpy()
            flat = kpts.reshape(-1, 2)
            df = pd.DataFrame(flat, columns=[f'x', f'y'])
            csv_path = OUT / f"{i}_instance{inst_idx}_keypoints.csv"
            df.to_csv(csv_path, index=False)
            kpts_all.append(str(csv_path))
        # write a small summary
        (OUT / f"{i}_summary.txt").write_text('\n'.join(kpts_all))

print('Saved annotated images and CSVs to', OUT)
