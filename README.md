# pose_human

This project trains and tests a YOLOv8 pose model on a CVAT-exported dataset.

Contents
- `cocopose.yaml`, `data.yaml` - dataset configs (now set to 15 keypoints)
- `labels/` - YOLO-format pose labels (originals backed up as `.bak` when converted)
- `images/` - training/validation images
- `train_pose.py` - training entrypoint
- `test_pose.py` - simple inference script
- `scripts/convert_labels_17_to_15.py` - utility that converted 17→15 keypoints (created backups `.bak`)
- `scripts/save_predictions_to_workspace.py` - runs model on `test_images/`, saves annotated images and per-image CSVs to `predictions/`
- `predictions/` - generated annotated images and per-image keypoint CSVs (created by the script)
- `keypoints_output.csv` - example CSV from `test_pose.py`

Quick start

1) Create and activate the virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2) (Optional) Convert labels from 17 → 15 keypoints (a conversion was already run; backups available as `.bak`):

```powershell
python scripts\convert_labels_17_to_15.py
```

3) Train the model (example uses CPU/training config in `train_pose.py`):

```powershell
python train_pose.py
```

4) Run inference using the latest weights (test script points to the run weights created during training):

```powershell
python test_pose.py
```

5) To save annotated prediction images and per-image keypoint CSVs:

```powershell
python scripts\save_predictions_to_workspace.py
```

Notes and next steps
- The project currently uses `kpt_shape: [15, 3]`. If you want a different 15-keypoint ordering (CVAT's custom labels), provide the mapping (index → label) and I can remap labels accordingly.
- Backups: any label file converted has a `.bak` alongside it containing the original 17-keypoint content.
- If you prefer to restore original 17-keypoint behaviour, restore the backups and set `kpt_shape: [17, 3]` in `data.yaml` and `cocopose.yaml`.
- `train_pose.py` contains an environment workaround for Windows OpenMP (`KMP_DUPLICATE_LIB_OK`) to avoid libiomp conflicts; leave it as-is on Windows.

Where outputs are saved
- Training outputs: `C:/Users/Swetha/runs/pose/pose_human_run*/weights/best.pt`
- Predictions (annotated images + CSVs): `predictions/` in project root
- Example CSV: `keypoints_output.csv`

If you'd like, I can now:
- remap keypoints to an exact CVAT 15-point order (if you provide it), or
- restore the dataset to 17 keypoints and re-run training.

