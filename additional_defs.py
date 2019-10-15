"""
A file for functions that are not AI or CV functions. Only additional functions.
DO NOT input here important classes and functions, put them into main.py

Made by: Konrad Kihan-Wąsik and Mateusz Krzyżostanek    ZSL GDANSK
"""
import winsound
import os


def error_sound(duration=250, frequency=3000):
    winsound.Beep(frequency, duration)


def success_sound(duration=250, frequency=150):
    winsound.Beep(frequency, duration)


def making_paths(training_path="./Intel IA4Y/img/images_train", testing_path="./Intel IA4Y/img/images_test"):  # just
    # for making paths for training purposes
    if not os.path.exists(training_path):
        os.makedirs(training_path)

    if not os.path.exists(testing_path):
        os.makedirs(testing_path)