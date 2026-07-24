import pandas as pd


def print_sample_data():
    data_set = pd.read_csv("data/raw/train_transaction.csv")
    print(data_set.head(10))


def main():
    print_sample_data()


if __name__ == "__main__":
    main()