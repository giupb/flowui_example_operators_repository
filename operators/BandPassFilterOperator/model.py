from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Bandpass filter test commit
    """

    freq_min: float = Field(
        default=1.,
        description='minimum frequency - description',
        gt=0.
    )
    freq_max: float = Field(
        default=300.,
        description='maximum frequency',
        gt=0.
    )
    include_results_in_report: bool = False

    class Config:
        title = 'BandPassFilterOperator'
