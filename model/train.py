from ultralytics import YOLO

#Takes data path => trains yolo => returns weights
def train_model(data_yaml):

    #define model in use
    YOLOmodel = YOLO("yolo11n.pt")

    #define model training params
    weights = YOLOmodel.train(data=data_yaml, epochs=50, imgsz=640, batch=16, patience=10, name="lying_in_bed", device=0)

    savefolder = str(weights.save_dir) 
    best_weights_path = savefolder + "\\weights\\best.pt"
    return best_weights_path

if __name__ == "__main__":
    weights_best = train_model("lying-in-bed-4/data.yaml")  
    print(f"weights successfully saved to: {weights_best}")