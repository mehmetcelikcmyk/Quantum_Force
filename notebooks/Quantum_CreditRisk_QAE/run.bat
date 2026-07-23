@echo off
echo ===================================================
echo   Quantum Credit Risk QAE Baslatiliyor...
echo ===================================================

:: Sanal ortam kontrolu ve olusturulmasi
if exist .venv goto :activate_venv

echo [INFO] Sanal ortam bulunamadi. Yeni bir sanal ortam olusturuluyor...
python -m venv .venv
if errorlevel 1 (
    echo [WARNING] Sanal ortam olusturulamadi, sistem Python'i kullanilacak.
    goto :check_data
)

echo [OK] Sanal ortam olusturuldu. Gerekli paketler yukleniyor...
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
goto :check_data

:activate_venv
echo [OK] Sanal ortam venv mevcut. Aktiflestiriliyor...
call .venv\Scripts\activate.bat
goto :check_data

:check_data
:: Veri ve Model Kontrolu
if not exist data\raw\german_credit_data.csv (
    echo [INFO] Veri seti indiriliyor...
    python src/data_downloader.py
) else (
    echo [OK] Veri seti zaten mevcut.
)

if not exist data\processed\predicted_portfolio.csv (
    echo [INFO] Model egitiliyor ve portfoy olusturuluyor...
    python src/train_credit_classifier.py
) else (
    echo [OK] Egitilmis model ve portfoy zaten mevcut.
)

echo.
echo [INFO] Streamlit uygulamasi baslatiliyor...
streamlit run src/app.py

pause
