# pose_human

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Light-weight repo for training and running YOLOv8 pose models on a small CVAT-exported dataset.

# 🧍‍♀️ Human Pose Estimation with YOLOv8

This project uses YOLOv8 for full-body human pose estimation on custom images. It includes label conversion, keypoint plotting, and model training workflows.

## 📁 Project Structure

- `scripts/`: preprocessing and label conversion scripts  
- `test_images/`: sample images for inference  
- `labels/`: training and validation label files  
- `train_pose.py`: training pipeline  
- `test_pose.py`: inference and visualization  
- `output_keypoints.png`: sample output  
- `data.yaml`, `cocopose.yaml`: dataset configuration  

## 🧠 Key Features

- Converts COCO-style labels to YOLOv8 format  
- Trains pose estimation model using Ultralytics YOLO  
- Visualizes keypoints and saves predictions  
- Supports `.jpg`, `.webp`, `.avif` test images  

## 🛠️ Setup

```bash
pip install -r requirements.txt


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


**License**

This project is provided under the MIT License — see `LICENSE` for details.

