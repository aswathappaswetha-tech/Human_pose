
🧍‍♂️ pose_human
https://opensource.org/licenses/MIT

A lightweight, clean, and reproducible repository for training and running YOLOv8 pose estimation models on a small CVAT‑exported dataset.
Includes label conversion utilities, training/inference scripts, and workspace‑ready prediction outputs.

🚀 Quick Start
1. Create and activate a virtual environment, then install dependencies
powershell:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
2. Train the model
powershell:
python train_pose.py
3. Run inference using the latest trained weights
powershell:
python test_pose.py
4. Save annotated images + per‑image keypoint CSVs
powershell:
python scripts\save_predictions_to_workspace.py
📁 Files & Folders Overview
cocopose.yaml, data.yaml — dataset + model configuration (currently using 15 keypoints)

images/, labels/ — training and validation data

train_pose.py, test_pose.py — training and inference entrypoints

scripts/convert_labels_17_to_15.py — converts COCO 17‑keypoint labels → YOLO 15‑keypoint format (creates .bak backups)

predictions/ — annotated images and keypoint CSV outputs

📝 Notes
Backup handling:  
When converting labels, the original 17‑keypoint files are preserved as .bak.

Switching back to 17 keypoints:  
Restore the .bak files and update:kpt_shape: [17, 3]
in both data.yaml and cocopose.yaml.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
yaml
kpt_shape: [17, 3]
in both data.yaml and cocopose.yaml.
