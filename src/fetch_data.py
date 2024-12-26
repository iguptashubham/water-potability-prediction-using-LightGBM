import pandas as pd
import logging
from pathlib import Path

# Initialize logging
log_dir = Path(__file__).resolve().parent.parent / 'logs'
log_dir.mkdir(parents=True, exist_ok=True)  # Ensure the logs directory exists

log_file = log_dir / 'fetch_data.log'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler(log_file), logging.StreamHandler()])

FD_DIR = Path(__file__).resolve()
MAIN_DIR = FD_DIR.parent.parent
DATA_DIR = MAIN_DIR / 'data'
DATA_DIR.mkdir(parents=True, exist_ok=True)  # Ensure the data directory exists

def fetch_data(url_path: str):
    logging.info(f'Fetching data from {url_path}')
    df = pd.read_csv(url_path)
    save_data = DATA_DIR / 'raw' / 'water-potability.csv'
    save_data.parent.mkdir(parents=True, exist_ok=True)  # Ensure the raw data directory exists
    df.to_csv(save_data, index=False)
    logging.info(f'Data saved to {save_data}')

# Example usage
if __name__ == "__main__":
    fetch_data("https://raw.githubusercontent.com/DataThinkers/Datasets/refs/heads/main/DS/water_potability.csv")
