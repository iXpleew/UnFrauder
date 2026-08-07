import pandas as pd
import numpy as np


def main():
    data_set = pd.read_csv("data/train/train_transaction.csv", chunksize=5_000)
    how_many_nans = 0
    for chunk in data_set:
        how_many_nans += chunk.isna().groupby(chunk["isFraud"]).sum()
    
    print(how_many_nans)
    # missing_values = data_set.isna().groupby(data_set["isFraud"]).mean()
    #diff_vector = missing_values.loc[1] - missing_values.loc[0]
    #print(diff_vector)


if __name__ == "__main__":
    main()