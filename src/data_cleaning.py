import pandas as pd


def main():
    data_set = pd.read_csv("data/train/train_transaction.csv")
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    missing_values = data_set.isna().groupby(data_set["isFraud"]).mean()
    diff_vector = missing_values.loc[1] - missing_values.loc[0]
    print(diff_vector)


if __name__ == "__main__":
    main()