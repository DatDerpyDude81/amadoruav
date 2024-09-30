from ultralytics import YOLO
#load classifier model
model = YOLO("yolov8n-cls.yaml",task="classify")
#train for 100 epochs
#100 epochs took me around 6 hours to train
reuslts = model.train(data="/Users/matthewyang/amadoruav/pt2/data", model="yolov8n-cls.yaml",epochs=100)
