from sklearn.model_selection import train_test_split
from pathlib import Path
import logging
import pandas as pd

#--------logging----------

log_dir = Path(__file__).resolve().parent.parent / 'logs'
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'split_data.log'

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s',
                    handlers=[logging.FileHandler(log_file),logging.StreamHandler()])

#--------Split Data-------

MAIN_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = MAIN_DIR / 'data' / 'raw'

def split_data(data_path:str):
    logging.info(f"Get data from {data_path}")
    
    df = pd.read_csv(data_path)
    train_data,test_data = train_test_split(df,
                                            test_size=0.25,
                                            shuffle=True)
    logging.info("Spliting Data into Train and Test Dataset")
    
    TRAIN_DIR = DATA_DIR / 'train'
    TEST_DIR = DATA_DIR / 'test'
    
    TRAIN_DIR.mkdir(parents=True, exist_ok=True)
    TEST_DIR.mkdir(parents=True, exist_ok=True)
    
    logging.info(f"save train data into {TRAIN_DIR} and test data into {TEST_DIR}")
    train_data.to_csv(TRAIN_DIR / "train.csv", index=False)
    test_data.to_csv(TEST_DIR / "test.csv", index=False)
    
    logging.info(f"Data Splitted an Saved Successfully")
    
if __name__ == "__main__":
    MAIN_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = MAIN_DIR / 'data' / 'raw'
    split_data(data_path= DATA_DIR/'water-potability.csv')