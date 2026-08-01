import os
import numpy as np
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def run_classical_baselines():
    print("=== Training Classical Baseline Models ===")
    
    # Load processed data
    processed_dir = os.path.join("data", "processed")
    try:
        X_train = np.load(os.path.join(processed_dir, "train_x.npy"))
        X_test = np.load(os.path.join(processed_dir, "test_x.npy"))
        y_train = np.load(os.path.join(processed_dir, "train_y.npy"))
        y_test = np.load(os.path.join(processed_dir, "test_y.npy"))
    except FileNotFoundError:
        print("[ERROR] Preprocessed data not found. Please run 'data_preprocessing.py' first.")
        return
        
    print(f"Loaded train data size: {X_train.shape}")
    print(f"Loaded test data size: {X_test.shape}")
    
    # Define models
    models = {
        "Support Vector Machine (RBF)": SVC(kernel='rbf', probability=True, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Gradient Boosting (GBM)": GradientBoostingClassifier(random_state=42)
    }
    
    # Results dictionary
    results = {}
    
    # Train and evaluate each model
    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train, y_train)
        
        # Predict
        y_pred = model.predict(X_test)
        # Probabilities for AUC
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
        else:
            y_prob = model.decision_function(X_test)
            
        # Calculate metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_prob)
        
        results[name] = {
            "Accuracy": acc,
            "Precision": prec,
            "Recall": rec,
            "F1-Score": f1,
            "ROC-AUC": auc
        }
        
        print(f"Results for {name}:")
        print(f"  Accuracy:  {acc:.4f}")
        print(f"  Precision: {prec:.4f}")
        print(f"  Recall:    {rec:.4f}")
        print(f"  F1-Score:  {f1:.4f}")
        print(f"  ROC-AUC:   {auc:.4f}")
        print(f"  Ornek Test Islemleri Tahminleri:")
        for i in range(min(5, len(y_test))):
            real_status = "SUPHELI (Fraud)" if y_test[i] == 1 else "GUVENLI (Normal)"
            pred_status = "SUPHELI (Fraud)" if y_pred[i] == 1 else "GUVENLI (Normal)"
            result = "DOGRU" if y_test[i] == y_pred[i] else "YANLIS"
            print(f"    Islem {i+1}: Gercek={real_status:<16} Tahmin={pred_status:<16} ({result})")

    # Print final comparison table
    print("\n" + "="*50)
    print("CLASSICAL MODELS PERFORMANCE COMPARISON")
    print("="*50)
    print(f"{'Model Name':<30} | {'F1-Score':<8} | {'ROC-AUC':<8} | {'Accuracy':<8}")
    print("-" * 62)
    for name, metrics in results.items():
        print(f"{name:<30} | {metrics['F1-Score']:.4f}   | {metrics['ROC-AUC']:.4f}   | {metrics['Accuracy']:.4f}")
    print("="*50)

if __name__ == "__main__":
    run_classical_baselines()
