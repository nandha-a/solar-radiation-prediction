from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pickle
from solarRadiation.logging import logger
import numpy as np
import pandas as pd
from solarRadiation.entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config=ModelEvaluationConfig):
        self.config = config

    def evaluate(self):
        model = pickle.load(open(self.config.trained_model_path,'rb'))
        x_val = pickle.load(open(self.config.val_feature_path,'rb'))
        y_val = pickle.load(open(self.config.val_target_path,'rb'))

        prediction = model.predict(x_val)

        model_score = r2_score(y_val, prediction)
        absolute_error = mean_absolute_error(y_val, prediction)
        squared_error = mean_squared_error(y_val, prediction)
        root_squared_error = np.sqrt(mean_squared_error(y_val, prediction))
        logger.info("Model evaluated successfully")

        metrics_dict = {'Score': [model_score],'MAE':[absolute_error],'MSE':[squared_error],'RMSE':[root_squared_error]}

        df = pd.DataFrame.from_dict(metrics_dict)
        
        df.to_csv(self.config.metric_file_name, index=False)
        logger.info(f"Metrics recorded and stored in {self.config.metric_file_name}")