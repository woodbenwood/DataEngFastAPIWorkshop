import os
import shutil

from pandas import DataFrame


def data_eng(df: DataFrame) -> DataFrame:
    df = df.drop(columns=["_id", "Time Stamp"])
    df.columns = [col.lower() for col in df.columns]
    return df


def make_cache(temp: str):
    if os.path.exists(temp):
        shutil.rmtree(temp)
    os.mkdir(temp)
    return temp


def description_setup():
    with open("README.md", "r") as docs:
        next(docs)
        return docs.read()
