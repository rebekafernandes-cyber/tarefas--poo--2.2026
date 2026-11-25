import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProdutoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Produtos")
        categorias = Service.categoria_listar()
        if not categorias:
            st.warning("Cadastre uma categoria antes de inserir produtos.")
            return
        with st.form("produto_form"):
            descricao = st.text_input("Informe a descrição do produto")
            preco = st.number_input("Informe o preço", min_value=0.01, step=1.0)
            estoque = st.number_input("Informe o estoque", min_value=0, step=1)
            categoria = st.selectbox("Categoria", categorias,
                                     format_func=lambda c: c.descricao)
            inserir = st.form_submit_button("Inserir")
        if inserir:
            if descricao.strip():
                Service.produto_inserir(descricao, preco, int(estoque), categoria.get_id())
                st.success("Produto inserido com sucesso.")
                st.rerun()
            else:
                st.error("Informe a descrição.")
        produtos = Service.produto_listar()
        if produtos:
            st.subheader("Produtos cadastrados")
            st.dataframe(pd.DataFrame([{"ID":p.id,"Descrição":p.descricao,
                         "Preço":p.preco,"Estoque":p.estoque,
                         "Categoria":p.idCategoria} for p in produtos]),
                         use_container_width=True)
            op = st.selectbox("Produto para alterar ou excluir", [p.id for p in produtos])
            p = Service.produto_listar_id(op)
            nova_desc = st.text_input("Descrição", value=p.descricao)
            novo_preco = st.number_input("Preço", min_value=0.01, value=float(p.preco), step=1.0)
            novo_estoque = st.number_input("Estoque", min_value=0, value=int(p.estoque), step=1)
            nova_cat = st.selectbox("Categoria do produto", categorias,
                         index=next((i for i,c in enumerate(categorias) if c.get_id()==p.idCategoria),0),
                         format_func=lambda c: c.descricao)
            c1,c2 = st.columns(2)
            if c1.button("Atualizar produto"):
                Service.produto_atualizar(op,nova_desc,novo_preco,int(novo_estoque),nova_cat.get_id())
                st.success("Produto atualizado.")
                st.rerun()
            if c2.button("Excluir produto"):
                Service.produto_excluir(op)
                st.success("Produto excluído.")
                st.rerun()
