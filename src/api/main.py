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

class UserInput(BaseModel):
    user_input: float

@app.get('/')
async def index():
    return {"Message": "Hello World"}

@app.post('/predict/')
async def predict(UserInput: UserInput):

    prediction = model.predict([UserInput.user_input])

    return {"prediction": float(prediction)}