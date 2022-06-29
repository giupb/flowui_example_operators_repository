from pydantic import BaseModel, Field
from enum import Enum


class ReferenceOperatorType(str, Enum):
    average = 'average'
    median = 'median'


class OperatorModel(BaseModel):
    """
    Common reference filter
    """

    reference_operator: ReferenceOperatorType = 'average'
    include_results_in_report: bool = False