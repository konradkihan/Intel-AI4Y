import os
import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt
import matplotlib

print("Modules active. Current OpenCV version "+cv2.__version__)

# size setting of resized photo of the object (width x height)
dim = (250, 250)


def image_read():
    non_resized_img = cv2.imread("image001.png")
    img = cv2.resize(non_resized_img, (dim), interpolation=cv2.INTER_AREA)
    plt.imshow(img)
    plt.show()

image_read()

# facial recognision algorithm by Intel

from opv import OpvModel

mymodel2 = OpvModel("face-detection-adas-0001", device="CPU", fp="FP32", ncs=1)
predictions = mymodel2.Predict(img)



def DrawBoundingBoxes(predictions, image, conf=0.5):
    canvas = image.copy()  # copy instead of modifying the original image
    predictions_1 = predictions[0][0]  # subset dataframe
    confidence = predictions_1[:, 2]  # getting conf value [image_id, label, conf, x_min, y_min, x_max, y_max]
    topresults = predictions_1[(confidence > conf)]  # choosing only predictions with conf value bigger than treshold
    (h, w) = canvas.shape[:2]  # setting the variable h and w according to image height

    #
    for detection in topresults:
        box = detection[3:7] * np.array([w, h, w, h])  # determine box location
        (xmin, ymin, xmax, ymax) = box.astype("int")  # assign box location value to xmin, ymin, xmax, ymax

        cv2.rectangle(canvas, (xmin, ymin), (xmax, ymax), (0, 0, 255), 4)  # make a rectangle
        cv2.putText(canvas, str(round(detection[2] * 100, 1)) + "%", (xmin, ymin),  # include text
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    cv2.putText(canvas, str(len(topresults)) + " face(s) detected", (50, 50),  # include text
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    return canvas


imshow_bgr(DrawBoundingBoxes(predictions, img), "Your picture")



"""sources to read
https://towardsdatascience.com/train-image-recognition-ai-with-5-lines-of-code-8ed0bdd8d9ba
"""