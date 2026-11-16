import cv2
from ultralytics import YOLO
import pygame
from datetime import datetime
from helperFunctions.lights import TurnOnLights

WEIGHTS = "runs/detect/lying_in_bed/weights/best.pt"
BOOM_SOUND_PATH = "media/boom.mp3"

CAM = 1

#model conf, inital set to 0.5 for regression testing
Confidence = .6

#opens webcam and applys YOLO model to all frames
def main(end_time):
    model = YOLO(WEIGHTS)
    pygame.mixer.init()
    boom_sound = pygame.mixer.Sound(BOOM_SOUND_PATH)

    #open the cam using windows DSHOW driver
    camera = cv2.VideoCapture(CAM, cv2.CAP_DSHOW)
    #cam failsafe
    if not camera.isOpened():
        raise MemoryError("Camera not opened")
        return

    #main model application loop
    #Frab frame by frame, then apply YOLO to seek a label
    cont = True
    while cont:
        if datetime.now() >= end_time:
            break
        OK, frame = camera.read()

        if not OK:
            print("shits wack")
            break
        #YOLO application and frame result grab
        results = model(frame, conf=Confidence, verbose=False)
        result = results[0]

        #Display boxes based off of the model frame responce
        boxes = result.boxes
        names = result.names
        annotation = result.plot()

        detection_count = 0
        #print model results
        for box in boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = names[class_id]    
            detection_count = detection_count + 1
            print(f"Detected: {class_name}\nCI: {(round(confidence, 2)*100)}%")

        #display on screen
        if detection_count > 0:
            status_text = "Laying"
        else:
            status_text = "n/a"
        if status_text == "Laying":
            if not pygame.mixer.get_busy():
                boom_sound.play()
        cv2.putText(annotation, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

        #show window
        cv2.imshow("UpOrElse", annotation)

        #cancelation
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()