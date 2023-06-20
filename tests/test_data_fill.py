import pytest
import pandas as pd
import numpy as np
from titanic.features.fill import fill_age


@pytest.mark.parametrize(
    "input_data",
    [
        [
            ["male", 22.0],
            ["female", 38.0],
            ["female", 26.0],
            ["female", np.nan],
            ["male", 26.0],
            ["male", 32.0],
        ],
    ],
)
def test_age_fill(input_data: pd.DataFrame):
    input_data = pd.DataFrame(data=input_data, columns=["Sex", "Age"])
    age_filled = fill_age(
        input_data=input_data, input_feature_name="Age", imputer_func_name="age_imputer"
    )
    assert np.isnan(age_filled).sum() == 0
    assert age_filled.shape[0] == input_data.shape[0]
