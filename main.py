from solarRadiation.logging import logger
from solarRadiation.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from solarRadiation.pipeline.stage_02_data_validation import DataValidationPipeline
from solarRadiation.pipeline.stage_03_data_transformation import DataTransformationPipeline
from solarRadiation.pipeline.stage_04_model_trainer import ModelTrainerPipeline

STAGE_NAME = " Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = " Data Validation "

try:
    logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = " Data Transformation "

try:
    logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = " Model Trainer "

try:
    logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e