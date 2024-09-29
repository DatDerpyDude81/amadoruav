from ultralytics import YOLO
model=YOLO("yolov8n.pt")
print(model.predict(source="pt2/training/images/ccircle1.jpg",conf=0.25))