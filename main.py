"""
Program made for Intel AI4Y project.
It recognizes pokemons like Pikachu via image.
Based on Intelb AI4Y project materials, some random stackoverflow solutions and own knowledge.
Put images ONLY in "images input folder"
Has an additional files for trashy functions and classes - additional_defs.py. DO NOT run WITHOUT second file in
same directory.
"images_train" - testing directory
Made by: Konrad Kihan-Wąsik and Mateusz Krzyżostanek    ZSL GDANSK

increase counter if edited code:
    TOTAL_HOURS WASTED_HERE = 5

Additional courses (REMOVE AFTER FINISHING A PROJECT):
https://towardsdatascience.com/train-image-recognition-ai-with-5-lines-of-code-8ed0bdd8d9ba
"""
import os
import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt
import matplotlib
from PIL import Image
import argparse

import additional_defs  # file module with custom and additional solutions

# creating "images_input" folder if not existing; IMPORTANT - creates a location where files are stored
additional_defs.making_paths()


def resizing_images(dir="./img/images_train/", dim=(200,200)):  # function resize and overwrite given images to 200x200px
    for img in os.listdir(dir):
        non_resized = Image.open(dir+img)
        resized_img = non_resized.resize(dim, Image.ANTIALIAS)
        resized_img.save(dir+img)


def resizing_test(dir="./img/images_test/", dim=(200,200)):
    for img in os.listdir(dir):
        non_resized = Image.open(dir+img)
        resized_img = non_resized.resize(dim, Image.ANTIALIAS)
        resized_img.save(dir+img)


def image_read(dir="./img/images_train/"):  # function reads user asked for
    try:
        given_img = input("Type image name you want to load. Specify image type. \n "
                          "IMAGE NAME: ")
        img = cv2.imread(dir+given_img)
        plt.imshow(img)
        plt.show()

    except TypeError:
        print("Oops! Something went wrong! Did you write correct file name?"
              " Remember to specify file type (ie. PNG/JPG)")
        additional_defs.error_sound()




image_read()
