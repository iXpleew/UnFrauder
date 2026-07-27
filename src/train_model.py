import pandas as pd
import matplotlib.pyplot as plt


def check_all_values(dseries: pd.Series):
    print(f"{dseries.name} values: ")
    print(dseries.value_counts())


def print_sample_data(data_set: pd.DataFrame):
    pd.set_option("display.max_columns", None)
    print(data_set.head(10))


def main():
    data_set = pd.read_csv("data/train/train_transaction.csv")
    pd.set_option("display.max_columns", None)

    print_sample_data(data_set)


    for name, column in data_set.items():
        if name == "V1":
            break
        if name == "TransactionID" or name == "TransactionDT":
            continue
        check_all_values(column)


if __name__ == "__main__":
    main()