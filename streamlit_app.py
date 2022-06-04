import streamlit as st

lista_name = ["Lucas Campos"]
lista_senha = ["lucasomatoria7@gmail.com"]
st.title("Login de inicialização")
name = st.time_input("Digite seu login : ")
senha = st.time_input("Digite sua senha : ")
botao = st.button("Efetue Login")
if botao:
    if (name in lista_name)and(senha in lista_senha):
        st.text("Seja bem vindo!")
    else:
        st.text("Falha no login")
