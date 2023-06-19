import pytest
import pandas as pd
import numpy as np

from src.titanic.features.fill import *

data_test = pd.DataFrame({'Age': [25, 12, 6, np.nan]})
data_true = [[25.], [12.], [6.], [12.]]

@pytest.mark.parametrize("test_input,expected", [(data_test, data_true)])

def test_fill_age(test_input, expected):
    age_filled = fill_age(test_input)
    assert np.allclose(age_filled, expected)

