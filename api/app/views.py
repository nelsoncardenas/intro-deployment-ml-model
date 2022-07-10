from .data_models import PredictionRequest
from .app_utils import get_model, transform_to_dataframe


MODEL = get_model()


def get_prediction(request: PredictionRequest) -> str:
    data_to_predict = transform_to_dataframe(request)
    prediction = MODEL.predict(data_to_predict)[0]
    return '$ {:,.2f}'.format(max(0, prediction))
