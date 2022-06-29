from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Agreement comparison
    """

    include_results_in_report: bool = False
