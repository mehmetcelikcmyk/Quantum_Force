import os
import sys
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Add parent directory and current directory to path to import src modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from src.quantum_risk_engine import QuantumCreditRiskEngine
except ModuleNotFoundError:
    from quantum_risk_engine import QuantumCreditRiskEngine

st.set_page_config(page_title="Kuantum Kredi Risk Analizi", layout="wide")

st.title("⚛️ Kuantum Genlik Tahmini (QAE) ile Kredi Risk Değerleme Platformu")
st.markdown("Bu platform, **Alman Kredi Veri Seti** verileriyle eğitilen klasik bir makine öğrenmesi modeli ile **Kuantum Genlik Tahmini (QAE)** algoritmasını birleştiren bir öğrenci projesidir.")

# Load raw and portfolio data
raw_path = os.path.join("data", "raw", "german_credit_data.csv")
portfolio_path = os.path.join("data", "processed", "predicted_portfolio.csv")

if not os.path.exists(raw_path) or not os.path.exists(portfolio_path):
    st.warning("Lütfen önce verileri indirmek ve modeli eğitmek için `data_downloader.py` ve `train_credit_classifier.py` betiklerini çalıştırın!")
else:
    # Read files
    df_raw = pd.read_csv(raw_path)
    df_portfolio = pd.read_csv(portfolio_path)
    
    # Sidebar
    st.sidebar.header("⚙️ Kuantum Motoru Parametreleri")
    epsilon = st.sidebar.slider("Kuantum Hata Payı (Epsilon)", 0.01, 0.10, 0.05, step=0.01)
    
    st.sidebar.subheader("💰 Kredi Limiti Ayarları")
    l1 = st.sidebar.number_input("Kredi 1 Limiti (TL)", 50000, 500000, 100000, step=10000)
    l2 = st.sidebar.number_input("Kredi 2 Limiti (TL)", 50000, 500000, 250000, step=10000)
    l3 = st.sidebar.number_input("Kredi 3 Limiti (TL)", 50000, 500000, 150000, step=10000)
    
    losses = [l1, l2, l3]
    probabilities = df_portfolio['Default_Probability'].values
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📊 Kredi Portföyü", "⚛️ Kuantum Risk Analizi", "🎓 Proje Hakkında"])
    
    with tab1:
        st.subheader("📋 Analiz Edilen Kredi Portföyü")
        st.markdown("XGBoost sınıflandırma modeli tarafından tahmin edilen bireysel temerrüt olasılıkları:")
        
        display_df = df_portfolio.copy()
        display_df['Loss_Given_Default'] = losses
        display_df.columns = ["Müşteri ID", "Temerrüt Olasılığı (Default Prob)", "Kredi Limiti (TL)"]
        st.dataframe(display_df.style.format({"Temerrüt Olasılığı (Default Prob)": "{:.2%}", "Kredi Limiti (TL)": "{:,.2f} TL"}))
        
        st.markdown("### Veri Kümesinden Örnek Satırlar (İlk 5 Satır):")
        st.dataframe(df_raw.head())
        
    with tab2:
        st.subheader("⚛️ Kuantum Genlik Tahmini (QAE) vs Klasik Monte Carlo")
        
        # Initialize Engine
        engine = QuantumCreditRiskEngine(probabilities=probabilities, losses=losses)
        
        # Calculate
        with st.spinner("Klasik Monte Carlo ve Kuantum QAE hesaplamaları yapılıyor..."):
            mc_results = engine.run_monte_carlo(num_samples=50000)
            qae_results = engine.run_quantum_qae(epsilon=epsilon)
            
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Klasik Beklenen Kayıp (Monte Carlo)", f"{mc_results['expected_loss']:,.2f} TL")
            st.metric("Riske Maruz Değer (VaR %95)", f"{mc_results['var_95']:,.2f} TL")
            st.metric("Koşullu Riske Maruz Değer (CVaR %95)", f"{mc_results['cvar_95']:,.2f} TL")
            
        with col2:
            st.metric("Kuantum Beklenen Kayıp (QAE)", f"{qae_results['expected_loss']:,.2f} TL")
            st.metric("Kuantum Hata Toleransı Sınırı", f"± {epsilon * 100:.1f}%")
            st.info(f"Kuantum Çözüm Tipi:\n{qae_results['quantum_status']}")
            
        # Comparison plot
        st.subheader("📊 Portföy Kayıp Olasılık Yoğunluğu Grafiği")
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.hist(mc_results['portfolio_losses'], bins=15, density=True, alpha=0.6, color='skyblue', edgecolor='black', label="Simüle Edilen Kayıplar")
        ax.axvline(mc_results['expected_loss'], color='red', linestyle='dashed', linewidth=2, label=f"Klasik Beklenen Kayıp ({mc_results['expected_loss']:.0f} TL)")
        ax.axvline(qae_results['expected_loss'], color='green', linestyle='dotted', linewidth=3, label=f"Kuantum Beklenen Kayıp ({qae_results['expected_loss']:.0f} TL)")
        ax.axvline(mc_results['var_95'], color='orange', linestyle='dashed', linewidth=2, label=f"VaR %95 ({mc_results['var_95']:.0f} TL)")
        ax.set_title("Klasik ve Kuantum Yöntemlerle Portföy Risk Dağılımı")
        ax.set_xlabel("Toplam Kayıp (TL)")
        ax.set_ylabel("Sıklık Oranı")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        
    with tab3:
        st.subheader("🎓 Proje Açıklaması ve Kuantum Avantajı")
        st.markdown(r"""
        ### Kuantum Genlik Tahmini (QAE) Nedir?
        Kuantum Genlik Tahmini (Quantum Amplitude Estimation - QAE), bir kuantum durumunun olasılık genliğini tahmin etmek için kullanılan temel bir kuantum algoritmasıdır.
        
        Klasik bilgisayarlarda kredi portföy riskini veya finansal opsiyon fiyatlarını hesaplamak için kullanılan **Monte Carlo Simülasyonu**, hata payını $\epsilon$ seviyesine indirmek için **$N = O(1/\epsilon^2)$** örneklem gerektirir.
        Kuantum QAE algoritması ise genlik yükseltme (amplitude amplification) tekniklerini kullanarak hata payını $\epsilon$ seviyesine indirmek için sadece **$N = O(1/\epsilon)$** kuantum ölçümü yapar.
        
        Bu durum, kuantum bilgisayarların finansal simülasyonlarda klasik sistemlere kıyasla **karesel hızlanma (quadratic speedup)** sunmasını sağlar.
        
        ### Projede Kullanılan Teknolojiler
        *   **XGBoost Classifier:** Alman Kredi Veri Setini kullanarak bireysel müşteri temerrüt olasılıklarını tahmin eder.
        *   **Qiskit Finance (CreditRiskAnalysis):** Kredileri kuantum devrelerine kübit olarak kodlar ve beklenen portföy kaybını QAE devresiyle hesaplar.
        *   **Streamlit:** Platform arayüzü ve görselleştirme için kullanılmıştır.
        """)
