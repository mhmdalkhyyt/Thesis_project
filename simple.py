from ultralytics import YOLO
import sys as sys
import cv2

def detect(img):
    # Load a model
    model = YOLO("yolov8n.pt")  # load an official model


    # Predict with the model
    results = model.predict(img)  # predict on an image
    #cv2.imwrite("img.jpg", img)
    cv2.imwrite('./clear_drone/img.jpg', results.boxes)


detect(sys.argv[1])