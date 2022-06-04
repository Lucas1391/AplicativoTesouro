import streamlit as st

lista_name = ["Lucas Campos"]
lista_senha = ["lucasomatoria7@gmail.com"]
st.title("Login de inicialização")
usuario = st.text_input("Insira seu nome de usuário : ")
senha = st.text_input("Insira sua senha : ",type='password')
if senha:
    if (usuario  not in lista_name)and(senha not in lista_senha):
        st.text("Falha no Login!")
    else:
        st.text("Seja bem vindo!")
