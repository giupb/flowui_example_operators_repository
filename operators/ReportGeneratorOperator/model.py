from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Generate report and save as PDF.
    """

    arg_1: str = Field(
        default='default_value',
        description='this is an argument'
    )
    arg_2: str = Field(
        default='value',
        description='this is another argument'
    )

    class Config:
        title = 'ReportGeneratorOperator'