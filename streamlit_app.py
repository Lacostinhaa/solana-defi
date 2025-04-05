
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Painel DeFi Solana", layout="wide", initial_sidebar_state="expanded")

st.title("📊 Painel DeFi - Solana com Kamino")
st.markdown("Este é o painel de monitoramento de pools e empréstimos na rede Solana.")

wallet = st.text_input("Digite o endereço da sua carteira Solana")

# Exemplo estático de posição
st.markdown("### 🏦 KAMINO - Empréstimo")
with st.expander("🔽 Ver detalhes do empréstimo"):
    st.write("* Token colateral: SOL")
    st.write("* Valor emprestado: US$ 180.00")
    st.write("* LTV: 52%")
    st.write("* Status: 🟡 Take Care")
    st.write("* Data de entrada: 05/04/2025")
    st.write("* Health Factor: 1.41")

st.markdown("### 📝 Registrar Dados Manuais")
st.write("Clique no botão abaixo para registrar suas informações personalizadas da pool.")

if st.button("➕ Registrar Dados"):
    st.markdown("---")
    st.subheader("📋 Formulário de Registro Manual")

    plataforma = st.selectbox("Plataforma", ["Orca", "Raydium", "Meteora", "Kamino"])
    pool = st.text_input("Pool (ex: SOL/USDC)")
    valor = st.number_input("Valor Investido (em USD)", min_value=0.0, format="%.2f")
    quantidade = st.text_input("Quantidade de Tokens (ex: SOL: 0.2 | USDC: 100)")
    data = st.date_input("Data de Entrada")

    if st.button("Salvar Dados"):
        st.success("✅ Dados registrados com sucesso (exibição simulada abaixo).")
        st.write(f"**Plataforma**: {plataforma}")
        st.write(f"**Pool**: {pool}")
        st.write(f"**Valor investido**: US$ {valor:.2f}")
        st.write(f"**Quantidade**: {quantidade}")
        st.write(f"**Data de entrada**: {data}")

