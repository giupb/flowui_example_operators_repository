from flowuipackage.base_operator import BaseOperator
from .model import OperatorModel


class SaveToNwbOperator(BaseOperator):

    def operator_function(self, operator_model: OperatorModel):
        return None