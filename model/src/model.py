#constants
NUM_FEATURES = 54
NUM_CLASSES = 7

import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

#avoid TF INFO messages about internal optimizations (This TensorFlow binary is optimized with ...)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

class Model:
    NUM_EPOCS = 75

    #constructor
    def __init__(self):
        #here is the NN model
        self.model = Sequential()
        self.model.add(Dense(units = NUM_FEATURES * 2/3, activation = 'relu', kernel_initializer = 'normal', input_dim = NUM_FEATURES))
        self.model.add(Dense(units = NUM_CLASSES, activation = 'softmax'))
        self.model.compile(loss = keras.losses.categorical_crossentropy,
            optimizer = 'Adam',
            metrics = ['accuracy'])

    #train the model
    def train(self, x_train, y_train, x_test, y_test):
        self.model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs = self.NUM_EPOCS)
    
    #save the model
    def save(self):
        self.model.save('/model-registry/model/')

