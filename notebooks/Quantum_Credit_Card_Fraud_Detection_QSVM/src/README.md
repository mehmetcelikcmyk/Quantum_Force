# 💻 Src (Source - Ana Kod) Klasörü

Bu klasör, projenin çalışan tüm kaynak kodlarını ve işlevsel modüllerini barındırır. Modüller, veri indirmeden başlayarak veri ön işleme, klasik referans modellerin eğitimi, kuantum SVM modelinin simülasyonu ve sonuçların dokümantasyonuna kadar olan iş akışını yönetir.

## 📁 Dosya Yapısı ve Görevleri

* **`data_downloader.py`:** Kaggle kredi kartı dolandırıcılık veri kümesini GitHub yedek adreslerinden çeken ve `data/raw/` klasörüne çıkaran betik.
* **`data_preprocessing.py`:** Verideki sınıf dengesizliğini gideren (undersampling) ve verileri 6 kübite uygun hale getirmek amacıyla PCA ile boyut indirgemesi gerçekleştiren modül.
* **`classical_baseline.py`:** Support Vector Machine (RBF), Random Forest ve Gradient Boosting klasik modellerini eğiterek referans metrikleri hesaplayan kod.
* **`qsvm_model.py`:** Qiskit v2.5.0 ile ZZFeatureMap ve FidelityQuantumKernel yapılarını kullanarak kuantum benzerlik matrisini hesaplayan ve Quantum SVM (QSVM) modelini eğiten ana kuantum kodu.
* **`plot_results.py`:** Klasik ve kuantum metriklerini karşılaştırmalı sütun grafiğine dönüştüren çizim kodu.
* **`generate_documents.py`:** Jüri için sunum (PPTX), rapor taslakları (DOCX, PDF) üreten ve görselleri `docs/` klasöründeki yerlerine kopyalayan dokümantasyon otomasyon modülü.

## 🚀 Çalıştırma Sırası

Tüm projeyi sırasıyla çalıştırmak için aşağıdaki komutları kullanabilirsiniz:

```bash
python src/data_downloader.py
python src/data_preprocessing.py
python src/classical_baseline.py
python src/qsvm_model.py
python src/plot_results.py
python src/generate_documents.py
```