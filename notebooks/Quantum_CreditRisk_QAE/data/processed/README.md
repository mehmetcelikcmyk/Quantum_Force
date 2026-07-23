# 📊 Processed (İşlenmiş) Veri Klasörü

Bu klasör, ham veri setinin temizlenmesi ve klasik makine öğrenmesi modeli tarafından işlenmesi sonucu elde edilen ve kuantum simülatörüne doğrudan beslenebilecek nihai dosyaları içerir.

## 📁 Üretilen Dosyalar

1.  **[predicted_portfolio.csv](file:///c:/Users/mehme/OneDrive/Desktop/Quantum_Force/data/processed/predicted_portfolio.csv)**
    *   **Açıklama:** XGBoost modeli ile eğitilerek Alman Kredi Veri Seti test kümesinden seçilen 3 adet kredi için temerrüt olasılıkları (`Default_Probability`) ve atanan kredi limitleri (`Loss_Given_Default`).
    *   **Sütunlar:**
        *   `Client_ID`: Müşterinin veri setindeki benzersiz numarası.
        *   `Default_Probability`: Model tarafından tahmin edilen kredi temerrüt olasılığı ($p_i$).
        *   `Loss_Given_Default`: Müşterinin kredi riski miktarı (TL cinsinden kayıp).