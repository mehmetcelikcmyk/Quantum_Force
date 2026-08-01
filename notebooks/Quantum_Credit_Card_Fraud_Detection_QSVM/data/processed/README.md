# 📊 İşlenmiş Veri Seti (Processed Data)

Bu klasör, ham kredi kartı dolandırıcılığı verilerinin kuantum makine öğrenmesi (QML) modelinde eğitilmeye uygun hale getirilmiş nihai numpy matrislerini barındırır.

## 📂 Dosya Yapısı ve Boyutları

* **`train_x.npy`:** Eğitim kümesi öznitelik matrisi. (Boyut: `128 x 6`)
* **`train_y.npy`:** Eğitim kümesi etiket matrisi. (Boyut: `128`) - 64 normal (Class 0), 64 sahte (Class 1) işlem içerir.
* **`test_x.npy`:** Test kümesi öznitelik matrisi. (Boyut: `32 x 6`)
* **`test_y.npy`:** Test kümesi etiket matrisi. (Boyut: `32`) - 16 normal (Class 0), 16 sahte (Class 1) işlem içerir.

## ⚙️ Uygulanan Önişleme Adımları

1. **Sınıf Dengeleme (Undersampling):** Ham veri setinde dolandırıcılık oranı %0.17 gibi çok düşük bir düzeydedir. Kuantum simülatöründe modelin sağlıklı öğrenmesi için 80 normal ve 80 dolandırıcılık işlemi rastgele seçilerek toplam 160 örnekten oluşan dengeli bir alt küme oluşturulmuştur.
2. **Standardizasyon (Standardization):** Öznitelikler ortalaması 0 ve varyansı 1 olacak şekilde ölçeklendirilmiştir (`StandardScaler`).
3. **Boyut İndirgeme (PCA):** 30 adet öznitelik (Time, Amount ve V1-V28), kuantum kübit sınırlarına (6 kübit) uyması amacıyla Temel Bileşen Analizi (PCA) ile **6 ana bileşene** indirgenmiştir. Toplam açıklanan varyans oranı yaklaşık **%74.6**'dır.
4. **Eğitim-Test Bölünmesi:** Veriler %80 eğitim, %20 test olmak üzere stratify edilerek bölünmüştür.

## 🚀 Modelde Kullanım

Bu numpy dosyalarını Python kodlarında yüklemek için aşağıdaki şablonu kullanabilirsiniz:

```python
import os
import numpy as np

processed_dir = os.path.join("data", "processed")
X_train = np.load(os.path.join(processed_dir, "train_x.npy"))
y_train = np.load(os.path.join(processed_dir, "train_y.npy"))

print("Eğitim Verisi Yüklendi:", X_train.shape)
```