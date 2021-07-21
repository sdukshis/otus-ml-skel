from typing import Tuple

import pandas
from sklearn.model_selection import train_test_split as sklean_train_test_split

__all__ = ["train_test_split"]


def train_test_split(
    df: pandas.DataFrame, test_size: float = 0.3, random_state: int = 42
) -> Tuple[pandas.DataFrame, pandas.DataFrame]:
    train_idxs, test_idxs = sklean_train_test_split(
        df.index, test_size=test_size, random_state=random_state
    )
    return df.loc[train_idxs], df.loc[test_idxs]
