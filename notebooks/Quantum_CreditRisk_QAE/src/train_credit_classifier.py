import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb

def train_classifier():
    raw_path = os.path.join("data", "raw", "german_credit_data.csv")
    if not os.path.exists(raw_path):
        print("Error: german_credit_data.csv not found! Run data_downloader.py first.")
        return
        
    df = pd.read_csv(raw_path)
    
    # Preprocessing
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    df_processed = df.copy()
    for col in cat_cols:
        le = LabelEncoder()
        df_processed[col] = le.fit_transform(df[col])
        
    df_processed['default'] = 1 - df_processed['credit_risk']
    df_processed.drop(columns=['credit_risk'], inplace=True)
    
    X = df_processed.drop(columns=['default'])
    y = df_processed['default']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Train XGBoost model
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.08,
        random_state=42,
        use_label_encoder=False,
        eval_metric='logloss'
    )
    model.fit(X_train, y_train)
    
    # Predict default probabilities
    y_prob = model.predict_proba(X_test)[:, 1]
    
    # Build a small credit portfolio for Quantum QAE (3 loans)
    np.random.seed(42)
    portfolio_indices = np.random.choice(X_test.index, size=3, replace=False)
    
    portfolio_df = pd.DataFrame({
        'Client_ID': portfolio_indices,
        'Default_Probability': model.predict_proba(X.loc[portfolio_indices])[:, 1],
        'Loss_Given_Default': [100000.0, 250000.0, 150000.0]
    })
    
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    
    portfolio_df.to_csv(os.path.join(processed_dir, "predicted_portfolio.csv"), index=False)
    print("\nSaved portfolio file successfully to data/processed/predicted_portfolio.csv")
    print(portfolio_df)

if __name__ == "__main__":
    train_classifier()
