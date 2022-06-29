from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Mountainsort 4 sorter
    """
    include_results_in_report: bool = False
