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
    image = cv2.imread(clear_files[i])
    output = cv2.fastNlMeansDenoisingColored(image,None,7,7,7,21) 
    cv2.imwrite('./lurred_imgs/denoised' + str(i) + '.png', output)
    i = i+1


#run obj detection on blurred images
blurred_path = "C:\\Users\\TheGreatOne\\Examens_arbetet\\Yolo_test\\YOLOv8_working\\lurred_imgs\\*"
blurred_files = glob.glob(blurred_path)
size_of_blurred_files = len(blurred_files)
i = 0
while(i < size_of_blurred_files):
    subprocess.run(f"python ./obj_detect.py {blurred_files[i]}")
    i = i+1




