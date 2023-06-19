"""Module providing family_size,  is_alone, test_func functions"""
import pandas

__all__ = ["family_size", "is_alone"]


def family_size(data: pandas.DataFrame) -> pandas.Series:
    """Function family_size"""
    return (
        data[["SibSp", "Parch"]]
        .apply(lambda row: row.SibSp + row.Parch + 1, axis=1)
        .astype(int)
    )


def is_alone(data: pandas.DataFrame) -> pandas.Series:
    """Function is_alone"""
    return (
        data[["SibSp", "Parch"]]
        .apply(lambda row: row.SibSp == 0 and row.Parch == 0, axis=1)
        .astype(int)
    )


def test_func():
    """test_func"""
