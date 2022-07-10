from pydantic import BaseModel


class PredictionRequest(BaseModel):
    opening_gross: float
    screens: float
    production_budget: float
    title_year: int
    aspect_ratio: float
    duration: int
    cast_total_facebook_likes: float
    budget: float
    imdb_score: float

    class Config:
        extra = "forbid"
        schema_extra = {
            "example": {
                "opening_gross": 8330681,
                "screens": 2271,
                "production_budget": 13000000,
                "title_year": 1999,
                "aspect_ratio": 1.85,
                "duration": 97,
                "cast_total_facebook_likes": 37907,
                "budget": 16000000,
                "imdb_score": 7.2,
            }
        }


class PredictionResponse(BaseModel):
    worldwide_gross: str

    class Config:
        extra = "forbid"
