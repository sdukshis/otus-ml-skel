"""Module providing make_baseline_model function"""



from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from ..features.fill import embarked_imputer
from ..features.fill import age_imputer
from ..features.ordering import ColumnOrderer

__all__ = ["make_baseline_model"]


def make_baseline_model() -> Pipeline:
    """function make_baseline_model"""
    onehot_features = ["Sex", "Pclass"]

    embarked_transformer = Pipeline(
        steps=[
            ("emb_imputer", embarked_imputer()),
            ("onehot", OneHotEncoder()),
        ]
    )

    age_transformer = Pipeline(
        steps=[
            ("a_imputer", age_imputer())
        ]
    )

    onehot_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("Embarked", embarked_transformer, ["Embarked"]),
            ("Age", age_transformer, ["Age"]),
            ("Onehot", onehot_transformer, onehot_features),
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("column_orderer", ColumnOrderer()),
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression()),
        ]
    )

    return pipeline
