from fastapi import FastAPI 
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


@app.post("/echo")
def predict(data: InputPayload):
    return {data}