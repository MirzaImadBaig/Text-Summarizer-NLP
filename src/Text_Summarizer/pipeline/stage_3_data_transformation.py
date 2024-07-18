from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.conponents.data_transformation import DataTransformation
from src.Text_Summarizer.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()