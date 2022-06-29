from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Toy Dataset
    """

    dataset_id: str = Field(
        default="toy_dataset", 
        description='Dataset unique ID'
    )
    duration: float = Field(
        default=10.,
        description='duration in seconds',
        gt=0.
    )
    num_channels: int = Field(
        default=4,
        description='number of channels',
        gt=0
    )
    num_units: int = Field(
        default=10,
        description='number of units',
        gt=0
    )
    sampling_frequency: float = Field(
        default=30000.,
        description='Sampling frequency in Hz',
        gt=0.
    )
    average_peak_amplitude: float = Field(
        default=-100., 
        description='Average peak amplitude',
    )
    upsample_factor: int = Field(
        default=13, 
        description='upsample factor',
        gt=0
    )
    contact_spacing_um: float = 40., 
    num_columns: int = 1, 
    seed: int = 0,
    include_results_in_report: bool = False