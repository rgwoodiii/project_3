# Put the code for your API here.
import numpy as np
import pandas as pd
import os
from fastapi import FastAPI
from typing import Union, List
from pydantic import BaseModel, Field
import uvicorn
from joblib import load
import os.path
import sys

# load model
model = load("/starter/model_building/trainedmodel.pkl")

# instantiate app with fastapi
app = FastAPI()

# allow heroku to pull data from dvc
if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")
    
# greeting
@app.get("/")
async def greet_user():
    return {"Welcome!"}


# greet with name
@app.get("/{name}")
async def get_name(name: str):
    return {f"Hi {name}, Welcome to this app"}


# predict
@app.post("/predict")
def predict(data1: ClassifierFeatureIn):
    data = pd.DataFrame.from_dict([data1.dict(by_alias=True)])
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)