import os

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Skrypt dokonujący transformacji na plikach datasetu.

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

def expansion(name):
    path = name + '.png'
    img = cv2.imread(path)   #Load the image file into memory
    #read -----------------------------------------------------
    img2 = cv2.flip(img,1)
    cv2.imwrite(name +'_flp.png',img2)
    #flipping horizontally ------------------------------------
    img_rot_1 = rotateImage(img,10)
    cv2.imwrite(name +'_rot10.png',img_rot_1)
    img_rot_2= rotateImage(img,20)
    cv2.imwrite(name +'_rot20.png',img_rot_2)
    img_rot_3= rotateImage(img,30)
    cv2.imwrite(name +'_rot30.png',img_rot_3)
    img_rot_4= rotateImage(img,40)
    cv2.imwrite(name +'_rot40.png',img_rot_4)
    img_rot_5= rotateImage(img,50)
    cv2.imwrite(name +'_rot50.png',img_rot_5)
    img_rot_6= rotateImage(img,60)
    cv2.imwrite(name +'_rot60.png',img_rot_6)
    #rotating regular clockwise ----------------------------------
    img_rot_7= rotateImage(img,350)
    cv2.imwrite(name +'_rot-10.png',img_rot_7)
    img_rot_8= rotateImage(img,340)
    cv2.imwrite(name +'_rot-20.png',img_rot_8)
    img_rot_9= rotateImage(img,330)
    cv2.imwrite(name +'_rot-30.png',img_rot_9)
    img_rot_10= rotateImage(img,320)
    cv2.imwrite(name +'_rot-40.png',img_rot_10)
    img_rot_11= rotateImage(img,310)
    cv2.imwrite(name +'_rot-50.png',img_rot_11)
    img_rot_12= rotateImage(img,300)
    cv2.imwrite(name +'_rot-60.png',img_rot_12)
    #rotating regular anticlockwise ---------------------------
    img_flp_rot_1 = rotateImage(img,10)
    cv2.imwrite(name +'_flp_rot10.png',img_flp_rot_1)
    img_flp_rot_2 = rotateImage(img2,20)
    cv2.imwrite(name +'_flp_rot20.png',img_flp_rot_2)
    img_flp_rot_3 = rotateImage(img2,30)
    cv2.imwrite(name +'_flp_rot30.png',img_flp_rot_3)
    img_flp_rot_4 = rotateImage(img2,40)
    cv2.imwrite(name +'_flp_rot40.png',img_flp_rot_4)
    img_flp_rot_5 = rotateImage(img2,50)
    cv2.imwrite(name +'_flp_rot50.png',img_flp_rot_5)
    img_flp_rot_6 = rotateImage(img2,60)
    cv2.imwrite(name +'_flp_rot60.png',img_flp_rot_6)
    #rotating flipped clockwise --------------------------------------
    img_flp_rot_7 = rotateImage(img,350)
    cv2.imwrite(name +'_flp_rot-10.png',img_flp_rot_7)
    img_flp_rot_8 = rotateImage(img2,340)
    cv2.imwrite(name +'_flp_rot-20.png',img_flp_rot_8)
    img_flp_rot_9 = rotateImage(img2,330)
    cv2.imwrite(name +'_flp_rot-30.png',img_flp_rot_9)
    img_flp_rot_10 = rotateImage(img2,320)
    cv2.imwrite(name +'_flp_rot-40.png',img_flp_rot_10)
    img_flp_rot_11 = rotateImage(img2,310)
    cv2.imwrite(name +'_flp_rot-50.png',img_flp_rot_11)
    img_flp_rot_12 = rotateImage(img2,300)
    cv2.imwrite(name +'_flp_rot-60.png',img_flp_rot_12)
    #rotating flipped anticlockwise ----------------------------

the_path = input("Wpisz ścieżkę folderu z obrazami: ")
os.chdir(the_path)
root_name = input("Wpisz nazwę bez uwzględnienia liczb porządkowych: ")
n = int(input("Wpisz zakres datasetu(ostatni wyraz): "))
for x in range(1, n + 1):
    expansion(root_name + str(x))    
    
    
# changing image vector 
for dir in os.path.join("./images"):
    for image_here in os.path.join("dir"+"image_here"):
        cv2.imwrite(image_here + "_vector.png", image)
        
    
