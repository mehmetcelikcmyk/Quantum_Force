import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def preprocess_data(n_components=6, sample_size_per_class=250, test_size=0.2, random_state=42):
    print("Starting data preprocessing...")
    
    # Path settings
    csv_path = os.path.join("data", "raw", "creditcard.csv")
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    
    if not os.path.exists(csv_path):
        print(f"[ERROR] Raw dataset not found at {csv_path}. Please run 'data_downloader.py' first.")
        return
        
    print(f"Loading raw dataset from {csv_path}...")
    df = pd.read_csv(csv_path)
    print(f"Loaded dataset with shape: {df.shape}")
    
    # Separate fraud and normal transactions
    normal_df = df[df['Class'] == 0]
    fraud_df = df[df['Class'] == 1]
    
    print(f"Number of normal transactions: {len(normal_df)}")
    print(f"Number of fraud transactions: {len(fraud_df)}")
    
    # Downsample to handle imbalance and fit into quantum memory/simulation constraints
    # We sample 'sample_size_per_class' from each class
    n_normal_samples = min(len(normal_df), sample_size_per_class)
    n_fraud_samples = min(len(fraud_df), sample_size_per_class)
    
    print(f"Sampling {n_normal_samples} normal and {n_fraud_samples} fraud transactions (Total: {n_normal_samples + n_fraud_samples})")
    
    normal_sampled = normal_df.sample(n=n_normal_samples, random_state=random_state)
    fraud_sampled = fraud_df.sample(n=n_fraud_samples, random_state=random_state)
    
    balanced_df = pd.concat([normal_sampled, fraud_sampled]).sample(frac=1, random_state=random_state).reset_index(drop=True)
    
    # Separate features and labels
    # Feature columns are 'Time', 'Amount', and 'V1' through 'V28'
    X = balanced_df.drop(columns=['Class'])
    y = balanced_df['Class'].values
    
    # Standardize features before applying PCA
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Dimensionality Reduction using PCA
    print(f"Applying PCA to reduce features to {n_components} components...")
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    
    explained_variance = np.sum(pca.explained_variance_ratio_)
    print(f"PCA Total Explained Variance Ratio: {explained_variance:.4f}")
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_pca, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print(f"Training set shape: {X_train.shape}, Labels: {np.bincount(y_train)}")
    print(f"Testing set shape: {X_test.shape}, Labels: {np.bincount(y_test)}")
    
    # Save processed files
    np.save(os.path.join(processed_dir, "train_x.npy"), X_train)
    np.save(os.path.join(processed_dir, "test_x.npy"), X_test)
    np.save(os.path.join(processed_dir, "train_y.npy"), y_train)
    np.save(os.path.join(processed_dir, "test_y.npy"), y_test)
    
    print("[SUCCESS] Preprocessing completed and data saved to data/processed/")

if __name__ == "__main__":
    # We use 6 PCA components and 80 samples per class (Total: 160 samples)
    # This is a good balance for running QSVM simulations in reasonable time
    preprocess_data(n_components=6, sample_size_per_class=80, test_size=0.2, random_state=42)
