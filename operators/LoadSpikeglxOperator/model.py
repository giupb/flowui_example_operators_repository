from pydantic import BaseModel, Field
from enum import Enum


class StreamIdType(str, Enum):
    """
    Stream type, defines whether the data comes from lfp or raw signal
    """
    ap = 'ap'
    lf = 'lf'


class OperatorModel(BaseModel):
    """
    Load SpikeGLX dataset from S3
    """

    bucket_name: str = Field(
        default='catalystneuro',
        description='this is the name of the bucket'
    )
    dataset_path: str = Field(
        default='spikeglx',
        description='this is the path for the dataset'
    )
    stream_id: StreamIdType = 'ap'
    include_results_in_report: bool = True
