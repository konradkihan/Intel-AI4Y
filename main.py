"""
Program made for Intel AI4Y project.
It recognizes pokemons like Pikachu via image.
Based on Intel AI4Y project materials, some random stackoverflow solutions and own knowledge.

Made by: Konrad Kihan-Wąsik and Mateusz Krzyżostanek    ZSL GDANSK 2019

increase counter if edited code:
    TOTAL_HOURS WASTED_HERE = a lot. very alot

USAGE: put folders with pokemons inside "images" folder. Pictures that we want to recognise must be put in the same
directory as "main.py" file
"""
import keras
import numpy as np
import os
import cv2
from tqdm import tqdm
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import random

# very important variables
images_path = "./images/"
label_cats = ["arcanine", "bulbasaur", "charmander", "fearow", "pikachu", "sandslash", "squirtle"]  # pokemon names
dim = 80
dataset = []


def dataset_compiler():
    for cat in label_cats:
        path = os.path.join(images_path,cat)
        class_index = label_cats.index(cat)
        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(path,img))
                actual_image = cv2.resize(img_array, (dim, dim))
                dataset.append([actual_image, class_index])
            except Exception:
                print()
                # basically this try and except thing is necessary and we have no idea why :c but only sometimes


dataset_compiler()

print("Size of dataset: ",len(dataset))


random.shuffle(dataset)

for sample in dataset[:10]:
    print(sample[1])

trainingX = []
labelsY = []

for features, label in dataset:
    trainingX.append(features)
    labelsY.append(label)

trainingX = np.array(trainingX).reshape(-1, dim, dim, 3)
trainingX = trainingX/255.0


def modeling():     # adds layers and models

    model = Sequential()

    model.add(Conv2D(256, (3, 3), input_shape=trainingX.shape[1:]))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(256, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Dense(7))
    model.add(Activation('sigmoid'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    labelsY_but_converted = keras.utils.to_categorical(labelsY, num_classes=7)
    model.fit(trainingX, labelsY_but_converted, batch_size=16, epochs=6, validation_split=0.2)
    return model


model = modeling()


def prepare(dir):
    dim = 80
    img_array = cv2.imread(dir)
    actual_image = cv2.resize(img_array, (dim, dim))
    return actual_image.reshape(-1, dim, dim, 3)


def calling_predictions():  # prints out a prediction
    prediction = model.predict([prepare('p1.jpg')])   # to change image we want to predict we have to change parameter here (default: 'sq30.jpg')
    print(label_cats[int(prediction[0][0])])


calling_predictions()
