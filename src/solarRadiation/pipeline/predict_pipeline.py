import pandas as pd
import sys
import pickle
from solarRadiation.logging import logger
class PredictPipeline():
    def __init__(self) -> None:
        pass

    def predict (self,features):
        try:
            model = pickle.load(open('artifacts/model_trainer/model.pkl','rb'))
            transformer = pickle.load(open('artifacts/data_transformation/transformer.pkl','rb'))
            transformed_data = transformer.transform(features)
            prediction = model.predict(transformed_data)
            return prediction
        except Exception as e:
            raise e
        

class CustomData():
    def __init__ (self, Clearsky_DHI:float, Clearsky_GHI:float,SolarZenithAngle:float):
        self.Clearsky_DHI = Clearsky_DHI
        self.Clearsky_GHI = Clearsky_GHI
        self.SolarZenithAngle = SolarZenithAngle

    def get_data_as_frame(self):
        try:
            custom_input_data_dict = {
                'Clearsky DHI' : [self.Clearsky_DHI],
                'Clearsky GHI' : [self.Clearsky_GHI],
                'Solar Zenith Angle' : [self.SolarZenithAngle]
            }
            return pd.DataFrame(custom_input_data_dict)
        except Exception as e:
            raise e