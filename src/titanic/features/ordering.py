from __future__ import annotations

import pandas

__all__ = ["FeatureOrderer"]


class ColumnOrderer:
    """Remember columns order of pandas DataFrame on fit step and reorder to save on transform"""

    def __init__(self):
        self._features = []

    def fit(self, X: pandas.DataFrame, y) -> ColumnOrderer:
        self._features = X.columns
        return self

    def transform(self, X: pandas.DataFrame) -> pandas.DataFrame:
        return X[self._features]

    def __repr__(self) -> str:
        return "ColumnOrderer()"
