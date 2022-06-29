from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Compute metrics
    """

    include_results_in_report: bool = False
