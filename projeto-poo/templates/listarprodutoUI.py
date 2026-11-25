import streamlit as st
from service import Service

class ListarProdutosUI:
    @staticmethod
    def main():
        st.header("Produtos disponíveis")
        produtos = Service.produto_listar()
        if not produtos:
            st.info("Nenhum produto cadastrado.")
        for p in produtos:
            with st.container(border=True):
                st.subheader(p.descricao)
                st.write(f"Preço: R$ {p.preco:.2f}")
                st.write(f"Estoque disponível: {p.estoque}")
                if p.estoque > 0:
                    quantidade = st.number_input("Quantidade", min_value=1,
                        max_value=int(p.estoque), value=1, key=f"qtd_{p.id}")
                    if st.button("Adicionar ao carrinho", key=f"add_{p.id}"):
                        carrinho = st.session_state.get("carrinho", [])
                        encontrado = False
                        for item in carrinho:
                            if item["produto_id"] == p.id:
                                item["quantidade"] += int(quantidade)
                                encontrado = True
                        if not encontrado:
                            carrinho.append({"produto_id":p.id,"quantidade":int(quantidade)})
                        st.session_state["carrinho"] = carrinho
                        st.success("Produto adicionado ao carrinho.")
                        st.rerun()
