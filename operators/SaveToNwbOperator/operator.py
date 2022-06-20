from flowuipackage.base_operator import BaseOperator
from .model import OperatorModel


class SaveToNwbOperator(BaseOperator):
    
    __name__ = "SaveToNwbOperator"
    __version__ = "0.1.0"
    __dockerfile__ = "Dockerfile-base"
    __operator_model__ = OperatorModel


    def operator_function(self, operator_model: OperatorModel):
        return None


    def generate_report(self, rec, recording_lfp):
        return None