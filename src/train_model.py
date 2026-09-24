import pandas as pd
import pdcast as pdc
import numpy as np
import xgboost as xgb

FILE_PATH = "data/traindataset/train1.csv"

def set_model_option():
    pd.set_option("display.max_columns", None)
    param = {"eval_metric": "auc"}
    return param


def build_dtypes():
    column_names = pd.read_csv(FILE_PATH, nrows=0).columns.to_list()
    dtype_dict = {}
    global_mins = {}
    global_maxs = {}

    for chunk in pd.read_csv(FILE_PATH, chunksize=5_000):
        for column in column_names:
            series = chunk[column]

            if series.dtype == "object":
                dtype_dict[column] = "category"
                continue
            elif pd.api.types.is_float_dtype(series):
                dtype_dict[column] = "float32"
                continue
            elif pd.api.types.is_integer_dtype(series):
                if dtype_dict.get(column) == "float32":
                    continue
                chunk_min = series.min()
                chunk_max = series.max()

                global_mins[column] = min(global_mins.get(column, float('inf')), chunk_min)
                global_maxs[column] = max(global_maxs.get(column, float('-inf')), chunk_max)

    for column, col_min in global_mins.items():
        if dtype_dict.get(column) == "float32":
            continue
        col_max = global_maxs[column]

        if col_min >= np.iinfo(np.int8).min and col_max <= np.iinfo(np.int8).max:
            dtype_dict[column] = "int8"
        elif col_min >= np.iinfo(np.int16).min and col_max <= np.iinfo(np.int16).max:
            dtype_dict[column] = "int16"
        elif col_min >= np.iinfo(np.int32).min and col_max <= np.iinfo(np.int32).max:
            dtype_dict[column] = "int32"
        else:
            dtype_dict[column] = "int64"

    return dtype_dict


def main():
    dtypes_dict = build_dtypes()
    trainset = pd.read_csv(FILE_PATH, dtype=dtypes_dict)

    print(trainset.memory_usage(deep=True).sum())

if __name__ == "__main__":
    main()