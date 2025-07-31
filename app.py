from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_injestion import DataIngestion
from src.mlproject.components.data_injestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_injestion_config=DataIngestionConfig()
        data_injestion = DataIngestion()
        data_injestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)