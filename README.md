# UnFrauder
## About the project
Project was created as a side-project during summer break. The main goal was to deal with the real world problem which are fraudulent transactions. Data set that was used here comes from the kaggle competition 'IEEE-CIS Fraud Detection' provided by Vesta Corporation.


## Main first difficulties
Entire project was being created on Microsoft Azure cloud platform. This was caused by the fact that many companies nowadays have their pipelines on cloud platforms. Fortunately because of fact that I'm a student I was given 100$ of cloud computing credits for free almost half of which I spent on that project.

The second issue was fact that I couldn't check which transactions of test data set were fraudulent and therefore I was forced to split the given training set by the creators of competition into 3 smaller data set (train/validate/test). Proportion that was used here is 70/15/15. Therefore the model has less data to train on compared to teams that participated in that kaggle contest


## Project itself
It was my first data science project and due to the lack of my experience I didn't know what to do at the beginning. So I had searched that first step to create a model is to do an EDA, so my first days were spent on it. I've created methods to show some anomalies, correlation and patterns.

Secondly I wanted to check what will be the result of a model that is trained on raw data. I used XGBoost, because I've searched that XGBoost works excellent with tabular data. Unfortunately data set was so huge and moreover my cloud machine had only 8GB of RAM I couldn't load entire dataset to my RAM. Therefore I created a method "build_dtypes()" that tries to optimize dtypes (type of every column) to the minimum on. It worked, because my set could easily be loaded into my RAM memory. Model with raw validation data set (with just `train_transaction.csv`) had ROC AUC, of about 90.1%. After merging it with `train_identity.csv` ROC-AUC dropped to 89.1%. 

Next up was data cleaning. I've deleted columns that were duplicates of another ones or have a huge correlation between any other one. With some modification (changed number of trees) my model achieved 91.17%. I was aware that my test result will be significant lower likely because of a "gap" that creates validation set (70% of dataset is training then 15% is validation and finally 15% is a test set). At the end the model achieved 88.4% I've tried to do some feature engineering with time passed (TransactionDT) and with number of missing values per row but it make the validation ROC-AUC lower.


## Results
All scores are ROC AUC on the validation set (the 15% of rows following the training period), unless stated otherwise. Model: XGBoost.

| # | Change | Validation ROC AUC | Comment |
|---|--------|--------------------|---------|
| 1 | Baseline: `train_transaction` only, default parameters (100 trees) | 90.15% | PR AUC of the same setup: 0.536 |
| 2 | Removed ~20 duplicated columns | 90.35% | small gain |
| 3 | Removed V columns with absolute correlation >= 0.925 | 90.42% | within noise; threshold chosen on validation |
| 4 | Merged with `train_identity` (all identity columns) | 89.37% | worse |
| 5 | Dropped `id_10`-`id_38`, `DeviceInfo`, `DeviceType`; kept `id_01`-`id_09` and `TransactionID` | 90.45% | better than the full merge, no clear gain over step 3 |
| 6 | 1000 trees | 90.76% | |
| 7 | 350 trees (learning rate 0.3) | 91.17% | number of trees chosen on validation |

### Feature engineering experiments (relative to 91.17%)
| Added features | Validation ROC AUC | Difference |
|----------------|--------------------|------------|
| `number_of_nulls` (missing values per row) | 90.84% | -0.3 pp |
| `hour` + `weekday` from `TransactionDT` | 90.20% | -1.0 pp |
| both | 90.32% | -0.8 pp |

None of these features helped, so they are not used in the final model.

### Final result (test set, last 15% of the data)
| Model | Test ROC AUC |
|-------|--------------|
| XGBoost, 350 trees, learning rate 0.3, configuration frozen after validation | 88.4% |


### Notes
- Differences below roughly 0.2-0.5 percentage points should be treated as noise. This is a rough estimate based on about 3,000 fraud cases in the validation set, not a formal test.
- The threshold for correlated columns, the number of trees and the decision to keep `TransactionID` were all chosen using the validation set, so validation scores are slightly optimistic. The test score is the more honest figure.
- The 2.8 pp gap between validation and test is likely caused by fraud patterns changing over time (the test set is the furthest from the training period). This is a hypothesis, not a verified conclusion.
- `TransactionID` is kept as a feature because removing it lowered the validation score. My hypothesis is that it works as a proxy for time. I did not verify this.

## How to run
All commands are run in a terminal, from the root folder of the project (the paths in the code are relative).

### Requirements

- Python 3.13
- About 8 GB of RAM (the project was developed on a machine with 8 GB) and a few GB of free disk space for intermediate files

### 1. Install
    git clone <https://github.com/iXpleew/UnFrauder.git>
    cd UnFrauder
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

### 2. Get the data

The data is not included in this repository

1. Log in to Kaggle and accept the rules of the [IEEE-CIS Fraud Detection](https://www.kaggle.com/c/ieee-fraud-detection/data) competition.
2. Download `train_transaction.csv` and `train_identity.csv` (the other files are not used).
3. Create the folders below and put both files in `data/kaggle_dataset/`:

        data/kaggle_dataset/
        data/traindataset/
        data/validatetaset/
        data/testdataset/

### 3. Prepare the data

    python src/data_cleaning.py

This script:
1. merges `train_transaction.csv` with `train_identity.csv` (left join),
2. splits the rows in time order into train / validation / test (410,000 / 90,000 / 90,540 rows, about 70/15/15),
3. saves the target (`isFraud`) to separate files,
4. drops V columns whose absolute correlation with another V column is at least 0.925 (decided on the training set only),
5. drops `id_10`-`id_38`, `DeviceInfo` and `DeviceType`.

It creates several intermediate CSV files in the `data/` folders. The final files used for training are `new_train3.csv` and `goal_train.csv` (train) and `new_test3.csv` and `goal_test.csv` (test). The validation set is written to disk, but it is not used by the training script.

### 4. Train and evaluate

    python src/train_model.py

Trains XGBoost (350 trees, learning rate 0.3) on the training set and prints ROC AUC on the test set. I got about 0.884; small differences are possible between library versions.

### Troubleshooting

- `Killed` in the terminal: the machine ran out of RAM.
- `FileNotFoundError`: check that the folders and file names from step 2 are exactly as above and that you run the commands from the project root.