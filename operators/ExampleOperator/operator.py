from email import message
from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel
import os


class ExampleOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # The BaseOperator class provides a set of convenience self variables ready to be used
        env_secret = os.environ.get('EXAMPLE_VAR', 'SECRET NOT FOUND!!')
        secret_msg = f"""
        Example Operator secret: {env_secret}
        """
        self.logger.info(secret_msg)

        msg = """
        #############################################################################
        #############################################################################\n
        Example Operator Successfully Completed!\n
        #############################################################################\n
        #############################################################################
        """
        self.logger.info(msg)

        return OutputModel(
            message="Task successfully completed!",
            output_arg_1="something else"
        )