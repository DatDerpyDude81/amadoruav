from ultralytics import YOLO
model = YOLO("yolov8n-cls.yaml",task="classify")
reuslts = model.train(data="/Users/matthewyang/amadoruav/pt2/data", model="yolov8n-cls.yaml",epochs=50)
