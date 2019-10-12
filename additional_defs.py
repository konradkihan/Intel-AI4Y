"""
A file for functions that are not AI or CV functions. Only additional functions.
DO NOT input here important classes and functions, put them into main.py

Made by: Konrad Kihan-Wąsik and Mateusz Krzyżostanek    ZSL GDANSK
"""
import winsound
def error_sound(duration=250, frequency=3000):
    winsound.Beep(frequency, duration)

def success_sound(duration=250, frequency=150):
    winsound.Beep(frequency, duration)

