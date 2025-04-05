
import streamlit as st

st.set_page_config(
    page_title="Painel DeFi Solana",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos customizados
st.markdown("""
    <style>
        body {
            background-color: #0d1b2a;
            color: white;
        }
        .main {
            background-color: #0d1b2a;
        }
        .stButton > button {
            background-color: #1b263b;
            color: white;
            border-radius: 5px;
            padding: 0.5em 1em;
        }
        .stSelectbox, .stTextInput, .stNumberInput, .stDateInput {
            background-color: #1b263b !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌊 Painel DeFi - Solana")

st.sidebar.title("🔗 Navegação")
pagina = st.sidebar.radio("Ir para:", ["🏠 Visão Geral", "💧 Pools", "🏦 Empréstimos", "📝 Registro Manual"])

if pagina == "🏠 Visão Geral":
    st.header("📊 Visão Geral da Carteira")
    st.write("Aqui você verá um resumo das suas posições, ganhos e saúde geral das interações DeFi.")
    st.info("✅ Layout com fundo azul marinho ativo!")

elif pagina == "💧 Pools":
    st.header("💧 Pools de Liquidez")
    st.write("Informações sobre suas posições em pools na Orca, Raydium e Meteora.")
    st.warning("Ainda em construção.")

elif pagina == "🏦 Empréstimos":
    st.header("🏦 Empréstimos - Kamino")
    st.write("Dados em tempo real sobre empréstimos ativos.")
    st.warning("Integração com Kamino em andamento.")

elif pagina == "📝 Registro Manual":
    st.header("📝 Registro Manual de Dados")
    with st.form("registro_manual"):
        plataforma = st.selectbox("Plataforma", ["Orca", "Raydium", "Meteora", "Kamino"])
        pool = st.text_input("Pool (ex: SOL/USDC)")
        valor = st.number_input("Valor investido (USD)", min_value=0.0)
        quantidade = st.text_input("Quantidade de Tokens")
        data = st.date_input("Data de entrada")
        enviar = st.form_submit_button("Salvar")
        if enviar:
            st.success("✅ Dados salvos (simulação)")
            st.write(f"**Plataforma:** {plataforma}")
            st.write(f"**Pool:** {pool}")
            st.write(f"**Valor:** ${valor}")
            st.write(f"**Quantidade:** {quantidade}")
            st.write(f"**Data:** {data}")
