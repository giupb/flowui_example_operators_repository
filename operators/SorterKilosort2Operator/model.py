from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Kilosort 2 sorter
    """
    include_results_in_report: bool = False
