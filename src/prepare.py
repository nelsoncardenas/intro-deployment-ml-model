from io import StringIO
import sys
import logging

from dvc import api
import pandas as pd

from utils import get_config


logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

logging.info("Fetching data")
config = get_config()

movie_data_path = api.get_url(config["path"]["movies"], remote="dataset-tracker")
finantial_data_path = api.get_url(
    config["path"]["finantials"], remote="dataset-tracker"
)
opening_data_path = api.get_url(config["path"]["openings"], remote="dataset-tracker")

"""print(movie_data_path, finantial_data_path, opening_data_path)
breakpoint()
movie_df = pd.read_csv(movie_data_path)
finantial_df = pd.read_csv(finantial_data_path)
opening_df = pd.read_csv(opening_data_path)

breakpoint()"""