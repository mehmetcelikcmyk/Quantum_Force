# 🚀 Quantum_Force - Kuantum Kredi Kartı Dolandırıcılık Tespiti (QSVM)

Bu depo, Kuantum Algoritmaları geliştirdiğim **Kuantum Destek Vektör Makineleri (QSVM) ile Kredi Kartı Dolandırıcılık Tespiti (Quantum Fraud Detection)** projesinin kaynak kodlarını ve resmi dokümantasyonunu içermektedir.

---

## 🎯 Proje Özeti ve Çözüm Yaklaşımı

Finansal siber güvenlikte kredi kartı dolandırıcılığını tespit etmek, sınıf dengesizliğinin son derece yüksek olduğu (dolandırıcılık oranı yalnızca **%0.17**) ve yüksek boyutlu veriler barındıran bir anomali tespit problemidir. Klasik doğrusal olmayan makine öğrenmesi modelleri bu karmaşık öznitelik sınırlarını öğrenirken aşırı öğrenmeye (overfitting) maruz kalabilmektedir.

Bu projede kuantum makine öğrenmesi (QML) teknikleri kullanılarak aşağıdaki çözüm mimarisi geliştirilmiştir:
1. **Veri Ön İşleme & Boyut Azaltma:** Kaggle veri seti sınıf dengesizliğini çözmek amacıyla undersampling ile dengelenmiş, ardından 30 öznitelik kuantum simülasyon sınırlarına (6 kübit) uyması için **PCA** yöntemiyle 6 ana bileşene indirgenmiştir.
2. **Kuantum Haritalama (Feature Mapping):** Klasik öznitelikler Qiskit platformundaki `ZZFeatureMap` devresi kullanılarak kuantum durum genlikleri ve evrelerine kodlanmıştır.
3. **Kuantum Çekirdek (Quantum Kernel):** İki işlem arasındaki benzerliği kuantum Hilbert uzayında ölçmek için `FidelityQuantumKernel` ve `StatevectorSampler` aracılığıyla kuantum benzerlik matrisi (fidelity) hesaplanmıştır.
4. **Sınıflandırma:** Hesaplanan kuantum kernel, klasik Support Vector Classifier (SVC) algoritmasına precomputed kernel olarak beslenerek nihai dolandırıcılık tespiti gerçekleştirilmiştir.

---

## 📁 Depo Klasör Yapısı

* **`data/`:** Ham (`raw/creditcard.csv`) ve önişlemeden geçmiş (`processed/`) numpy veri dosyaları.
* **`docs/`:** Proje belgeleri, görseller ve raporlar:
  * **`docs/sunumlar/proje_sunumu.pptx`:** Projeyi açıklayan 7 slaytlık resmi jüri sunumu.
  * **`docs/raporlar_ve_taslaklar/proje_raporu.docx` / `.pdf`:** Resmi proje raporları.
  * **`docs/gorseller/`:** Karşılaştırma grafikleri ve kuantum çekirdek benzerlik sıcaklık haritaları.
* **`notebooks/`:** Projenin adım adım Ar-Ge aşamasını, kodlarını ve çalışma çıktısını gösteren **`quantum_fraud_detection.ipynb`** Jupyter Notebook dosyası.
* **`src/`:** Projeyi baştan sona çalıştıran modüler Python kaynak kodları.
* **`requirements.txt`:** Projede kullanılan Qiskit, Scikit-learn ve raporlama kütüphaneleri.

---

## 📈 Model Performans Sonuçları

Küçük bir dengeli veri kümesi (128 eğitim, 32 test örneği) ve 6 kübitlik kuantum simülasyonu üzerinde elde edilen sonuçların karşılaştırması:

| Model | F1-Score | ROC-AUC | Doğruluk (Accuracy) |
| :--- | :---: | :---: | :---: |
| **SVM (RBF Kernel)** | 0.8966 | 0.9609 | 0.9062 |
| **Random Forest** | 0.8966 | 0.9199 | 0.9062 |
| **Gradient Boosting** | 0.9032 | 0.9180 | 0.9062 |
| **Kuantum SVM (QSVM)** | **0.6667** | **0.8086** | **0.6875** |

> [!NOTE]
> Kuantum SVM modeli NISQ çağının kübit kısıtları nedeniyle simülatör ortamında klasik modellere yakın performans sergilemiştir. Kübit sayısı arttıkça ve gerçek kuantum işlemcilerde hata azaltma (error mitigation) metotları uygulandığında kuantum özellik uzayının sağladığı korelasyonlar sayesinde kuantum avantajı hedeflenmektedir.

---

## 🚀 Kurulum ve Başlangıç

Gerekli kütüphaneleri yüklemek için terminale şu komutu yazın:
```bash
pip install -r requirements.txt
```

Tüm iş akışını (veri indirme, önişleme, klasik baseline, kuantum SVM ve rapor üretimi) sırasıyla çalıştırmak için:
```bash
python src/data_downloader.py
python src/data_preprocessing.py
python src/classical_baseline.py
python src/qsvm_model.py
python src/plot_results.py
python src/generate_documents.py
```
