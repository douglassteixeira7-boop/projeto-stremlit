import streamlit as st
import random 

#sidebar
st.sidebar.title("Menu")

pagina = st.sidebar.selectbox(
    "Escolha uma página",
    ["Home", "Gráfico"]
)

#Home
if pagina == "Home":

    st.title("Página Home")

    st.write("Sistema usando o Streamlit")

    #input
    nome=st.text_input("Digite seu nome")

    #selectbox
    curso = st.selectbox(
        "Escolha um curso",
        ["Python", "JS", "Banco de dados", "Java"]
    )

    #slider
    nota = st.slider(
        "Escolha a sua nota",
        0,
        10,
        5
    )

    #checkbox
    mostrar = st.checkbox("Mostrar Mensagem")

    if mostrar:
        st.success("Checkbox marcado")
    
    #botão
    if st.button("Enviar"):
        st.write(f"Nome : {nome}")
        st.write(f"Curso : {curso}")
        st.write(f"Nota : {nota}")

    st.subheader("Colunas")
    col1, col2 = st.columns(2)

    with col1:
        st.info("Informações coluna 1")

    with col2:
        st.warning("Informações coluna 2")

elif pagina == "Gráfico":
    st.title("Página de Gráfico")
    valores = []
    for i in range(5):
        valores.append(random.randint(1,100))
    st.bar_chart(valores)