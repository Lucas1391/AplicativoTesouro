import streamlit as st

lista_name = ["Lucas Campos"]
lista_senha = ["lucasomatoria7@gmail.com"]
st.title("Login de inicialização")
name = st.text_input("Digite seu login : ")
senha = st.text_input("Digite sua senha : ")
st.button("Efetue Login")
if st.button("Efetue Login"):
    if (name in lista_name) and( senha in lista_senha):
        st.text("Seja bem vindo!")
    elif:
        st.text("Falha no login")
