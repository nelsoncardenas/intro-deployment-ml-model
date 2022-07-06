import sys
import logging
from joblib import dump

from sklearn.pipeline import Pipeline
import yaml


def get_config():
    with open(r"config.yml") as file:
        config = yaml.safe_load(file)
    return config


def build_logger(name):
    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
        level=logging.INFO,
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )
    logger = logging.getLogger(name)
    return logger


def update_model(model: Pipeline) -> None:
    """Updates a model file.

    Args:
        model (Pipeline): a model to save.
    """
    config = get_config()
    dump(model, config["path"]["model"])
