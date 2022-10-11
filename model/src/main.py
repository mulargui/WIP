#constants
NUM_FEATURES = 54
NUM_CLASSES = 7
NUM_EPOCS = 75

#avoid TF INFO messages about internal optimizations (This TensorFlow binary is optimized with ...)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 



from data import Data
d = Data('/data/train.csv')
#d.data_validation()
d.data_engineering()
d.split(0.2)

#here is the NN model
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

model = Sequential()
model.add(Dense(units = NUM_FEATURES * 2/3, activation = 'relu', kernel_initializer = 'normal', input_dim = NUM_FEATURES))
model.add(Dense(units = NUM_CLASSES, activation = 'softmax'))
model.compile(loss = keras.losses.categorical_crossentropy,
              optimizer = 'Adam',
              metrics = ['accuracy'])

#train the model
model.fit(d.x_train, d.y_train, validation_data = (d.x_test, d.y_test), epochs = NUM_EPOCS)

#save the model
model.save('/model-registry/model/')