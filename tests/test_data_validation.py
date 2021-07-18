import numpy as np
import pytest
import pandas as pd

from titanic.data.validation import *


@pytest.mark.parametrize("input_size", [100, 101])
def test_data_split(input_size):
    df = pd.DataFrame(np.random.randn(input_size, 2))
    train, test = train_test_split(df)
    assert input_size == len(train) + len(test)


@pytest.mark.parametrize("input_size", [0, 1])
def test_data_split_fail(input_size):
    df = pd.DataFrame(np.random.randn(input_size, 2))
    with pytest.raises(ValueError):
        train, test = train_test_split(df)
