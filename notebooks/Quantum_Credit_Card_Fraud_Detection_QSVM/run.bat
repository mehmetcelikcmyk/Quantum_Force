@echo off
echo ===================================================
echo   Quantum Fraud Detection QSVM Baslatiliyor...
echo ===================================================

:: Sanal ortam kontrolu ve olusturulmasi
if exist .venv\Scripts\activate.bat goto :activate_venv

if exist .venv (
    echo [WARNING] Sanal ortam venv klasoru mevcut ancak eksik veya bozuk. Yeniden olusturuluyor...
    rd /s /q .venv
)

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
:: Veri Kontrolu ve Indirilmesi
if not exist data\raw\creditcard.csv (
    echo [INFO] Veri seti indiriliyor...
    python src/data_downloader.py
) else (
    echo [OK] Ham veri seti zaten mevcut.
)

:: Preprocessing Kontrolu
if not exist data\processed\train_x.npy (
    echo [INFO] Veri on isleme PCA yapiliyor...
    python src/data_preprocessing.py
) else (
    echo [OK] Preprocessed veri zaten mevcut.
)

:: Model Calistirma Secenekleri
echo.
echo ===================================================
echo   Modelleri ve Analiz Adimlarini Calistir
echo ===================================================
echo [1] Klasik Baseline Modellerini Calistir (classical_baseline.py)
echo [2] Kuantum SVM Modelini Calistir (qsvm_model.py)
echo [3] Sonuclari Gorsellestir (plot_results.py)
echo [4] Rapor ve Dokumanlari Uret (generate_documents.py)
echo [5] Tum Adimlari Sirayla Calistir
echo [6] Cikis
echo ===================================================
set /p secim="Lutfen yapmak istediginiz islemi secin (1-6): "

if "%secim%"=="1" goto :run_classical
if "%secim%"=="2" goto :run_qsvm
if "%secim%"=="3" goto :run_plot
if "%secim%"=="4" goto :run_generate
if "%secim%"=="5" goto :run_all
if "%secim%"=="6" goto :eof
echo Gecersiz secim yapildi!
goto :check_data

:run_classical
echo [INFO] Klasik baseline modelleri calistiriliyor...
python src/classical_baseline.py
pause
goto :check_data

:run_qsvm
echo [INFO] Kuantum SVM modeli calistiriliyor...
python src/qsvm_model.py
pause
goto :check_data

:run_plot
echo [INFO] Sonuclar gorsellestiriliyor...
python src/plot_results.py
pause
goto :check_data

:run_generate
echo [INFO] Rapor ve dokumanlar uretiliyor...
python src/generate_documents.py
pause
goto :check_data

:run_all
echo [INFO] Tum adimlar sirayla calistiriliyor...
echo [1/4] Klasik baseline modelleri calistiriliyor...
python src/classical_baseline.py
echo.
echo [2/4] Kuantum SVM modeli calistiriliyor...
python src/qsvm_model.py
echo.
echo [3/4] Sonuclar gorsellestiriliyor...
python src/plot_results.py
echo.
echo [4/4] Rapor ve dokumanlar uretiliyor...
python src/generate_documents.py
echo [OK] Tum adimlar tamamlandi.
pause
goto :check_data
