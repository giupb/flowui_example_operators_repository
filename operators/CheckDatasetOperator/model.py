from pydantic import BaseModel


class OperatorModel(BaseModel):
    """
    Check Dataset
    """

    include_results_in_report: bool = False
