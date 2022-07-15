from fastapi import FastAPI
from mangum import Mangum

from .app.data_models import PredictionRequest, PredictionResponse
from .app.views import get_prediction


app = FastAPI()

@app.get("/hello")
def home():
    return {"hello": "world"}


@app.post("/prediction")
def make_model_prediction(request: PredictionRequest):
    return PredictionResponse(worldwide_gross=get_prediction(request))

handler = Mangum(app)
