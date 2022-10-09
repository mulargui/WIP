import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
print(os.listdir("../input/"))
print(os.listdir("../working/"))
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#load data, I had an issue with the data and hacked the data into the kernel
#dftrain=pd.read_csv('/kaggle/input/train.csv')
#dftest=pd.read_csv('/kaggle/input/test.csv')
dftrain=pd.read_csv('/kaggle/input/learn-together/train.csv')
dftest=pd.read_csv('/kaggle/input/learn-together/test.csv')

#validate files - nans per feature
print(dftrain.isnull().sum(axis = 0))
print(dftest.isnull().sum(axis = 0))

#validate files - no rows with all zeros
print(dftrain[dftrain.drop(['Id','Cover_Type'], axis=1).eq(0).all(1)].empty)
print(dftest[dftest.drop('Id', axis=1).eq(0).all(1)].empty)

#split train data in features and labels
y = dftrain.Cover_Type
x = dftrain.drop(['Id','Cover_Type'], axis=1)

# split test data in features and Ids
Ids = dftest.Id
x_predict = dftest.drop('Id', axis=1)

#force all types to float
x = x.astype(float)
x_predict = x_predict.astype(float)

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
                                
x_predict['Elevation']=(x_predict['Elevation']-1859)/(3858-1859)                             
x_predict['Aspect']=x_predict['Aspect']/360                      
x_predict['Slope']=x_predict['Slope']/66                      
x_predict['Horizontal_Distance_To_Hydrology']=x_predict['Horizontal_Distance_To_Hydrology']/1397                      
x_predict['Vertical_Distance_To_Hydrology']=(x_predict['Vertical_Distance_To_Hydrology']+173)/(601+173)                             
x_predict['Horizontal_Distance_To_Roadways']=x_predict['Horizontal_Distance_To_Roadways']/7117                      
x_predict['Hillshade_9am']=x_predict['Hillshade_9am']/254                      
x_predict['Hillshade_Noon']=x_predict['Hillshade_Noon']/254                      
x_predict['Hillshade_3pm']=x_predict['Hillshade_3pm']/254                      
x_predict['Horizontal_Distance_To_Fire_Points']=x_predict['Horizontal_Distance_To_Fire_Points']/67173                      

#validate data - no rows with all zeros
#x.index[x.eq(0).all(1)]
print(x[x.eq(0).all(1)].empty)
print(x_predict[x_predict.eq(0).all(1)].empty)

# convert the label to One Hot Encoding
#to_categorical requires 0..6 instead of 1..7
y -=1
y = y.to_numpy()

num_classes = 7

from tensorflow.keras.utils import to_categorical
y = to_categorical(y, num_classes)

#convert the features dataframes to numpy arrays
x = x.to_numpy()
x_predict = x_predict.to_numpy()

#split in train (80%) and test (20%) sets 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2)

#here is the NN model
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

num_features = 54

model = Sequential()
model.add(Dense(units=num_features*2/3, activation='relu', kernel_initializer='normal', input_dim=num_features))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='Adam',
              metrics=['accuracy'])

#train the model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=250)

# Predict!!
y_predict = model.predict(x_predict)

for i in range(10):
	print(y_predict[i], np.argmax(y_predict[i])+1)