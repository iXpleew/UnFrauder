import pandas as pd


def main():
    data_set = pd.read_csv("data/train/train_transaction.csv", chunksize=5000)
    for chunk in data_set:
        pass    
    print(data_set.min())
    print(data_set.max())

    # missing_values = data_set.isna().groupby(data_set["isFraud"]).mean()
    #diff_vector = missing_values.loc[1] - missing_values.loc[0]
    #print(diff_vector)


if __name__ == "__main__":
    main()