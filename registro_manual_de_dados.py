
import streamlit as st

st.set_page_config(page_title="Registrar Dados", layout="wide")

st.title("📄 Registro Manual de Dados")
st.write("Preencha os campos abaixo para registrar dados personalizados sobre sua pool.")

plataforma = st.selectbox("Plataforma", ["Orca", "Raydium", "Meteora", "Kamino"])
pool = st.text_input("Pool (ex: SOL/USDC)")
montante = st.number_input("Montante investido (em dólares)", min_value=0.0, format="%.2f")
quantidade_sol = st.number_input("Quantidade de SOL", min_value=0.0)
quantidade_usdc = st.number_input("Quantidade de USDC", min_value=0.0)
data_entrada = st.date_input("Data de entrada")

if st.button("Salvar Dados"):
    st.success("Dados salvos com sucesso!")
