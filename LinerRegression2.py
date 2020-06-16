import matplotlib.pyplot as plt
import tensorflow as tf
import math
import cv2 as cv

model = keras.Sequential(keras.layers.Dense(units=30, input_shape=(2, ), activation=tf.keras.activations.relu))
model.add(keras.layers.Dense(units=2, activation=tf.keras.activations.softmax))

t_x = np.array([[33, 55], [20, 33], [38, 37], [46, 6], [9, 33], [25, 11], [99, 5], [53, 24], [62, 12]], np.float)
l_y = np.array([1, 1, 1, 0, 0, 0, 0, 1, 1], np.int)