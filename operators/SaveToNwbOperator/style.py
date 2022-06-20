from flowuipackage.utils.base_node_style import get_frontend_node_style


node_style = get_frontend_node_style(
    module_name="SaveToNwbOperator",
    node_label="Save to NWB",
    source_position="null",
    node_style=dict(
        backgroundColor="#b9e8b3"
    ),
    icon_class_name="fas fa-file-export"
)