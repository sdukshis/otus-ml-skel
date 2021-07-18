import pandas
from sklearn.impute import SimpleImputer


__all__ = ["embarked_imputer", "fill_embarked"]


def embarked_imputer() -> SimpleImputer:
    return SimpleImputer(strategy="most_frequent")


def fill_embarked(df: pandas.DataFrame) -> pandas.Series:
    return embarked_imputer().fit_transform(df[["Embarked"]])
