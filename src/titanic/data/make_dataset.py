import os
from typing import Optional
from urllib.request import urlopen
import logging

import pandas

logger = logging.getLogger(__name__)

__all__ = ["load_titanic"]

URL = "https://gist.github.com/sdukshis/c4fa70ed0bd9468f6401ab8dc1e36f8d/raw/e62762bbb28d67b72ad1c4819b65b2fc67ae4b12/train.csv"

SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR_PATH = os.path.dirname(SCRIPT_PATH)
RAW_DATA_FOLDER = os.path.join(SCRIPT_DIR_PATH, "..", "..", "..", "data", "raw")
TRAIN_PATH = os.path.join(RAW_DATA_FOLDER, "train.csv")


def load_titanic(datapath: Optional[str] = None) -> pandas.DataFrame:
    if datapath is None:
        datapath = TRAIN_PATH

    if not os.path.exists(datapath):
        logger.info("Downloading dataset from %s", URL)
        opener = urlopen(URL)
        with open(datapath, "wb") as fd:
            fd.write(opener.read())

    logging.info("Reading dataset from %s", datapath)
    return pandas.read_csv(datapath, index_col="PassengerId")
