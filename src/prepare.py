import sys
import logging

from dvc import api
import pandas as pd

from model_utils import get_config


def filter_and_combine_data(
    movie_df: pd.DataFrame, finantial_df: pd.DataFrame, opening_df: pd.DataFrame
) -> pd.DataFrame:
    """Filter columns and combine the 3 df for movies, finantial and opening gross.

    Args:
        movie_df (pd.DataFrame): movies dataframe.
        finantial_df (pd.DataFrame): finantials dataframe.
        opening_df (pd.DataFrame): opening gross dataframe.

    Returns:
        pd.DataFrame: data filtered and combined.
    """
    numeric_columns_mask = (movie_df.dtypes == float) | (movie_df.dtypes == int)
    numeric_columns = [
        column for column in numeric_columns_mask.index if numeric_columns_mask[column]
    ]
    movie_df = movie_df[numeric_columns + ["movie_title"]]

    finantial_df = finantial_df[["movie_title", "production_budget", "worldwide_gross"]]

    fin_movie_df = pd.merge(finantial_df, movie_df, on="movie_title", how="left")
    full_movie_data = pd.merge(opening_df, fin_movie_df, on="movie_title", how="left")
    full_movie_data.drop(["gross", "movie_title"], axis=1, inplace=True)
    return full_movie_data


logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

logging.info("Fetching data")
config = get_config()

movie_data_path = api.get_url(config["path"]["movie"], remote="dataset-track")
finantial_data_path = api.get_url(config["path"]["finantial"], remote="dataset-track")
opening_data_path = api.get_url(config["path"]["opening"], remote="dataset-track")

movie_df = pd.read_csv(movie_data_path)
finantial_df = pd.read_csv(finantial_data_path)
opening_df = pd.read_csv(opening_data_path)

full_movie_data = filter_and_combine_data(movie_df, finantial_df, opening_df)

full_movie_data.to_csv(config["path"]["full_data"], index=False)

logger.info("Data Fetched and prepared...")
