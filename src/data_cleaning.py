import pandas as pd
import logging
from pathlib import Path

#----------------logging

LOG_DIR = Path(__file__).resolve().parent.parent / 'logs'
log_file = LOG_DIR / 'data_cleaning.log'

logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s-%(levelname)s %(message)s',
                    handlers=[logging.FileHandler(log_file),logging.StreamHandler()])

#----------------Data-cleaning

ROOT_DIR = Path(__file__).resolve().parent.parent
processed_dir = ROOT_DIR / 'data' / 'processed'
train_dir = processed_dir / 'train'
train_dir.mkdir(parents=True,exist_ok=True)

test_dir = processed_dir / 'test'
test_dir.mkdir(parents=True,exist_ok=True)

def process_data(raw_path: str) -> pd.DataFrame:
    logging.info(f"Getting Data from {raw_path} and applying Processing")
    test_path = raw_path / 'test' / 'test.csv'
    train_path = raw_path / 'train' / 'train.csv'
    
    train_df = pd.read_csv(train_path)
    for column in train_df.columns:
        if train_df[column].isnull().any():
            train_df[column] = train_df[column].fillna(train_df[column].mean())
    train_df.to_csv(train_dir/'preprocessed_train.csv',index=False)

    logging.info(f"Processed Train Data saved Sucessfully in {train_path}")
    
    test_df = pd.read_csv(test_path)
    for column in test_df.columns:
        if test_df[column].isnull().any():
            test_df[column] = test_df[column].fillna(test_df[column].mean())
    test_df.to_csv(test_dir/'preprocessed_test.csv',index=False) 
    
    logging.info(f"Processed Test Data saved Sucessfully in {test_path}")   
    
if __name__ == "__main__":
    ROOT_DIR = Path(__file__).resolve().parent.parent
    raw_path = ROOT_DIR / 'data'/'raw'
    process_data(raw_path=raw_path)