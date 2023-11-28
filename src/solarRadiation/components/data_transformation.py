import pandas as pd
import os
from solarRadiation.utils.common import create_directories
from sklearn.preprocessing import StandardScaler
from solarRadiation.entity import DataTransformationConfig
from solarRadiation.logging import logger


class DataTransformation:
    def __init__(self, config = DataTransformationConfig):
        self.config = config
        self.transformer = StandardScaler()
        self.target = "Clearsky DNI"

    def transform_data(self):
        train = pd.read_csv(self.config.train_data_path)
        test = pd.read_csv(self.config.test_data_path)
        validation = pd.read_csv(self.config.validation_data_path)

        tr_data = train.drop(["Clearsky DNI","Timestamp"], axis=1)

        col_list = list(tr_data.columns)

        high_correlation = []
        low_correlation = []
        for col in col_list:
            if (train[col].corr(train[self.target]) > 0.50) or (train[col].corr(train[self.target]) < -0.50):
                high_correlation.append(col)
            else:
                low_correlation.append(col)

        x_train = train.loc[:,high_correlation]
        x_test = test.loc[:, high_correlation]
        x_val = validation.loc[:, high_correlation]
        y_train = train[self.target]
        y_val = validation[self.target]
        
        logger.info("Data transformation started")
        X_train = self.transformer.fit_transform(x_train)
        X_test = self.transformer.transform(x_test)
        X_val = self.transformer.transform(x_val)

        logger.info("Data transformation completed")
        create_directories([self.config.transformed_data_path])

        X_train.dump(os.path.join(self.config.transformed_data_path,'x_train.pkl'))
        X_test.dump(os.path.join(self.config.transformed_data_path,'x_test.pkl'))
        X_val.dump(os.path.join(self.config.transformed_data_path,'x_validation.pkl'))
        y_train.to_pickle(os.path.join(self.config.transformed_data_path,'y_train.pkl'))
        y_val.to_pickle(os.path.join(self.config.transformed_data_path,'y_validation.pkl'))
        logger.info("Transformed data saved to the transformed data path")

