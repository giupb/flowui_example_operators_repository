from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Ironclust sorter
    """
    include_results_in_report: bool = False
