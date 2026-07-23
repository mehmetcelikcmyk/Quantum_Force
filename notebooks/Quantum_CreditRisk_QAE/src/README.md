# 💻 Src (Source - Ana Kod) Klasörü

Projemizin beyni ve çalışan nihai sistemi burasıdır. `notebooks` klasöründe test edilip onaylanmış, hatasız çalışan fonksiyonlar ve sınıflar (classes) buraya taşınır. Proje sunulurken veya jüri tarafından test edilirken sadece bu klasördeki kodlar çalıştırılacaktır.

## 📁 Modül Yapısı
* `data_preprocessing.py` -> Veriyi alan, temizleyen ve modele hazır hale getiren fonksiyonlar.
* `quantum_model.py` -> Kuantum devrelerinin (Qiskit/Ocean) kurulduğu ve çalıştırıldığı ana kodlar.
* `optimization.py` -> Problemi çözen hibrit veya klasik optimizasyon algoritmaları.
* `app.py` / `main.py` -> Projenin arayüzünü (Streamlit/Gradio) başlatan veya tüm sistemi tek tıkla çalıştıran ana dosya.

## ⚠️ Kesin Kurallar
* **Doğrudan main branch'e push yapmayın!** Bu klasördeki kodları değiştirmek veya yeni kod eklemek için her zaman kendi branch'inizde çalışın ve bir **Pull Request (PR)** açın.
* Yazdığınız fonksiyonların modüler (tekrar kullanılabilir) olmasına ve docstring (fonksiyon açıklaması) içermesine dikkat edin.