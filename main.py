import subprocess
import glob
import cv2
import numpy as np


#blur pictures
clear_path = "C:\\Users\\TheGreatOne\\Examens_arbetet\\Yolo_test\\YOLOv8_working\\clear_drone\\*"
clear_files = glob.glob(clear_path)
size_of_clear_files = len(clear_files)
i = 0
while(i < size_of_clear_files):
    subprocess.run(f"python ./blur/python_cli_image_editor/editor.py filter --input {clear_files[i]} --output ./lurred_imgs --blur 4")

    i = i+1


#run obj detection on blurred images
blurred_path = "C:\\Users\\TheGreatOne\\Examens_arbetet\\Yolo_test\\YOLOv8_working\\lurred_imgs\\*"
blurred_files = glob.glob(blurred_path)
size_of_blurred_files = len(blurred_files)
i = 0
while(i < size_of_blurred_files):
    subprocess.run(f"python ./obj_detect.py {blurred_files[i]}")
    i = i+1




