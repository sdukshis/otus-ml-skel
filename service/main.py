"""FastAPI Titanic model inference example"""

import logging
from typing import Optional
import traceback
import sys

import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from titanic.models.serialize import load

app = FastAPI()


class Model:
    pipeline = None


class Passanger(BaseModel):
    Pclass: int
    Name: str
    Sex: str
    Age: Optional[int] = None
    SibSp: int
    Parch: int
    Ticket: str
    Fare: float
    Cabin: Optional[str] = None
    Embarked: Optional[str] = None


@app.on_event("startup")
def load_model():
    Model.pipeline = load("baseline.v1")


@app.get("/")
def read_healthcheck():
    return {"status": "Green"}


@app.post("/predict")
def predict(passenger_id: int, passanger: Passanger):
    df = pd.DataFrame([passanger.dict()])
    df.fillna(value=np.nan, inplace=True, downcast=False)
    try:
        pred = int(Model.pipeline.predict(df)[0])
    except Exception as e:
        traceback.print_exception(*sys.exc_info())
        raise HTTPException(status_code=400, detail=str(e))
    return {"passenger_id": passenger_id, "survived": pred}
