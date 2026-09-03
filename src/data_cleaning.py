import pandas as pd
import numpy as np
import os

# COMMENTS FOR FUTURE
# commented code is meant for future methods that will be needed in analysis chapter
# no rows is 590540
# no rows train - 410000


def prepare_file(file_path: str):
    if os.path.isfile(file_path):
        os.remove(file_path)
    
    header = pd.read_csv("data/kaggle_dataset/train_transaction.csv", nrows=0)
    header.to_csv(file_path, header=True, index=False)


def split_dataset(dataset_itr: pd.DataFrame, no_rows: int):
    # split is 70/15/15

    prepare_file("data/testdataset/test.csv")
    prepare_file("data/validatedataset/validate.csv")
    prepare_file("data/traindataset/train.csv")

    validate_index: int = int(no_rows * 70/100)
    test_index: int = int(no_rows * 85/100)
    rows_counter: int = 0

    for chunk in dataset_itr:
        rows_counter += chunk.shape[0]
        if rows_counter >= test_index:
            chunk.to_csv("data/testdataset/test.csv", mode="a", header=False, index=False)
        elif rows_counter >= validate_index:
            chunk.to_csv("data/validatedataset/validate.csv", mode="a", header=False, index=False)
        else:
            chunk.to_csv("data/traindataset/train.csv", mode="a", header=False, index=False)


def number_of_rows(data_set: pd.DataFrame):
    # how_many_nans = 0
    records_number = 0

    for chunk in data_set:
        records_number += chunk.shape[0]
        # how_many_nans += chunk.isna().groupby(chunk["isFraud"]).sum()
    
    # print(how_many_nans)
    print(records_number)
    return records_number


def show_nans_everycolumn(data_set: pd.DataFrame):
    pd.set_option("display.max_columns", None)
    how_many_nans = pd.DataFrame()
    for chunk in data_set:
        if how_many_nans.empty:
            how_many_nans = chunk.isna().groupby(chunk["isFraud"]).sum()
        else:
            how_many_nans += chunk.isna().groupby(chunk["isFraud"]).sum()
        
    print(how_many_nans)


def show_nans_impact_fraud(data_set: pd.DataFrame):
    all_missing_values = pd.DataFrame
    for chunk in data_set:
        chunk_nans = chunk.isna().groupby(chunk["isFraud"]).sum()
        if all_missing_values.empty:
            all_missing_values = chunk_nans
        else:
            all_missing_values += chunk_nans
    print(all_missing_values)


def show_uniques_everycolumn():
    column_names = pd.read_csv("data/traindataset/train.csv", nrows=0)
    frauds_column = pd.read_csv("data/traindataset/train.csv", usecols=["isFraud"])
    for column_name in column_names:
        if column_name == "isFraud":
            continue
        column = pd.read_csv("data/traindataset/train.csv", skipinitialspace=True, usecols=[column_name])
        uniq_values = pd.concat([column, frauds_column], axis=1)
        based_uniqes = uniq_values.groupby(by=uniq_values["isFraud"]).value_counts()
        print(based_uniqes)


def show_nans_everycolumn():
    column_names = pd.read_csv("data/traindataset/train.csv", nrows=0)
    frauds_column = pd.read_csv("data/traindataset/train.csv", usecols=["isFraud"])
    for column_name in column_names:
        if column_name == "isFraud":
            continue
        column = pd.read_csv("data/traindataset/train.csv", skipinitialspace=True, usecols=[column_name])
        column_with_fraud = pd.concat([frauds_column, column], axis=1)
        based_uniqes = uniq_values.groupby(by=uniq_values["isFraud"]).value_counts()
        print(based_uniqes)
        

def main():
    # train_dataset_itr = pd.read_csv("data/traindataset/train.csv", chunksize=1000)
    show_nans_everycolumn()

    # missing_values = data_set.isna().groupby(data_set["isFraud"]).mean()
    #diff_vector = missing_values.loc[1] - missing_values.loc[0]
    #print(diff_vector)


if __name__ == "__main__":
    main()