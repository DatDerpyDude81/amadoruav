from ultralytics import YOLO
import json
import numpy
model=YOLO("runs/classify/train3/weights/best.pt")
results=model("vision.png")
jsonoutput=results[0].to_json()
item=json.loads(jsonoutput)

with open("vision.out","x") as file:
    file.write(item[0]["name"])