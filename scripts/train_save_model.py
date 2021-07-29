#!/usr/bin/env python
"""Train and save model for Titanic"""

import argparse
from typing import NoReturn
import logging
import sys

import pandas
from sklearn.pipeline import Pipeline

from titanic.models import train
from titanic.models.serialize import store
from titanic.data.make_dataset import load_titanic


logger = logging.getLogger()


def main():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "-m",
        "--model",
        required=True,
        help="model name (must be importable from titanic.models.train module)",
    )
    argparser.add_argument(
        "-d",
        "--datapath",
        required=False,
        default=None,
        help="dataset store path",
    )
    argparser.add_argument(
        "-o", "--output", required=True, help="filename to store model"
    )
    argparser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )
    args = argparser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    model_train_func = getattr(train, args.model)
    model = model_train_func()
    logging.info("Model '%s' created", args.model)
    dataset = load_titanic(args.datapath)
    train_store(dataset, model, args.output)


def train_store(dataset: pandas.DataFrame, model: Pipeline, filename: str) -> NoReturn:
    y = dataset["Survived"]
    X = dataset.drop("Survived", axis=1)

    logger.info("Training model on %d items", len(X))
    model.fit(X, y)
    store(model, filename)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(e)
        sys.exit(1)
