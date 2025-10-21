import streamlit as st
import requests 

API_URL =""

st.set_page_config(page_title="gerenciador de estoques" page_icon="✔")
st.title("gerenciador de estoques")

menu = st.sidebar.radio("navegação", ["catalogo", "gerenciamemto de estoques"])

if menu == "catalogo":
    st.subheader("estoques disponiveis")
    response = requests.get(f"{API_URL}/estoques")
    if response.status_code == 200:
        estoques  = response.json().get("estoques",[])
        if estoques:
            st.dataframe(estoques)
    else:
        st.error("erro ao acessar a API")


elif menu == "adicionar produtos":
    st.subheader()