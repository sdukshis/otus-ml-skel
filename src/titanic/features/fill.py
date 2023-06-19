"""Module providing imputer and fill functions"""
import pandas
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from sklearn.impute import SimpleImputer
import seaborn as sns

__all__ = ["embarked_imputer", "fill_embarked", "age_imputer", "fill_age"]


def embarked_imputer() -> SimpleImputer:
    """Function embarked_imputer"""
    return SimpleImputer(strategy="most_frequent")


def age_imputer() -> SimpleImputer:
    """Function age_imputer"""
    return SimpleImputer(strategy="median")


def fill_embarked(data: pandas.DataFrame) -> pandas.Series:
    """Function fill_embarked"""
    return embarked_imputer().fit_transform(data[["embarked"]])


def fill_age(data: pandas.DataFrame) -> pandas.Series:
    """Function fill_age"""
    return age_imputer().fit_transform(data[["age"]])


if __name__ == "__main__":
    titanic = sns.load_dataset('titanic')
    titanic = fill_age(titanic)
