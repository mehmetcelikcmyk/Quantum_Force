# 🚀 Quantum_CreditRisk_QAE - Kuantum Kredi Risk Değerlemesi

Bu depo, Kuantum Genlik Tahmini (Quantum Amplitude Estimation - QAE) ve klasik makine öğrenmesi yöntemleri kullanarak finansal kredi riskini ve kredi portföylerinin Riske Maruz Değerini (Value-at-Risk - VaR) hesaplamak amacıyla geliştirdiğim projenin kaynak kodlarını ve dokümantasyonunu içermektedir.

## 👤 Geliştirici

*   **Proje Geliştiricisi / Araştırmacı:** Mehmet Çelik

---

## 🎯 Proje Amacı ve Karar Süreci

Geleneksel bankacılık sistemlerinde kredi portföylerinin maruz kalacağı toplam risk ve batık oranı hesaplamaları, milyonlarca simülasyona dayalı klasik Monte Carlo yöntemleriyle yapılmaktadır. Ancak bu işlemler büyük portföyler için saatler sürmekte ve yüksek bilgi işlem maliyeti yaratmaktadır.

Bu projede:
1.  **Klasik Bölüm:** Gerçek **Alman Kredi Veri Seti (German Credit Dataset)** kullanılarak her bir müşterinin temerrüt (default) olasılığı makine öğrenmesi (XGBoost) ile tahmin edilmektedir.
2.  **Kuantum Bölümü:** Elde edilen olasılıklar bir kuantum belirsizlik modeline (uncertainty model) kodlanmaktadır. Qiskit Finance kütüphanesi ve **Iterative Quantum Amplitude Estimation (IQAE)** algoritması kullanılarak kredi portföyünün beklenen kaybı (expected loss) ve Riske Maruz Değeri (VaR) klasik Monte Carlo'ya göre karesel hızlanma (quadratic speedup) ile hesaplanmaktadır.

---

## 📁 Proje Klasör Yapısı

*   `data/` -> Ham ve işlenmiş kredi risk verileri.
*   `docs/` -> Akademik makaleler, referans kaynaklar ve raporlar.
*   `src/` -> Projenin ana kod kütüphanesi (Veri indirme, kuantum motoru ve Streamlit arayüzü).
*   `notebooks/` -> Adım adım veri analizi, model eğitimi ve kuantum devresi denemeleri.

---

## 🛠 Kurulum ve Çalıştırma

Projede kullanılan tüm kuantum ve makine öğrenmesi kütüphanelerini lokal ortamınıza yüklemek için terminale şu komutu yazın:

```bash
pip install -r requirements.txt
```

### 1. Veri İndirme:
İlk olarak gerçek Alman Kredi Veri Setini indirmek için şu scripti çalıştırın:
```bash
python src/data_downloader.py
```

### 2. Arayüzü Başlatma (Streamlit Dashboard):
Kuantum risk simülasyonunu ve analiz grafiklerini görmek için şu komutla Streamlit arayüzünü çalıştırabilirsiniz:
```bash
streamlit run src/app.py
```
