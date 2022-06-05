import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    usuario = st.text_input("Insira seu nome de usuário : ")
    senha = st.text_input("Insira sua senha : ",type='password')
    if senha:
        if (usuario  not in lista_name)and(senha not in lista_senha):
            st.text("Falha no Login!")
    else:
        st.text("Seja bem vindo!")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

page_names_to_funcs = {
    "": ""
    "Main Page": main_page(),
    "Home": page2(),

}
lista_name = ["Lucas Campos"]
lista_senha = ["lucasomatoria7@gmail.com"]


selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

        
