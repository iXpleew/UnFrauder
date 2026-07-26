import pandas as pd

def check_all_values(dset: pd.Series):
    print(dset.value_counts())

def print_sample_data():
    data_set = pd.read_csv("data/train/train_transaction.csv")
    pd.set_option("display.max_columns", None)
    print(data_set.head(10))


def main():
    data_set = pd.read_csv("data/train/train_transaction.csv")
    pd.set_option("display.max_columns", None)
    
    print("Is fraud:")
    check_all_values(data_set["isFraud"])


if __name__ == "__main__":
    main()