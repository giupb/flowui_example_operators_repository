# flowui_example_project
A FlowUI project should be structured in the following way:
```
/containers
/operators
/workflows
```


# Operators
The `/operators` folder should contain your customized Operators. Each Operator should follow a standard organization and contain certain information to be able to be found and used by your deployed FlowUI instance. Example:
```
/operators
..../ExampleOperator
......../metadata.json    # REQUIRED
......../model.py         # REQUIRED
......../operator.py      # REQUIRED
```
<br>

### metadata.json
Contains a JSON object with metadata related to the Operator ans also optional style configurations for the UI node. Example:
```
{
    name: "ExampleOperator"
    version: "0.1.0"
    dockerfile: "Dockerfile_1",
    style: {**style_args}
}
```
<br>

### model.py
Contains the Pydantic model which defines the the input arguments types for the Operator. Example:
```
from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """Bandpass filter"""

    argument_1: float = Field(
        default=1.,
        description="an argument of numeric type",
    )
    argument_2: str = Field(
        default="default",
        description="an argument of string type"
    )
    argument_3: bool = False

    class Config:
        title = "ExampleOperator"
```
<br>

### operator.py
Contains the logic to run your custom code. The Operator you're writing comes here, and it should inherit from FlowUI `BaseOperator`. Example:
```
from flowui.base_operator import BaseOperator
from .model import OperatorModel


class ExampleOperator(BaseOperator):

    def operator_function(self, operator_model: OperatorModel):
        # Your custom function code comes here
```
<br>


# Workflows
The `/workflows` folder is the target place where your running FlowUI instance will store your customized Worflows. Example:
```
/worflows
..../custom_worflow_1.py
..../custom_worflow_2.py
..../...
```
<br>

# Containers
The `/containers` folder should contain all `requirements.txt` and `Dockerfile` files that will be used to define the dependencies and to build the containers that will run your custom code. Example:

```
/containers
..../Dockerfile_1
..../Dockerfile_2
..../requirements_1.txt
..../requirements_1.txt
```