from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path
    unzip_dir : Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    train_data_path: str
    test_data_path: str
    validation_data_path: str
    transformed_data_path: Path
    transformer_path: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir : Path
    feature_path: str
    target_path: str
    model_path: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir : Path
    val_feature_path: str
    val_target_path: str
    trained_model_path: str
    metric_file_name: str