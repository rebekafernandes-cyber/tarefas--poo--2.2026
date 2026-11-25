import streamlit as st
from service import Service

class ReajustePrecoUI:
    @staticmethod
    def main():
        st.header("Reajustar preços")
        percentual = st.number_input("Percentual (positivo aumenta, negativo reduz)",
                                     value=0.0, step=1.0)
        if st.button("Aplicar reajuste"):
            Service.produto_reajustar(percentual)
            st.success("Preços atualizados.")
            st.rerun()