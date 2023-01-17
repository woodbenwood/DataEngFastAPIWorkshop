import os
import shutil


def make_cache(temp: str):
    if os.path.exists(temp):
        shutil.rmtree(temp)
    os.mkdir(temp)
