import pandas
from sklearn.impute import SimpleImputer


__all__ = ["embarked_imputer", "fill_embarked"]


def embarked_imputer() -> SimpleImputer:
    return SimpleImputer(strategy="most_frequent")

# def age_imputer() -> SimpleImputer:
#     return SimpleImputer(strategy=)


def fill_embarked(df: pandas.DataFrame) -> pandas.Series:
    return embarked_imputer().fit_transform(df[["Embarked"]])

def fill_age(df: pandas.DataFrame, inplace=False) -> pandas.DataFrame:
    if not inplace:
        transformed = df.copy(deep=True)
    else:
        transformed = df

    dict_to_age_map = df.groupby('Pclass')['Age'].median().astype(int).to_dict()
    for pclass in df['Pclass'].unique():
        nan_mask = (df['Pclass'] == pclass) & df['Age'].isna()
        transformed.loc[nan_mask, 'Age'] = dict_to_age_map[pclass]

    return transformed


if __name__ == '__main__':
    from titanic.data.make_dataset import load_titanic

    titanic = load_titanic()
    titanic = fill_age(titanic, inplace=False)

    assert titanic[titanic['Age'].isna()].shape[0] == 0

