import pandas as pd
import numpy as np

def create_lack_info_column(dataset: pd.DataFrame):
    new_column = dataset.isnull().sum(axis=1).to_list()
    dataset["number_of_nulls"] = new_column
    return dataset


def add_time_columns(dataset: pd.DataFrame):
    seconds_passed = dataset["TransactionDT"]
    hour_column = seconds_passed // 3600 % 24
    dataset["hour"] = hour_column
    weekday_column = seconds_passed // 86400 % 7
    dataset["weekday"] = weekday_column
    return dataset


def apply_feature_engineering(dataset: pd.DataFrame):
    dataset = add_time_columns(dataset)
    dataset = create_lack_info_column(dataset)
    return dataset


def build_dtypes(file_path: str):
    column_names = pd.read_csv(file_path, nrows=0).columns.to_list()
    dtype_dict = {}
    global_mins = {}
    global_maxs = {}

    for chunk in pd.read_csv(file_path, chunksize=5_000):
        for column in column_names:
            series = chunk[column]

            if column in dtype_dict and dtype_dict[column] == "category":
                continue

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
        if dtype_dict.get(column) == "float32" or dtype_dict.get(column) == "category":
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

