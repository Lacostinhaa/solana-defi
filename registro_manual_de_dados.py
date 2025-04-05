
import streamlit as st

st.set_page_config(
    page_title="Registro Manual de Dados",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("📄 Registro Manual de Dados")
st.write("Preencha os dados abaixo para registrar manualmente sua pool de liquidez:")

with st.form("formulario_manual"):
    plataforma = st.selectbox("Plataforma", ["Orca", "Raydium", "Meteora", "Kamino"])
    pool = st.text_input("Pool (ex: SOL/USDC)")
    montante = st.number_input("Montante investido (US$)", min_value=0.0, step=0.01)
    quantidade_sol = st.text_input("Quantidade de tokens (ex: 0.2 SOL / 100 USDC)")
    data_entrada = st.date_input("Data de entrada na pool")

    enviado = st.form_submit_button("Salvar dados")
    if enviado:
        st.success("✅ Dados registrados com sucesso!")
        st.write(f"**Plataforma:** {plataforma}")
        st.write(f"**Pool:** {pool}")
        st.write(f"**Montante:** US$ {montante}")
        st.write(f"**Tokens:** {quantidade_sol}")
        st.write(f"**Data de entrada:** {data_entrada}")
