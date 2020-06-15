import numpy as np
from tensorflow import keras

model = keras.Sequential(keras.layers.Dense(units=1, input_shape=(1,)))

t_x = np.array([1.0, 2, 3, 4, 5, 6, 7, 8], np.float)
l_y = np.array([2 * x - 2 for x in t_x], np.float)

model.compile(optimizer='rmsprop', loss='mean_squared_error')

model.fit(t_x, l_y, batch_size=4, epochs=5000)
