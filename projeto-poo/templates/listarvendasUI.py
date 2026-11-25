import streamlit as st
import pandas as pd
from service import Service

class ListarVendasUI:
    @staticmethod
    def main():
        st.header("Vendas realizadas")
        pedidos = Service.listar_vendas()
        if not pedidos:
            st.info("Nenhuma venda realizada.")
        else:
            dados = [{"Pedido":p["id"],"Cliente":p["cliente_nome"],
                      "Data":p["data"],"Total":p["total"]} for p in pedidos]
            st.dataframe(pd.DataFrame(dados), use_container_width=True)
            for p in pedidos:
                with st.expander(f"Detalhes do pedido #{p['id']}"):
                    for item in p["itens"]:
                        st.write(f"{item['descricao']} - {item['quantidade']} x R$ {item['preco']:.2f}")