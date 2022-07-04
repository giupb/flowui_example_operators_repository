from flowuipackage.build_docker_images_operators import build_images_from_code_repository


operators_images_map = build_images_from_code_repository(
    code_repository=".",
    save_map_as_file=True
)