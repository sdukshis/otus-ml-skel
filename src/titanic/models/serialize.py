import os
import logging

import joblib
from sklearn.pipeline import Pipeline

__all__ = ["store", "load"]

logger = logging.getLogger()


def store(pipeline: Pipeline, filename: str, path: str = "default"):
    if path == "default":
        path = models_path()
    filepath = os.path.join(path, filename + ".joblib")

    logger.info("Dumpung model into %s", filepath)
    joblib.dump(pipeline, filepath)


def load(filename: str, path: str = "default") -> Pipeline:
    if path == "default":
        path = models_path()
    filepath = os.path.join(path, filename + ".joblib")

    logger.info("Loading model from %s", filepath)
    return joblib.load(filepath)


def models_path() -> str:
    script_path = os.path.abspath(__file__)
    script_dir_path = os.path.dirname(script_path)
    models_folder = os.path.join(script_dir_path, "..", "..", "..", "models")
    return models_folder
