import pandas as pd
import numpy as np
import xgboost as xgb

def set_model_option():
    pd.set_option("display.max_columns", None)
    param["eval_metric"] = "auc"


def main():
    col_set = pd.read_csv("data/traindataset/train1.csv",nrows=0).columns.to_list()
    train_set = pd.read_csv("data/traindataset/train1.csv", dtype=dtypes_dict)
    set_model_option()  



if __name__ == "__main__":
    main()