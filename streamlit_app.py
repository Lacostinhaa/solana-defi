import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Painel DeFi Solana", layout="wide")

st.title("📊 Painel DeFi - Solana com Kamino")
st.markdown("Este é o painel de monitoramento de pools e empréstimos na rede Solana.")

wallet = st.text_input("Digite o endereço da sua carteira Solana")

# Exemplo estático de posição
st.markdown("### KAMINO - Empréstimo")
with st.expander("🔽 Ver detalhes do empréstimo"):
    st.write("• Token colateral: SOL")
    st.write("• Valor emprestado: US$ 180.00")
    st.write("• LTV: 52%")
    st.write("• Status: 🟡 Take Care")
    st.write("• Data de entrada: 05/04/2025")
    st.write("• Health Factor: 1.41")
if st.button("➕ Registrar Dados"):
    st.switch_page("pages/registro_de_dados.py")
st.markdown("### 📝 Registrar Dados Manuais")
st.write("Clique no botão abaixo para registrar suas informações personalizadas da pool.")
st.info("Acesse a página **📋 Registro Manual de Dados** no menu lateral para adicionar suas informações personalizadas.")

  
