import yaml


def get_config():
    with open(r"config.yml") as file:
        config = yaml.safe_load(file)
    return config
