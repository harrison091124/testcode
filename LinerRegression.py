import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
import tensorflow as tf
import math
import cv2 as cv

model = keras.Sequential(keras.layers.Dense(units=20, input_shape=(None, 2), activation=tf.keras.activations.relu))
model.add(keras.layers.Dense(units=2, activation=tf.keras.activations.softmax))

t_x = np.array([[33, 55], [20, 33], [38, 37], [46, 6], [9, 33], [25, 11], [62, 5], [53, 24], [62, 12]], np.float)
l_y = np.array([1, 1, 1, 0, 0, 0, 0, 1, 1], np.int)


def plot_data(image, lst, label):
    b_list = np.array([list(lst[i]) for i in range(len(label)) if label[i] > 0])
    r_list = np.array([list(lst[i]) for i in range(len(label)) if label[i] <= 0])

    for item in b_list:
        cv.circle(image, tuple(item.astype(np.int)), 1, (255,0,0), 1)

    for item in r_list:
        cv.circle(image, tuple(item.astype(np.int)), 1, (0,0,255), 1)


def plot_square(img, w, h):
    for j in range(h):
            sample = np.array([[k, j] for k in range(w)], np.float)
            pred = model.predict(sample)
            for i in range(len(pred)):
                if np.argmax(pred[i]) == 1:
                    img[j,i] = (255, 255, 255)


def compile_model():
    model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy')


def fit():
    model.fit(t_x, l_y, epochs=4000)


def plot():
    w = math.ceil(np.max(t_x[:, 0]))+1
    h = math.ceil(np.max(t_x[:, 1]))+1
    img = np.zeros((h, w, 3),np.int)
    plot_square(img, w, h)
    plot_data(img, t_x, l_y)
    plt.imshow(img)
    plt.show()


def train():
    compile_model()
    fit()


if __name__ == '__main__':
    train()
    plot()
