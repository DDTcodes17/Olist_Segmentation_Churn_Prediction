import os
from src.constants import common_constants
from dataclasses import dataclass

@dataclass
class IngestionArtifact:
    train_file: str
    test_file:str