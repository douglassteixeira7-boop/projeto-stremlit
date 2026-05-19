import streamlit as st
st.title("Sistema de Chamados")

#Criar a lista de chamados
if "chamados" not in st.session_state:
    st.session_state.chamados = []
#Abrir chamado
st.subheader("Abrir Chamado")
titulo=st.text_input("Título do Chamado")
descricao=st.text_area("Descrição de serviço")

#Botão
if st.button("Abrir chamado"):
    if titulo != "" and descricao != "":
        chamado = {
            "titulo": titulo,
            "descricao":descricao,
            "status": "Aberto"
        }
        st.session_state.chamados.append(chamado)
        st.success("Chamado aberto com Sucesso")

st.subheader("Listas de chamados")
if len(st.session_state.chamados) ==0 :
    st.warning("Nenhum chamado aberto")
else:
    for i,chamado in enumerate(st.session_state.chamados):
        st.write(f"{chamado['titulo']}")
        st.write(f"Descrição:{chamado['descricao']}")
        st.write(f"Status:{chamado['status']}")
#Alterar status
        novo_status = st.selectbox(
            "Alterar Status",
            ["Aberto","Em andamento", "Finalizando"],
            key= f"status{i}"
)

#Botão para alterar
        if st.button("Atualizar Status", key=f"btn{i}"):
            st.session_state.chamados[i]["status"] = novo_status
            st.success("Status Atualizado!")
            st.rerun()
    st.divider()