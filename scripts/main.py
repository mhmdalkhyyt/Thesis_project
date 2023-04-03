import subprocess
import glob
import cv2
import numpy as np


#blur pictures
clear_path = "./clear_drone/*"
clear_files = glob.glob(clear_path)
size_of_clear_files = len(clear_files)
i = 0
while(i < size_of_clear_files):
    subprocess.run(f"python ./blur/python_cli_image_editor/editor.py filter --input {clear_files[i]} --output ./lurred_imgs --blur 4")
    print(f"bluring image {clear_files[i]}")
    i = i+1
    


#run obj detection on blurred images
blurred_path = "./lurred_imgs/*"
blurred_files = glob.glob(blurred_path)
size_of_blurred_files = len(blurred_files)
i = 0
while(i < size_of_blurred_files):
    subprocess.run(f"python ./obj_detect.py {blurred_files[i]}")
    print(f"running debluring on blur image {blurred_files[i]}")
    i = i+1

print("done")