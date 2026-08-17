import pandas as pd
import numpy as np
import os

# COMMENTS FOR FUTURE
# dataaet is splitted now it's time for checking the values 
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


def delete_unimportant_columns(data_set: pd.DataFrame):
    for chunk in data_set:
        how_many_nans = chunk.isna().groupby(chunk["isFraud"]).sum()
        print(how_many_nans)
        break


def main():
    #data_set_itr = pd.read_csv("data/kaggle_dataset/train_transaction.csv", chunksize=5_000)
    #split_dataset(data_set_itr, 590_540)
    train_dataset_itr = pd.read_csv("data/traindataset/train.csv", chunksize=1_000)
    delete_unimportant_columns(train_dataset_itr)

    
    # missing_values = data_set.isna().groupby(data_set["isFraud"]).mean()
    #diff_vector = missing_values.loc[1] - missing_values.loc[0]
    #print(diff_vector)


if __name__ == "__main__":
    main()