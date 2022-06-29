from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Load Openephys dataset from S3
    """

    bucket_name: str = Field(
        default='catalystneuro',
        description='this is the name of the bucket'
    )
    dataset_path: str = Field(
        default='openephys',
        description='this is the path for the dataset'
    )
    include_results_in_report: bool = True
