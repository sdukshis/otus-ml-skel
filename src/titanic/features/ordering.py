"""Module providing class ColumnOrderer"""

from __future__ import annotations

import pandas

__all__ = ["ColumnOrderer"]


class ColumnOrderer:
    """Remember columns order of pandas DataFrame on fit step and reorder to save on transform"""

    def __init__(self):
        """__init__ method"""
        self._features = []

    def fit(self, data_x: pandas.DataFrame) -> ColumnOrderer:
        """fit method"""
        self._features = data_x.columns
        return self

    def transform(self, data_x: pandas.DataFrame) -> pandas.DataFrame:
        """transform method"""
        return data_x[self._features]

    def __repr__(self) -> str:
        """__repr__ method"""
        return "ColumnOrderer()"
