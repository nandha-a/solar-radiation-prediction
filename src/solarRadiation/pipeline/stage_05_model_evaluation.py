from solarRadiation.config.configuration import ConfigurationManager
from solarRadiation.components.model_evaluation import ModelEvaluation
from solarRadiation.logging import logger

STAGE_NAME = " Model Evaluation "

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()





if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e