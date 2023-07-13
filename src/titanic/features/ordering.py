"""Implements column ordering"""
from __future__ import annotations

import pandas

__all__ = ["ColumnOrderer"]


class ColumnOrderer:
    """Remember columns order of pandas DataFrame on fit step and reorder to save on transform"""

    def __init__(self):
        self._features = []

    def fit(self, features: pandas.DataFrame, targets) -> ColumnOrderer:
        """Fits model"""
        self._features = features.columns
        return self

    def transform(self, features: pandas.DataFrame) -> pandas.DataFrame:
        """Returns features"""
        return features[self._features]

    def __repr__(self) -> str:
        return "ColumnOrderer()"
