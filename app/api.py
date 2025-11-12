from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
import numpy as np
import pandas as pd

app = FastAPI(title="Heart Disease Prediction API")

# Cargar modelo
model = load("notebooks/models/logistic_regression_final.joblib")

# Esquema de entrada
class InputData(BaseModel):
    edad: float
    sexo: int
    dolor_pecho: int
    presion_reposo: float
    colesterol: float
    azucar_ayunas: int
    ecg_reposo: int
    freq_cardiaca_max: float
    angina_ejercicio: int
    depresion_st: float
    pendiente_st: int
    vasos_coloreados: int
    talio: int

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])
    prob = model.predict_proba(df)[0, 1]
    pred = int(prob >= 0.5)
    return {
        "prediction": pred,
        "probability": round(float(prob), 4)
    }
