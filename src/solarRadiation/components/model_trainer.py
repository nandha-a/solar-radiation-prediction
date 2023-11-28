from sklearn.ensemble import RandomForestRegressor
import pickle
from solarRadiation.logging import logger
from solarRadiation.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config=ModelTrainerConfig):
        self.config = config
        self.model = RandomForestRegressor()

    def train(self):
        feature = pickle.load(open(self.config.feature_path,'rb'))
        target = pickle.load(open(self.config.target_path,'rb'))
        logger.info("Model training started")
        model = self.model.fit(feature, target)
        logger.info("Model trained successfully")
        pickle.dump(model, open(self.config.model_path,'wb'))
        logger.info("Model saved to the model path")