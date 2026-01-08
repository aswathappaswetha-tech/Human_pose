from ultralytics import YOLO

# Load your trained model
model = YOLO(r"C:/Users/Swetha/runs/pose/pose_human_run12/weights/best.pt")

# Run inference on a test image
results = model("test_images", save=True)

# Print keypoints for each detected person
for r in results:
    print(r.keypoints)

import pandas as pd

kpts = results[0].keypoints.xy[0].cpu().numpy()
df = pd.DataFrame(kpts, columns=["x", "y"])
df.to_csv("keypoints_output.csv", index=False)
