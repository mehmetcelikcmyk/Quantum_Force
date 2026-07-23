import os
import urllib.request

def download_data():
    raw_dir = os.path.join("data", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    
    url = "https://raw.githubusercontent.com/selva86/datasets/master/GermanCredit.csv"
    target_path = os.path.join(raw_dir, "german_credit_data.csv")
    
    print(f"Downloading dataset from: {url}")
    try:
        urllib.request.urlretrieve(url, target_path)
        print(f"Dataset successfully downloaded and saved to: {target_path}")
        
        # Simple validation
        if os.path.exists(target_path):
            file_size = os.path.getsize(target_path)
            print(f"File size: {file_size / 1024:.2f} KB")
            
            # Print first few lines
            with open(target_path, 'r') as f:
                print("\nFirst 3 lines of the dataset:")
                for _ in range(3):
                    print(f.readline().strip())
        else:
            print("Error: Target file was not created.")
    except Exception as e:
        print(f"An error occurred during download: {e}")

if __name__ == "__main__":
    download_data()
