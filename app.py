from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from solarRadiation.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Route for homepage
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        data = CustomData(
            Clearsky_DHI= request.form.get('Clearsky DHI'),
            Clearsky_GHI=request.form.get('Clearsky GHI'),
            SolarZenithAngle=request.form.get('Solar Zenith Angle')
        )
        pred_df = data.get_data_as_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('main.html',results=results)
    

if __name__=="__main__":
    app.run(host="0.0.0.0") 