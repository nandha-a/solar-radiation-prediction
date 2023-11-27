from solarRadiation.config.configuration import ConfigurationManager
from solarRadiation.components.data_validation import DataValidation
from solarRadiation.logging import logger

STAGE_NAME = " Data validation"


class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()






if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> statge {STAGE_NAME} started <<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e