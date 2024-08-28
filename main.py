from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import BaseModel
from data_model import Water

app = FastAPI(
    title="Water Potability Prediction",
    description="Predicting Water Potability"
)

with open(r"model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def index():
    return "Welcome to water Potability Prediction FastAPI"

@app.post("/predict")
def model_predict(water: Water):
    sample = pd.DataFrame({
        'ph' : [water.ph],
        'Hardness' : [water.Hardness],
        'Solids' :[water.Solids],
        'Chloramines' : [water.Chloramines],
        'Sulfate' : [water.Sulfate],
        'Conductivity' : [water.Conductivity],
        'Organic_carbon': [water.Organic_carbon],
        'Trihalomethanes': [water.Trihalomethanes],
        'Turbidity' : [water.Turbidity]
    })

    predictions = model.predict(sample)

    if predictions == 1:
        return "water is consumable"
    else:
        return "water is not consumable"
