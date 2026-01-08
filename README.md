# pose_human

Light-weight repo for training and running YOLOv8 pose models on a small CVAT-exported dataset.

Quick start

- Create and activate a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

- Train the model:

```powershell
python train_pose.py
```

- Run inference with the latest weights:

```powershell
python test_pose.py
```

- Save annotated images and per-image keypoint CSVs:

```powershell
python scripts\save_predictions_to_workspace.py
```

Files and folders

- `cocopose.yaml`, `data.yaml` — dataset and model config (currently using 15 keypoints)
- `images/`, `labels/` — training/validation data
- `train_pose.py`, `test_pose.py` — training and inference entrypoints
- `scripts/convert_labels_17_to_15.py` — utility used to convert 17→15 keypoints (backups saved as `.bak`)
- `predictions/` — generated annotated images and per-image keypoint CSVs

Notes

- Backups: converted label files keep a `.bak` copy of the original 17-keypoint labels.
- To switch back to 17 keypoints, restore backups and set `kpt_shape: [17, 3]` in `data.yaml` and `cocopose.yaml`.

Where outputs are saved

- Training outputs (example path): `C:/Users/Swetha/runs/pose/pose_human_run*/weights/best.pt`
- Predictions: `predictions/` in project root

Want help with branch protection or a longer README (badges, license, contributor guide)? Tell me which and I can set it up.

