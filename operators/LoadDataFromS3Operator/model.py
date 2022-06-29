from enum import Enum
from pydantic import BaseModel, Field


class DataFileType(str, Enum):
    """
    whether the data is stored in a CSV or JSON file.
    """
    csv = 'csv'
    json = 'json'


class OperatorModel(BaseModel):
    """
    Gets data from S3 path
    """

    bucket_name: str = Field(
        default='my-default-bucket',
        description='this is the name of the bucket'
    )
    dataset_path: str = Field(
        default='my-dataset',
        description='this is the path for the dataset'
    )
    data_file_type: DataFileType = "csv"
    include_results_in_report: bool = False