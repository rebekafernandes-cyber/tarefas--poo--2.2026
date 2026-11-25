import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Cálculos com Retângulos")
        b = st.text_input("Informe a base")
        h = st.text_input("Informe a altura")
        if st.button("Calcular"):
            x = Retangulo(float(b), float(h))
            st.write(x.calc_area())
            st.write(x.calc_diagonal())
            st.write(x)