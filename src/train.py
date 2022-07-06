import numpy as np
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd

from model_utils import build_logger, get_config, update_model


logger = build_logger(__name__)

logger.info("Loading full data...")
config = get_config()
data = pd.read_csv(config["path"]["full_data"])

logger.info("Building model...")
pipeline = Pipeline(
    [
        ("imputer", SimpleImputer(missing_values=np.nan, strategy="mean")),
        ("core_model", GradientBoostingRegressor()),
    ]
)

logger.info("Separating dataset into train and test...")
X = data.drop(["worldwide_gross"], axis=1)
y = data["worldwide_gross"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.35, random_state=config["random_state"]
)

logger.info("Setting hyperparameter to tune...")
param_tunning = {"core_model__n_estimators": [1, 5, 10] + list(range(20, 501, 20))}
grid_search = GridSearchCV(pipeline, param_grid=param_tunning, scoring="r2", cv=5)

logger.info("Starting grid search...")
grid_search.fit(X_train, y_train)

logger.info("Cross validating best model...")
final_result = cross_validate(
    grid_search.best_estimator_, X_train, y_train, return_train_score=True, cv=5
)

train_score = np.mean(final_result["train_score"])
test_score = np.mean(final_result["test_score"])
logger.info("Train score: {train_score}")
logger.info("Test score: {test_score}")

assert train_score > 0.7
assert test_score > 0.65

logger.info("Updating model...")
update_model(grid_search.best_estimator_)