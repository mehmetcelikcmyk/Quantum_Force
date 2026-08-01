import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Qiskit imports
from qiskit.circuit.library import ZZFeatureMap
from qiskit.primitives import StatevectorSampler
from qiskit_algorithms.state_fidelities import ComputeUncompute
from qiskit_machine_learning.kernels import FidelityQuantumKernel

def run_qsvm():
    print("=== Training Quantum Support Vector Machine (QSVM) ===")
    
    # Load preprocessed data
    processed_dir = os.path.join("data", "processed")
    try:
        X_train = np.load(os.path.join(processed_dir, "train_x.npy"))
        X_test = np.load(os.path.join(processed_dir, "test_x.npy"))
        y_train = np.load(os.path.join(processed_dir, "train_y.npy"))
        y_test = np.load(os.path.join(processed_dir, "test_y.npy"))
    except FileNotFoundError:
        print("[ERROR] Preprocessed data not found. Please run 'data_preprocessing.py' first.")
        return
        
    num_features = X_train.shape[1]
    print(f"Dataset Loaded. Features (Qubits) count: {num_features}")
    print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")
    
    # 1. Define Quantum Feature Map (ZZFeatureMap is standard for mapping non-linear correlations)
    # We use num_features qubits, 2 repetitions for deeper entanglement
    print("\nDefining Quantum Feature Map (ZZFeatureMap)...")
    feature_map = ZZFeatureMap(feature_dimension=num_features, reps=2, entanglement='linear')
    
    # 2. Initialize Qiskit Sampler primitive and State Fidelity computation
    print("Initializing Qiskit Sampler and ComputeUncompute Fidelity...")
    sampler = StatevectorSampler()
    fidelity = ComputeUncompute(sampler=sampler)
    
    # 3. Create FidelityQuantumKernel
    print("Creating Quantum Kernel...")
    quantum_kernel = FidelityQuantumKernel(fidelity=fidelity, feature_map=feature_map)
    
    # 4. Evaluate Quantum Kernel matrices
    print("Computing Training Quantum Kernel Matrix (this may take a minute)...")
    # train_kernel[i, j] = |<phi(x_i)|phi(x_j)>|^2
    train_matrix = quantum_kernel.evaluate(x_vec=X_train)
    print("Computing Testing Quantum Kernel Matrix...")
    test_matrix = quantum_kernel.evaluate(x_vec=X_test, y_vec=X_train)
    
    # 5. Save the kernel matrices for visualization/later use
    os.makedirs("results", exist_ok=True)
    np.save(os.path.join("results", "qsvm_train_kernel.npy"), train_matrix)
    print("Saved quantum kernel matrices to 'results/' directory.")
    
    # 6. Train classical SVM using the precomputed quantum kernel
    print("\nTraining classical SVM with Quantum Kernel...")
    qsvm = SVC(kernel='precomputed', probability=True, random_state=42)
    qsvm.fit(train_matrix, y_train)
    
    # 7. Predict and Evaluate
    print("Evaluating QSVM model...")
    y_pred = qsvm.predict(test_matrix)
    y_prob = qsvm.predict_proba(test_matrix)[:, 1]
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)
    
    print("\n" + "="*50)
    print("QUANTUM SVM (QSVM) PERFORMANCE")
    print("="*50)
    print(f"  Accuracy:  {acc:.4f}")
    print(f"  Precision: {prec:.4f}")
    print(f"  Recall:    {rec:.4f}")
    print(f"  F1-Score:  {f1:.4f}")
    print(f"  ROC-AUC:   {auc:.4f}")
    print("="*50)

    # Print sample predictions to show "Suspicious / Normal" (Supheli / Guvenli)
    print("\nOrnek Test Islemleri Tahmin Sonuclari (Ilk 10 Islem):")
    print("-" * 65)
    print(f"{'Islem No':<10} | {'Gercek Durum':<18} | {'QSVM Tahmini':<18} | {'Sonuc':<8}")
    print("-" * 65)
    for i in range(min(10, len(y_test))):
        real_status = "SUPHELI (Fraud)" if y_test[i] == 1 else "GUVENLI (Normal)"
        pred_status = "SUPHELI (Fraud)" if y_pred[i] == 1 else "GUVENLI (Normal)"
        result = "DOGRU" if y_test[i] == y_pred[i] else "YANLIS"
        print(f"Islem {i+1:<5} | {real_status:<18} | {pred_status:<18} | {result:<8}")
    print("-" * 65)
    
    # 8. Plot and save the Quantum Kernel Matrix Heatmap
    print("\nPlotting Quantum Kernel Matrix Heatmap...")
    plt.figure(figsize=(8, 6))
    sns.heatmap(train_matrix[:50, :50], cmap='viridis', cbar=True)
    plt.title("Quantum Kernel Matrix (First 50x50 samples)")
    plt.xlabel("Sample Index")
    plt.ylabel("Sample Index")
    plt.tight_layout()
    plot_path = os.path.join("results", "quantum_kernel_heatmap.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved heatmap to '{plot_path}'")
    
    # Save metrics to a text file for walkthrough/reporting
    with open(os.path.join("results", "qsvm_metrics.txt"), "w") as f:
        f.write(f"Accuracy: {acc:.4f}\n")
        f.write(f"Precision: {prec:.4f}\n")
        f.write(f"Recall: {rec:.4f}\n")
        f.write(f"F1-Score: {f1:.4f}\n")
        f.write(f"ROC-AUC: {auc:.4f}\n")

if __name__ == "__main__":
    run_qsvm()
