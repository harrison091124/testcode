import matplotlib.pyplot as plt
import tensorflow as tf
import math
import cv2 as cv
import numpy as np
from tensorflow import keras

model = keras.Sequential(keras.layers.Dense(units=30, input_shape=(2,), activation=tf.keras.activations.relu))
model.add(keras.layers.Dense(units=2, activation=tf.keras.activations.softmax))

t_x = np.array([[33, 55], [20, 33], [38, 37], [46, 6], [9, 33], [25, 11], [99, 5], [53, 24], [62, 12]], np.float)
l_y = np.array([f[0] * 2 + f[1] * 3 - 30 for f in t_x], np.float)


model = keras.Sequential(keras.layers.Dense(units=3, input_shape=(2, )))
model.add(keras.layers.Dense(units=1))


model.compile(optimizer='rmsprop', loss='MSE')

model.fit(t_x, l_y, epochs=1000)

