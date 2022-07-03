from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Download Image from Picsum (https://picsum.photos/)
    """

    width_pixels: int = Field(
        default=200,
        description='Width in number of pixels',
        gt=10
    )
    height_pixels: int = Field(
        default=200,
        description='Height in number of pixels',
        gt=10
    )
    include_results_in_report: bool = False
