import pandas
from sklearn.impute import SimpleImputer


__all__ = ["embarked_imputer", "fill_embarked"]


def embarked_imputer() -> SimpleImputer:
    """fill embarked feature"""
    return SimpleImputer(strategy="most_frequent")


def age_imputer() -> SimpleImputer:
    """fill age feature"""
    return SimpleImputer(strategy="median")


def fill_feature(
    input_data: pandas.DataFrame, input_feature_name: str, imputer_func_name: str
) -> pandas.Series:
    """general feature fill func"""
    return globals()[imputer_func_name]().fit_transform(
        input_data[[input_feature_name]]
    )


def fill_embarked(
    input_data: pandas.DataFrame,
    input_feature_name: str = "Embarked",
    imputer_func_name="embarked_imputer",
) -> pandas.Series:
    """wrapper to fill embark feature"""
    return fill_feature(input_data, input_feature_name, imputer_func_name)


def fill_age(
    input_data: pandas.DataFrame,
    input_feature_name: str = "Age",
    imputer_func_name="age_imputer",
) -> pandas.Series:
    """wrapper to fill age feature"""
    return fill_feature(input_data, input_feature_name, imputer_func_name)
