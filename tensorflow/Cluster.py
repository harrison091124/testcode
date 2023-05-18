# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

x_s = np.array(
    [[3.7, 1.5], [1, 2], [2.4, 3.1], [3, 4], [2, 1], [1, 1], [3, 4], [7, 8], [9, 10], [8, 6], [9, 8], [11, 8]],
    np.float)

plt.plot(x_s[:, 0], x_s[:, 1], 'x')
plt.show()

model = keras.Sequential([
    keras.layers.Dense(4, input_shape=(2,), activation='relu'),
    keras.layers.Dense(2)
])

model.compile()
