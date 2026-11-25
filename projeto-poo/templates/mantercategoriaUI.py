import streamlit as st
import pandas as pd
import time
from service import Service

import streamlit as st
import pandas as pd
from service import Service

class ManterCategoriaUI:
    @staticmethod
    def main():
        st.header("Cadastro de Categorias")
        descricao = st.text_input("Informe a descrição da categoria")
        if st.button("Inserir categoria"):
            if descricao.strip() == "":
                st.error("Informe a descrição.")
            else:
                Service.categoria_inserir(descricao)
                st.success("Categoria inserida com sucesso.")
                st.rerun()
        categorias = Service.categoria_listar()
        if categorias:
            st.subheader("Categorias cadastradas")
            st.dataframe(pd.DataFrame([{"ID":c.get_id(),"Descrição":c.descricao}
                         for c in categorias]), use_container_width=True)
            op = st.selectbox("Categoria para alterar ou excluir",
                              [c.get_id() for c in categorias])
            categoria = Service.categoria_listar_id(op)
            nova = st.text_input("Nova descrição", value=categoria.descricao)
            col1, col2 = st.columns(2)
            if col1.button("Atualizar categoria"):
                if nova.strip():
                    Service.categoria_atualizar(op, nova)
                    st.success("Categoria atualizada.")
                    st.rerun()
            if col2.button("Excluir categoria"):
                if any(p.idCategoria == op for p in Service.produto_listar()):
                    st.error("Não é possível excluir: existem produtos nessa categoria.")
                else:
                    Service.categoria_excluir(op)
                    st.success("Categoria excluída.")
                    st.rerun()
