import os
from roboflow import Roboflow

ROBOKEY = os.getenv("ROBO_API_KEY")

#Validate API LOGIN
robo = Roboflow(api_key=ROBOKEY)

#Define data repo we point at
workspace = robo.workspace("lying-glihm")
dataset = robo.project("lying-in-bed").version(4).download("yolov8")

ymalPath = os.path.join(dataset.location, "model_data.yaml")

print(f"DS downloaded to: {ymalPath}")
