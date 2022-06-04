import streamlit as st

lista_name = ["Lucas Campos"]
lista_senha = ["lucasomatoria7@gmail.com"]
st.title("Login de inicialização")
usuario = st.sidebar.text_input("Insira seu nome de usuário : ")
senha = st.sidebar.text_input("Insira sua senha : ",type='password')
if senha:
    if (usuario in lista_name)and( senha in lista_senha):
        st.text("Seja bem vindo!")
    else:
        st.text("Falha no login")
