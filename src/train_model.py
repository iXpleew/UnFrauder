import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.metrics import precision_recall_curve, auc, roc_auc_score
from feature import *


FILE_PATH_TRAINX = "data/traindataset/new_train3.csv"
FILE_PATH_TRAINY = "data/traindataset/goal_train.csv"
FILE_PATH_VALIDATEX = "data/testdataset/new_test3.csv"
FILE_PATH_VALIDATEY = "data/testdataset/goal_test.csv"


def create_light_sets():
    dtypes_dict = build_dtypes(FILE_PATH_TRAINX)
    trainsetX = pd.read_csv(FILE_PATH_TRAINX, dtype=dtypes_dict)
    validatesetX = pd.read_csv(FILE_PATH_VALIDATEX, dtype=dtypes_dict)
    for category_dtype_column in trainsetX.select_dtypes(include=["category"]):
        validatesetX[category_dtype_column] = validatesetX[category_dtype_column].astype(trainsetX[category_dtype_column].dtype)
    
    trainsetY = pd.read_csv(FILE_PATH_TRAINY, dtype=dtypes_dict)
    validatesetY = pd.read_csv(FILE_PATH_VALIDATEY, dtype=dtypes_dict)
    return trainsetX, validatesetX, trainsetY, validatesetY


def evaluate_model(predictions: np.array, real_results: np.array):
    return roc_auc_score(real_results, predictions)


def main():
    trainX, testX, trainY, testY = create_light_sets()
    bst = XGBClassifier(enable_categorical=True, n_estimators=350, learning_rate=0.3)
    bst.fit(trainX, trainY)
    preds = bst.predict_proba(testX)[:, 1]
    print(f"Model roc-auc is {evaluate_model(np.array(preds), np.array(testY))}")


if __name__ == "__main__":
    main()