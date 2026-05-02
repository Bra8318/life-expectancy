from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
import pandas as pd
from model.predict import predict_data
from fastapi.middleware.cors import CORSMiddleware

app =FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return {'message': 'Welcome to the Life Expectancy API!'}

@app.post('/economic')
def Life_Expectancy_Predict(data:UserInput):
    user_input = {    
        'continent_code': data.continent_code,
        'country_status': data.get_status,
        'GDP' : data.GDP,
        'Income composition of resources' : data.Income_Composition_of_Resources,
        'Total expenditure' : data.Total_Expenditure
    }
    try:
        prediction = predict_data('Economic',user_input)
        return JSONResponse(status_code=200,content={'status': 'success', 'prediction': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'error', 'message': str(e)})
                            
@app.post('/health')
def health_predict(data:UserInput):
    user_input = {
        'continent_code' : data.continent_code,
        'Adult Mortality' : data.Adult_Mortality,
        'infant deaths' : data.Infant_Deaths,
        'BMI' : data.BMI,
        'HIV/AIDS' : data.HIV_AIDS,
        'Measles' : data.Measles,
        'under-five deaths' : data.Under_Five_Deaths
    }
    try:
        prediction = predict_data('Health',user_input)
        return JSONResponse(status_code=200,content={'status': 'success', 'prediction': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'error', 'message': str(e)})
    
@app.post('/immunity')
def immunity_predict(data:UserInput):
    user_input = {
        'continent_code' : data.continent_code,
        'Polio' : data.Polio,
        'Diphtheria' : data.Diphtheria,
        'Hepatitis B' : data.Hepatitis_B

    }
    try:
        prediction = predict_data('Immunization',user_input)
        return JSONResponse(status_code=200,content={'status': 'success', 'prediction': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'error', 'message': str(e)})
    
@app.post('/nutrition')
def nutrition_predict(data:UserInput):
    user_input = {
        'continent_code' : data.continent_code,
        'thinness  1-19 years' : data.Thinness_1_19_years,
        'thinness 5-9 years' : data.Thinness_5_9_years,
        'BMI' : data.BMI,
        'infant deaths' : data.Infant_Deaths,
        'under-five deaths' : data.Under_Five_Deaths
    }
    try:
        prediction = predict_data('Nutrition',user_input)
        return JSONResponse(status_code=200,content={'status': 'success', 'prediction': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={'status': 'error', 'message': str(e)})


    