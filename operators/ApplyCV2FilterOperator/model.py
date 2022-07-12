from pydantic import BaseModel, Field
from enum import Enum


class EffectType(str, Enum):
    random = "random"
    grayscale = "grayscale"
    bright = "bright"
    dark = "dark"
    sharp = "sharp"
    sepia = "sepia"
    pencil = "pencil"
    pencil_color = "pencil_color"
    hdr = "hdr"
    invert = "invert"
    summer = "summer"
    winter = "winter"


class OperatorModel(BaseModel):
    """
    Apply effect to image
    """

    effect: EffectType = Field(
        default='random',
        description='Effect to be applied'
    )