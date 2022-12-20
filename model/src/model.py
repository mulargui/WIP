#constants
import constants

#avoid TF INFO messages about internal optimizations (This TensorFlow binary is optimized with ...)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

class Model:

    #constructor
    def __init__(self):
        #here is the NN model
        self.model = Sequential()
        self.model.add(Dense(units = constants.NUM_FEATURES * 2/3, activation = 'relu', kernel_initializer = 'normal', input_dim = constants.NUM_FEATURES))
        self.model.add(Dense(units = constants.NUM_CLASSES, activation = 'softmax'))
        self.model.compile(loss = keras.losses.categorical_crossentropy,
            optimizer = 'Adam',
            metrics = ['accuracy'])

    #train the model
    def train(self, x_train, y_train, x_test, y_test, epochs):
        self.model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs = epochs)
    
    #save the model
    #sagemaker requires to have the model stored under a numeric folder. temporary hack
    def save(self, model_dir):
        self.model.save(os.path.join(model_dir, "0001"))

    #import a model
    def load(self, model_dir):
        self.model = tf.keras.models.load_model(os.path.join(model_dir, "0001"))
