from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Save to NWB file
    """

    arg_1: str = Field(
        default='default_value',
        description='this is an argument'
    )
    arg_2: str = Field(
        default='value',
        description='this is another argument'
    )
    include_results_in_report: bool = False

    class Config:
        title = 'SaveToNwbOperator'