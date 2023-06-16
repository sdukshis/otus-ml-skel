import pytest
import pandas as pd
import numpy as np

from titanic.features.fill import fill_age


age_and_class = {
    1: [35, 40, 50, 60, 70, np.nan],
    2: [33, 40, 40, 45, 55, np.nan],
    3: [18, 25, 30, 35, 47, np.nan]
}

expected = {
    1: [35, 40, 50, 60, 70, 50],
    2: [33, 40, 40, 45, 55, 40],
    3: [18, 25, 30, 35, 47, 30]
}

age_and_class_without_cls = {
    1: [35, 40, 50, 60, 70, np.nan],
    2: [33, 40, 40, 45, 55, np.nan],
    np.nan: [18, 25, 30, 35, 47, np.nan]
}

expected_without_cls = {
    1: [35, 40, 50, 60, 70, 50],
    2: [33, 40, 40, 45, 55, 40],
    np.nan: [18, 25, 30, 35, 47, 40]
}

age_and_class_without_age = {
    1: [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    2: [33, 40, 40, 45, 55, np.nan],
    3: [18, 25, 30, 35, 47, np.nan]
}

expected_without_age = {
    1: [37, 37, 37, 37, 37, 37],
    2: [33, 40, 40, 45, 55, 40],
    3: [18, 25, 30, 35, 47, 30]
}

age_and_class_small = {
    1: [np.nan, np.nan],
    2: [33, np.nan],
    3: [18, np.nan]
}

expected_small = {
    1: [25, 25],
    2: [33, 33],
    3: [18, 18]
}


def make_df_from_dict(input_dict: dict) -> pd.DataFrame:
    pclass = []
    ages_on_board = []
    for cls, ages in input_dict.items():
        pclass.extend([cls] * len(ages))
        ages_on_board.extend(ages)

    df = pd.DataFrame({
        'Pclass': pclass,
        'Age': ages_on_board
    })

    return df


@pytest.mark.parametrize(
    ('age_and_class', 'expected'),
    [
        (age_and_class, expected),
        (age_and_class_without_cls, expected_without_cls),
        (age_and_class_without_age, expected_without_age),
        (age_and_class_small, expected_small),
    ]
)
def test_fill_age(age_and_class: dict, expected: dict):
    df = make_df_from_dict(age_and_class)
    df_expected = make_df_from_dict(expected)

    df_filled = fill_age(df, inplace=False)

    assert np.allclose(df_filled['Age'].values, df_expected['Age'].values)


@pytest.mark.parametrize(
    ('age_and_class', 'expected'),
    [
        ({1: [np.nan]}, 'The "Age" column is fully missed'),
        ({}, 'df is empty')
    ]
)
def test_fill_age_fail(age_and_class: dict, expected: str):
    df = make_df_from_dict(age_and_class)

    with pytest.raises(ValueError) as err:
        df_filled = fill_age(df, inplace=False)

    assert err.value.args[0] == expected
