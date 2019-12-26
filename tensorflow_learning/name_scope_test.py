import tensorflow as tf     # version: 2.0
from tensorflow import keras
from tensorflow.keras import layers


class ACNet:
    def __init__(self, scope):
        with tf.name_scope(scope):
            # tf.name_scope add a prefix on the variables,
            # but it don't work for keras.Sequential()
            self.A_net = keras.Sequential()
            self.A_net.add(layers.Input(shape=(4, )))
            self.A_net.add(layers.Dense(16, activation='relu', name='dense_1'))
            # Add another:
            self.A_net.add(layers.Dense(16, activation='relu', name='dense_2'))
            # Add a softmax layer with 10 output units:
            self.A_net.add(layers.Dense(10, activation='softmax', name='dense_3'))

if __name__=='__main__':
    acNet_1 = ACNet('first')
    acNet_2 = ACNet('second')
