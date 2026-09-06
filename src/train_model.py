import pandas as pd
import numpy as np
import xgboost as xgb

def set_model_option():
    pd.set_option("display.max_columns", None)
    param["eval_metric"] = "auc"


def main():
    train_set = pd.read_csv("data/train/train_transaction.csv")
    pd.set_option("display.max_columns", None)


if __name__ == "__main__":
    main()