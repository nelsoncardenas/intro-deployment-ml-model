import sys
import logging
from joblib import dump

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.pipeline import Pipeline
from string import Template
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


def save_simple_metrics_report(
    train_score: float, test_score: float, validation_score: float, model: Pipeline
) -> None:
    config = get_config()
    with open(config["path"]["report"], "w") as report_file:
        report_file.write("# Model Report\n\n")
        report_file.write("## Model Pipeline Description\n\n")
        for key, value in model.named_steps.items():
            report_file.write(f"* **{key}:** {value}\n")
        report_file.write("\n")
        report_file.write("## Metrics\n\n")
        report_template = Template(config["report_template"])
        report_updated = report_template.substitute(
            train_score=f"{train_score:.5f}",
            test_score=f"{test_score:.5f}",
            validation_score=f"{validation_score:.5f}",
        )
        report_file.write(r"{}".format(report_updated))


def get_model_performance(y_real: pd.Series, y_pred: pd.Series):
    config = get_config()
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(8)
    sns.regplot(x=y_pred, y=y_real, ax=ax)
    ax.set_xlabel("Predicted worldwide gross")
    ax.set_ylabel("Real world wide gross")
    ax.set_title("Behaviour of model performance")
    fig.savefig(config["path"]["image_behaviour"])
