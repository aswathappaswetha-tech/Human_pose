import os

# Workaround Windows OpenMP runtime conflict (libiomp5md.dll)
# Set before importing heavy libs to avoid OMP: Error #15
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
os.environ.setdefault("OMP_NUM_THREADS", "1")

from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")  # or yolov11n-pose.pt if you're using YOLOv11

model.train(
   data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="pose_human_run"
)
