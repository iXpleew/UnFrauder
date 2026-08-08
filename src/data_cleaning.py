import pandas as pd
import numpy as np


# data set is sortd, now it's time for splitting data set

def split_dataset(data_set: pd.DataFrame):
    pass


def data_analysis(data_set: pd.DataFrame):
    how_many_nans = 0
    records_number = 0

    for chunk in data_set:
        print(chunk["TransactionDT"][100])
        new_set = chunk.sort_values(by=["TransactionDT"])
        print(new_set["TransactionDT"][100])
        break

        records_number += chunk.shape[0]
        how_many_nans += chunk.isna().groupby(chunk["isFraud"]).sum()
    
    print(how_many_nans)
    print(records_number)


def main():
    data_set = pd.read_csv("data/train/train_transaction.csv", chunksize=5_000)
    data_analysis(data_set)
    # missing_values = data_set.isna().groupby(data_set["isFraud"]).mean()
    #diff_vector = missing_values.loc[1] - missing_values.loc[0]
    #print(diff_vector)


if __name__ == "__main__":
    main()