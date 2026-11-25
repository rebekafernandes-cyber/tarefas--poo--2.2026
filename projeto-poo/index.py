from templates.manterclienteUI import ManterClienteUI
from templates.mantercategoriaUI import ManterCategoriaUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.listarprodutoUI import ListarProdutosUI
from templates.carrinhoUI import CarrinhoUI
from templates.minhascomprasUI import MinhasComprasUI
from templates.listarvendasUI import ListarVendasUI
from templates.reajusteUI import ReajustePrecoUI
import streamlit as st
from service import Service

class IndexUI:
    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Clientes", "Categorias", "Produtos", "Reajustar preços", "Listar vendas"
        ])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Categorias": ManterCategoriaUI.main()
        if op == "Produtos": ManterProdutoUI.main()
        if op == "Reajustar preços": ReajustePrecoUI.main()
        if op == "Listar vendas": ListarVendasUI.main()

    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", [
            "Listar produtos", "Visualizar carrinho", "Minhas compras", "Meus dados"
        ])
        if op == "Listar produtos": ListarProdutosUI.main()
        if op == "Visualizar carrinho": CarrinhoUI.main()
        if op == "Minhas compras": MinhasComprasUI.main()
        if op == "Meus dados": PerfilClienteUI.main()

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            for chave in ["usuario_id", "usuario_nome", "usuario_email", "carrinho"]:
                if chave in st.session_state:
                    del st.session_state[chave]
            st.rerun()

    @staticmethod
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    @staticmethod
    def main():
        st.set_page_config(page_title="Comércio", page_icon="🛒", layout="wide")
        Service.cliente_criar_admin()
        st.title("Sistema de Comércio Eletrônico")
        IndexUI.sidebar()
IndexUI.main()
