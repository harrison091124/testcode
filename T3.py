import numpy as np
from tensorflow import keras

model = keras.Sequential(keras.layers.Dense(units=1, input_shape=(None, 2)))

t_x = np.array([[1.0, 1.0], [2, 3], [3, 3], [4, 5], [5, 9], [6, 2], [7, 2], [8, 2]], np.float)
l_y = np.array([1, 1, 1, 0, 0, 0, 1, 1], np.int)


def comp():
    model.compile(optimizer='rmsprop', loss='mean_squared_error')


def fit():
    model.fit(t_x, l_y, batch_size=4, epochs=5000)
