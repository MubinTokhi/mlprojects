
from src.logger import logging
import sys
import pickle


from src.pipeline.predict_pipeline import CustomeData,PredictPipeline
from src.utils import load_object
from flask import Flask, request, render_template
import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler



app = Flask(__name__)

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomeData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df = data.get_data_as_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html',results = results[0])
    

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000, debug=True)
    
























"""
obj = DataIngestion()
train_data, test_data = obj.initiate_data_ingestion() 


data_transformation = DataTransformation()
train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

modeltrainer = ModelTrainer()
print(modeltrainer.initiate_model_trainer(train_arr,test_arr))

"""