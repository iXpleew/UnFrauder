# UnFrauder
## About the project
Project was created as a side-project during summer break. The main goal was to deal with the real world problem which are fraudulent transactions. Data set that was used here comes from the kaggle competition 'IEEE-CIS Fraud Detection' provided by Vesta Corporation.

## Main first difficulties
Entire project was being created on Microsoft Azure cloud platform. This was caused by the fact that many companies nowadays have their pipelines on cloud platforms. Fortunately because of fact that I'm a student I was given 100$ of cloud computing credits for free which almost half of them I spent on that project.

The second issue was fact that I couldn't check which transactions of test data set were fraudulent and therefore I was forced to split the given training set by the creators of competition into 3 smaller data set (train/validate/test). Proportion that was used here is 70/15/15. Therefore the model has less data to train on compared to teams that participated in that kaggle contest


## Project itself
It was my first data science project and due to the lack of my experience I didn't know what to do at the beginning. So I had searched that first step to create a model is to do an EDA, so my first days were spent on it. I've created methods to show some anomalies, correlation and patterns.

Secondly I wanted to check what will be the result of a model that is trained on raw data. I used XGBoost, because I've searched that XGBoost works excellent with tabular data. Unfortunately data set was so huge and moreover my cloud machine had only 8GB of RAM I couldn't load entire dataset to my RAM. Therefore I created a method "build_dtypes()" that tries to optimize dtypes (type of every column) to the minimum on. It worked, because my set could easily be loaded into my RAM memory. Model with raw validation data set (with just transaction_train.csv) had ROC AUC, of about 90,1%. After merging it with train_idenitity.csv ROC-AUC dropped to 89,1%. 

Next up was data cleaning. I've deleted columns that were duplicates of another ones or have a huge correlation between any other one. With some modification (changed number of trees) my model achieved 91,17%. I was aware that my test result will be significant lower because of a "gap" that creates validation set (70% of dataset is training then 15% is validation and finally 15% is a test set). At the end the model achieved 88% for test set which is a nice result for a first project. I've tried to do some feature engineering with time passed (TransactionDT) and with number of missing values per column but it make the validation ROC-AUC lower.
