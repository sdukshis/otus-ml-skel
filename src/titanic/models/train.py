""" Scikit-learn pipeline to fill missing values, encode input and run classification"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression


from ..features.fill import embarked_imputer
from ..features.ordering import ColumnOrderer

__all__ = ["make_baseline_model"]


def make_baseline_model() -> Pipeline:
    """Baseline classifier

    Returns:
        Pipeline: column orderer, preprocessor and classifier
    """
    onehot_features = ["Sex", "Pclass"]

    embarked_transformer = Pipeline(
        steps=[
            ("imputer", embarked_imputer()),
            ("onehot", OneHotEncoder()),
        ]
    )
    onehot_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("Embarked", embarked_transformer, ["Embarked"]),
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
