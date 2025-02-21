from fastapi import FastAPI 
import pickle
import numpy as np
app = FastAPI() 

from pydantic import BaseModel

class InputPayload(BaseModel):
    sepal_lenght: float
    sepal_width: float
    petal_lenght: float
    petal_width: float

@app.post("/echo")
def echo_data(data: InputPayload):
    return {"message": "Data received", "data": data}

# Load the trained model from the pickle file
model = pickle.load(open("API_Project_ML_Model.pkl", "rb"))

@app.post("/predict")
def predict(data: InputPayload):
    input = input.dict()
    prediction = model.predict([[input['sepal_lenght'], input['sepal_width'], input['petal_lenght'], input['petal_width']]])
    map_predict_to_label = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    return {"prediction": map_predict_to_label[prediction[0]]}