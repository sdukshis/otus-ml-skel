"""Module providing train_test_split function"""
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from typing import Tuple

import pandas
from sklearn.model_selection import train_test_split as sklean_train_test_split

__all__ = ["train_test_split"]


def train_test_split(
    data: pandas.DataFrame, test_size: float = 0.3, random_state: int = 42
) -> Tuple[pandas.DataFrame, pandas.DataFrame]:
    """Function train_test_split"""
    train_idxs, test_idxs = sklean_train_test_split(
        data.index, test_size=test_size, random_state=random_state
    )
    return data.loc[train_idxs], data.loc[test_idxs]
