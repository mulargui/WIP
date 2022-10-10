#avoid TF INFO messages about internal optimizations (This TensorFlow binary is optimized with ...)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import tensorflow as tf

from fastapi import FastAPI
from pydantic import BaseModel

import numpy as np

#import the model
model = tf.keras.models.load_model('/model-registry/model')

app = FastAPI()

class Request(BaseModel):
    Elevation = 0.0
    Aspect = 0.0
    Slope = 0.0
    Horizontal_Distance_To_Hydrology = 0.0
    Vertical_Distance_To_Hydrology = 0.0
    Horizontal_Distance_To_Roadways = 0.0
    Hillshade_9am = 0.0
    Hillshade_Noon = 0.0
    Hillshade_3pm = 0.0
    Horizontal_Distance_To_Fire_Points = 0.0
    Wilderness_Area1 = 0.0
    Wilderness_Area2 = 0.0
    Wilderness_Area3 = 0.0
    Wilderness_Area4 = 0.0
    Soil_Type1 = 0.0
    Soil_Type2 = 0.0
    Soil_Type3 = 0.0
    Soil_Type4 = 0.0
    Soil_Type5 = 0.0
    Soil_Type6 = 0.0
    Soil_Type7 = 0.0
    Soil_Type8 = 0.0
    Soil_Type9 = 0.0
    Soil_Type10 = 0.0
    Soil_Type11 = 0.0
    Soil_Type12 = 0.0
    Soil_Type13 = 0.0
    Soil_Type14 = 0.0
    Soil_Type15 = 0.0
    Soil_Type16 = 0.0
    Soil_Type17 = 0.0
    Soil_Type18 = 0.0
    Soil_Type19 = 0.0
    Soil_Type20 = 0.0
    Soil_Type21 = 0.0
    Soil_Type22 = 0.0
    Soil_Type23 = 0.0
    Soil_Type24 = 0.0
    Soil_Type25 = 0.0
    Soil_Type26 = 0.0
    Soil_Type27 = 0.0
    Soil_Type28 = 0.0
    Soil_Type29 = 0.0
    Soil_Type30 = 0.0
    Soil_Type31 = 0.0
    Soil_Type32 = 0.0
    Soil_Type33 = 0.0
    Soil_Type34 = 0.0
    Soil_Type35 = 0.0
    Soil_Type36 = 0.0
    Soil_Type37 = 0.0
    Soil_Type38 = 0.0
    Soil_Type39 = 0.0
    Soil_Type40 = 0.0

@app.get('/')
async def index():
    return {"Message": "Hello World!"}

@app.post('/predict/')
async def predict(request: Request):

    #convert input to a numpy array
    iterable  = (value for name, value in request)
    x = np.fromiter(iterable, float)
    print(x)
    print (x.shape)
 
    #prediction = model.predict(x)
    prediction = model(x, training=False)
    
    return {"prediction": str(prediction)}