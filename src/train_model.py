import pandas as pd
import pdcast as pdc
import numpy as np
import xgboost as xgb

FILE_PATH = "data/traindataset/train1.csv"


def set_model_option():
    pd.set_option("display.max_columns", None)
    param["eval_metric"] = "auc"


def build_dtypes():
    column_names = pd.read_csv(FILE_PATH, nrows=0).columns.to_list()
    dtype_dict = {}
    for column in column_names:
        series = pd.read_csv(FILE_PATH, usecols=[column])[column]

        if series.dtype == "object":
            dtype_dict[column] = "category"

def main():
    trainset = pd.read_csv(FILE_PATH, nrows=2)  
    dtypes = trainset.dtypes.replace({"object": "category", "int64": "int16", "float64": "float32"}).to_dict()


    trainset = pd.read_csv(FILE_PATH, dtype=dtypes)
    print(trainset.memory_usage(deep=True).sum())

if __name__ == "__main__":
    main()