"""Feature extractor"""
import pandas

__all__ = ["family_size", "is_alone"]


def family_size(input_data: pandas.DataFrame) -> pandas.Series:
    """Generates family size feature"""
    return (
        input_data[["SibSp", "Parch"]]
        .apply(lambda row: row.SibSp + row.Parch + 1, axis=1)
        .astype(int)
    )


def is_alone(input_data: pandas.DataFrame) -> pandas.Series:
    """Checks if man was alone"""
    return (
        input_data[["SibSp", "Parch"]]
        .apply(lambda row: row.SibSp == 0 and row.Parch == 0, axis=1)
        .astype(int)
    )


def test_func():
    pass
