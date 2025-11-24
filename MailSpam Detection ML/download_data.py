import os
import urllib.request
import zipfile
import pandas as pd

# URL for the SMS Spam Collection Dataset (UCI Machine Learning Repository)
DATA_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
DATA_DIR = "data"
ZIP_FILE = os.path.join(DATA_DIR, "sms_spam_collection.zip")
EXTRACT_DIR = os.path.join(DATA_DIR, "extracted")

def download_and_prepare_data():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    # Download
    if not os.path.exists(ZIP_FILE):
        print(f"Downloading dataset from {DATA_URL}...")
        urllib.request.urlretrieve(DATA_URL, ZIP_FILE)
        print("Download complete.")
    else:
        print("Dataset already downloaded.")

    # Extract
    if not os.path.exists(EXTRACT_DIR):
        print("Extracting dataset...")
        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall(EXTRACT_DIR)
        print("Extraction complete.")
    
    # Read and convert to CSV for easier usage
    # The file usually is 'SMSSpamCollection' (tab separated)
    raw_file_path = os.path.join(EXTRACT_DIR, "SMSSpamCollection")
    if os.path.exists(raw_file_path):
        print("Converting to CSV...")
        df = pd.read_csv(raw_file_path, sep='\t', names=["label", "message"])
        csv_path = os.path.join(DATA_DIR, "spam_data.csv")
        df.to_csv(csv_path, index=False)
        print(f"Data saved to {csv_path}")
        print(df.head())
    else:
        print(f"Error: Could not find 'SMSSpamCollection' in {EXTRACT_DIR}")

if __name__ == "__main__":
    download_and_prepare_data()
