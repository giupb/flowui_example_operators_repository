from flowuipackage.utils.base_node_style import get_frontend_node_style


node_style = get_frontend_node_style(
    module_name="LoadDataFromS3Operator",
    node_label="Load Data from S3",
    target_position="null",
    node_style=dict(
        backgroundColor="#b3cde8"
    ),
    icon_class_name="fas fa-database"
)