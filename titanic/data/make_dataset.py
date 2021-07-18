import os
from urllib.request import urlopen
import logging

import pandas

logger = logging.getLogger(__name__)

__all__ = ["load_titanic"]

URL = "https://gist.github.com/sdukshis/c4fa70ed0bd9468f6401ab8dc1e36f8d/raw/e62762bbb28d67b72ad1c4819b65b2fc67ae4b12/train.csv"

SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR_PATH = os.path.dirname(SCRIPT_PATH)
RAW_DATA_FOLDER = os.path.join(SCRIPT_DIR_PATH, "..", "..", "data", "raw")
TRAIN_PATH = os.path.join(RAW_DATA_FOLDER, "train.csv")


def load_titanic() -> pandas.DataFrame:
    if not os.path.exists(TRAIN_PATH):
        logger.info("Downloading dataset from %s", URL)
        opener = urlopen(URL)
        with open(TRAIN_PATH, "wb") as fd:
            fd.write(opener.read())

    return pandas.read_csv(TRAIN_PATH, index_col="PassengerId")
