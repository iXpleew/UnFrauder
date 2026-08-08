import pandas as pd
import numpy as np

# COMMENTS FOR FUTURE
# data set is sortd, now it's time for splitting data set
# commented code is meant for future methods that will be needed in analysis chapter
# no rows is 590540


def split_dataset(data_set: pd.DataFrame, no_rows: int):
    # split is 70/15/15
    validate_index: int = int(no_rows * 70/100)
    test_index: int = int(no_rows * 85/100)
    pass


def number_of_rows(data_set: pd.DataFrame):
    # how_many_nans = 0
    records_number = 0

    for chunk in data_set:
        records_number += chunk.shape[0]
        # how_many_nans += chunk.isna().groupby(chunk["isFraud"]).sum()
    
    # print(how_many_nans)
    print(records_number)
    return records_number


def main():
    data_set_itr = pd.read_csv("data/kaggle_dataset/train_transaction.csv", chunksize=5_000)
    print(number_of_rows(data_set_itr))

    # no rows: 590540

    # missing_values = data_set.isna().groupby(data_set["isFraud"]).mean()
    #diff_vector = missing_values.loc[1] - missing_values.loc[0]
    #print(diff_vector)


if __name__ == "__main__":
    main()