import streamlit as st
from service import Service

class MinhasComprasUI:
    @staticmethod
    def main():
        st.header("Minhas Compras")
        pedidos = Service.minhas_compras(st.session_state["usuario_id"])
        if not pedidos:
            st.info("Você ainda não realizou compras.")
        for p in pedidos:
            with st.expander(f"Pedido {p['id']} - {p['data']} - R$ {p['total']:.2f}"):
                for item in p["itens"]:
                    st.write(f"{item['descricao']} - {item['quantidade']} x R$ {item['preco']:.2f}")
                st.write(f"Total: R$ {p['total']:.2f}")
