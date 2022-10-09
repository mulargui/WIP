#avoid TF INFO messages about internal optimizations (This TensorFlow binary is optimized with ...)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#load data
dftrain=pd.read_csv('/data/train.csv')

#split train data in features and labels
y = dftrain.Cover_Type
x = dftrain.drop(['Id','Cover_Type'], axis=1)

#force all types to float
x = x.astype(float)

#normalize features
#in the future it can be done more elegantly, for now just using the max min values of the data that we know
#x['Elevation']=(x['Elevation']-x['Elevation'].min())/(x['Elevation'].max()-x['Elevation'].min())                             
x['Elevation']=(x['Elevation']-1859)/(3858-1859)                             
x['Aspect']=x['Aspect']/360                      
x['Slope']=x['Slope']/66                      
x['Horizontal_Distance_To_Hydrology']=x['Horizontal_Distance_To_Hydrology']/1397                      
x['Vertical_Distance_To_Hydrology']=(x['Vertical_Distance_To_Hydrology']+173)/(601+173)                             
x['Horizontal_Distance_To_Roadways']=x['Horizontal_Distance_To_Roadways']/7117                      
x['Hillshade_9am']=x['Hillshade_9am']/254                      
x['Hillshade_Noon']=x['Hillshade_Noon']/254                      
x['Hillshade_3pm']=x['Hillshade_3pm']/254                      
x['Horizontal_Distance_To_Fire_Points']=x['Horizontal_Distance_To_Fire_Points']/67173                      

# convert the label to One Hot Encoding
#to_categorical requires 0..6 instead of 1..7
y -=1
y = y.to_numpy()

num_classes = 7

from tensorflow.keras.utils import to_categorical
y = to_categorical(y, num_classes)

#convert the features dataframes to numpy arrays
x = x.to_numpy()

#split in train (80%) and test (20%) sets 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2)

print (x_train.shape)
print (x_train[0])

import sys
sys.exit(0)

#here is the NN model
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

num_features = 54

model = Sequential()
model.add(Dense(units=num_features*2/3, activation='relu', kernel_initializer='normal', input_dim=num_features))
model.add(Dense(units=num_classes, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='Adam',
              metrics=['accuracy'])

#train the model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=75)

#save the model
model.save('/model-registry/model/')