import streamlit as st
from service import Service

class CarrinhoUI:
    @staticmethod
    def main():
        st.header("Meu Carrinho")
        carrinho = st.session_state.get("carrinho", [])
        if not carrinho:
            st.info("Seu carrinho está vazio.")
            return
        total = 0
        for item in carrinho:
            p = Service.produto_listar_id(item["produto_id"])
            if p == None:
                continue
            subtotal = p.preco * item["quantidade"]
            total += subtotal
            st.write(f"{p.descricao} | {item['quantidade']} x R$ {p.preco:.2f} = R$ {subtotal:.2f}")
        st.subheader(f"Total: R$ {total:.2f}")
        if st.button("Esvaziar carrinho"):
            st.session_state["carrinho"] = []
            st.rerun()
        if st.button("Comprar carrinho"):
            try:
                Service.pedido_comprar(st.session_state["usuario_id"],
                    st.session_state["usuario_nome"], carrinho)
                st.session_state["carrinho"] = []
                st.success("Compra realizada com sucesso!")
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
