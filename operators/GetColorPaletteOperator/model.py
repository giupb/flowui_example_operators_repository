from pydantic import BaseModel, Field
from enum import Enum


class PaletteModelType(str, Enum):
    default = "default"
    ui = "ui"
    makoto_shinaki = "makoto_shinkai"
    metroid_fusion = "metroid_fusion"
    akira_film = "akira_film"
    flower_photography = "flower_photography"


class OperatorModel(BaseModel):
    """
    Get color palette from image, using Colormind (http://colormind.io)
    """
    model: PaletteModelType = "default"
    include_results_in_report: bool = False
