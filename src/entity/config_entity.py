import os
from datetime import datetime
from src.constants import common_constants

class TrainingConfig:
    def __init__(self,timestamp = datetime.now() ):
        self.timestamp = timestamp.strftime('%d_%m_%Y_%H_%M_%S')
        self.artifact_name = common_constants.ARTIFACT_FOLDER_NAME
        self.artifact_dir = os.path.join(self.artifact_name, self.timestamp)

class DataIngestionConfig:
    def __init__(self, training_config:TrainingConfig):
        self.ingestion_path = os.path.join(self.artifact_dir, common_constants.DATA_INGESTION_DIRECTORY)
        self.feature_store_path = os.path.join(self.ingestion_path, common_constants.FEATURE_STORE_DIRECTORY)
        self.ingested_path = os.path.join(self.ingestion_path, common_constants.INGESTED_DIRECTORY)
        self.train_file_path = os.path.join(self.ingested_path, common_constants.TRAIN_FILENAME)
        self.test_file_path = os.path.join(self.ingested_path, common_constants.TEST_FILENAME)
        self.train_test_split_ratio = common_constants.TRAIN_TEST_SPLIT_RATIO