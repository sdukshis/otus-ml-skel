import pandas

__all__ = ["family_size", "is_alone"]


def family_size(df: pandas.DataFrame) -> pandas.Series:
    return (
        df[["SibSp", "Parch"]]
        .apply(lambda row: row.SibSp + row.Parch + 1, axis=1)
        .astype(int)
    )


def is_alone(df: pandas.DataFrame) -> pandas.Series:
    return (
        df[["SibSp", "Parch"]]
        .apply(lambda row: row.SibSp == 0 and row.Parch == 0, axis=1)
        .astype(int)
    )


def test_func():
    pass
