import os
import zipfile
import urllib.request

def download_data():
    # Target directories
    raw_data_dir = os.path.join("data", "raw")
    os.makedirs(raw_data_dir, exist_ok=True)
    
    zip_path = os.path.join(raw_data_dir, "creditcard.zip")
    csv_path = os.path.join(raw_data_dir, "creditcard.csv")
    
    # If csv already exists, skip
    if os.path.exists(csv_path):
        print(f"Dataset already exists at {csv_path}. Skipping download.")
        return
        
    # List of fallback URLs to download from
    urls = [
        "https://raw.githubusercontent.com/stat432/credit-analysis/main/data-raw/creditcard.csv.zip",
        "https://github.com/vatsal-dhama/Credit-Card-Fraud-Detection/raw/master/creditcard.csv.zip",
        "https://github.com/dominodatalab/reference-project-fraud-detection/raw/master/data/creditcard.csv.zip",
        "https://github.com/nsethi31/Kaggle-Data-Credit-Card-Fraud-Detection/raw/master/creditcard.csv.zip"
    ]
    
    download_success = False
    for url in urls:
        try:
            print(f"Attempting to download dataset from: {url}")
            # Download file
            urllib.request.urlretrieve(url, zip_path)
            print(f"Downloaded zip file to {zip_path}")
            
            # Extract zip file
            print("Extracting dataset...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(raw_data_dir)
            print(f"Successfully extracted dataset to {raw_data_dir}")
            
            # Clean up zip
            if os.path.exists(zip_path):
                os.remove(zip_path)
                print("Cleaned up zip file.")
            
            download_success = True
            break
        except Exception as e:
            print(f"Failed to download from {url}. Error: {e}")
            if os.path.exists(zip_path):
                os.remove(zip_path)
                
    if not download_success:
        print("\n[ERROR] Could not download the dataset from any of the URLs.")
        print("Please download 'creditcard.csv' manually from Kaggle (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)")
        print(f"and place it directly into the '{raw_data_dir}' folder.")
    else:
        print("\n[SUCCESS] Dataset is ready for preprocessing.")

if __name__ == "__main__":
    download_data()
