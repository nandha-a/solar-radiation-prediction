from solarRadiation.config.configuration import ConfigurationManager
from solarRadiation.components.data_transformation import DataTransformation
from solarRadiation.logging import logger

STAGE_NAME = " Data Transformation "


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.transform_data()





if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e