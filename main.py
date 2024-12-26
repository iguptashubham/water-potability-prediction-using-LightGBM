from fastapi import FastAPI
import pandas as pd
from app.structure import water
from src.load_model import load_model

app = FastAPI(title='Water Potability Prediction')

@app.get('/')
def home():
    return {'home':'Water Potability Prediction'}

@app.post('/potability_test')
def potability_test(water:water):
    data = pd.DataFrame(
        {
            'ph':[water.ph],
            'Hardness':[water.Hardness],
            'Solids':[water.Solids],
            'Chloramines':[water.Chloramines],
            'Sulfate':[water.Sulfate],
            'Conductivity':[water.Conductivity],
            'Organic_carbon':[water.Organic_carbon],
            'Trihalomethanes':[water.Trihalomethanes],
            'Turbidity':[water.Turbidity]
        }
    )
    #make prediction
    pred = load_model(df=data)
    if pred ==1:
        return {1:'Water is Drinkable'}
    else:
        return {0:'Water is not Drinkable'}