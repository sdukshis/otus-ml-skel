import pandas
from sklearn.impute import SimpleImputer


__all__ = ["embarked_imputer", "fill_embarked", "fill_age"]


def embarked_imputer() -> SimpleImputer:
    return SimpleImputer(strategy="most_frequent")


def fill_embarked(df: pandas.DataFrame) -> pandas.Series:
    return embarked_imputer().fit_transform(df[["Embarked"]])


def fill_age(df: pandas.DataFrame, inplace=False) -> pandas.DataFrame:

    if df.shape[0] == 0:
        raise ValueError("df is empty")

    if df[df["Age"].notna()].shape[0] == 0:
        raise ValueError('The "Age" column is fully missed')

    if not inplace:
        transformed = df.copy(deep=True)
    else:
        transformed = df

    age_all_over_cls = int(df["Age"].median())
    age_grouped = df.groupby("Pclass")["Age"].median()
    age_grouped.loc[age_grouped.isna()] = age_all_over_cls

    # Словарь, в котором не учтены NaN Pclass
    dict_to_age_map = age_grouped.astype(int).to_dict()

    for pclass, age_median in dict_to_age_map.items():
        nan_mask = (df["Pclass"] == pclass) & df["Age"].isna()
        transformed.loc[nan_mask, "Age"] = age_median

    # Заполнение тех, у которых Pclass был NaN и их не заполнили в предыдущих шагах
    transformed["Age"] = transformed["Age"].fillna(age_all_over_cls)

    return transformed


if __name__ == "__main__":
    from titanic.data.make_dataset import load_titanic

    titanic = load_titanic()
    titanic = fill_age(titanic, inplace=False)

    assert titanic[titanic["Age"].isna()].shape[0] == 0
