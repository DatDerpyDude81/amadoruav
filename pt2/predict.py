from ultralytics import YOLO
import json
import numpy
#predict with model
model=YOLO("runs/classify/train3/weights/best.pt")
results=model("vision.png")
#format output
jsonoutput=results[0].to_json()
item=json.loads(jsonoutput)

with open("vision.out","x") as file:
    file.write(item[0]["name"])