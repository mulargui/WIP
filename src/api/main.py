#avoid TF INFO messages about internal optimizations (This TensorFlow binary is optimized with ...)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import tensorflow as tf

from fastapi import FastAPI
from pydantic import BaseModel

import numpy as np

#import the model
model = tf.keras.models.load_model('/model')

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

    print('Elevation: ', request.Elevation)
    print('Aspect: ', request.Aspect)
    print('Slope: ', request.Slope)
    print('Horizontal_Distance_To_Hydrology: ', request.Horizontal_Distance_To_Hydrology)

    #there needs to be a better way
    #x = tf.convert_to_tensor([
    x = np.array([
        request.Elevation,
        request.Aspect,
        request.Slope,
        request.Horizontal_Distance_To_Hydrology,
        request.Vertical_Distance_To_Hydrology,
        request.Horizontal_Distance_To_Roadways,
        request.Hillshade_9am,
        request.Hillshade_Noon,
        request.Hillshade_3pm,
        request.Horizontal_Distance_To_Fire_Points,
        request.Wilderness_Area1,
        request.Wilderness_Area2,
        request.Wilderness_Area3,
        request.Wilderness_Area4,
        request.Soil_Type1,
        request.Soil_Type2,
        request.Soil_Type3,
        request.Soil_Type4,
        request.Soil_Type5,
        request.Soil_Type6,
        request.Soil_Type7,
        request.Soil_Type8,
        request.Soil_Type9,
        request.Soil_Type10,
        request.Soil_Type11,
        request.Soil_Type12,
        request.Soil_Type13,
        request.Soil_Type14,
        request.Soil_Type15,
        request.Soil_Type16,
        request.Soil_Type17,
        request.Soil_Type18,
        request.Soil_Type19,
        request.Soil_Type20,
        request.Soil_Type21,
        request.Soil_Type22,
        request.Soil_Type23,
        request.Soil_Type24,
        request.Soil_Type25,
        request.Soil_Type26,
        request.Soil_Type27,
        request.Soil_Type28,
        request.Soil_Type29,
        request.Soil_Type30,
        request.Soil_Type31,
        request.Soil_Type32,
        request.Soil_Type33,
        request.Soil_Type34,
        request.Soil_Type35,
        request.Soil_Type36,
        request.Soil_Type37,
        request.Soil_Type38,
        request.Soil_Type39,
        request.Soil_Type40
        ], dtype=np.single)

    x1 = {name: tf.convert_to_tensor([value]) for name, value in request.items()}

    prediction = model.predict(x1)
    #prediction = model(x, training=False)
    
    return {"prediction": int(prediction)}