# app.py
import streamlit as st
import pandas as pd
from pydantic import ValidationError
from models import Vendas  # Ajuste o caminho se necessário

def validar_dados(dados):
    """
    Valida os dados com base no modelo Pydantic.
    """
    erros = []
    for item in dados.itertuples():  # Iterando diretamente pelos registros do DataFrame
        try:
            # Convertendo o registro do DataFrame para um dicionário e validando
            Vendas(**item._asdict())
        except ValidationError as e:
            erros.append(e.errors())

    if erros:
        return False, erros
    return True, "Todos os registros são válidos!"

# Título da aplicação
st.title('Validador de Dados de Vendas')

# Upload do arquivo Excel
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=['xlsx'])

if uploaded_file:
    try:
        # Ler o arquivo Excel com o Pandas
        df = pd.read_excel(uploaded_file, engine='openpyxl')

        # Validação dos dados com o esquema Pydantic
        sucesso, mensagem = validar_dados(df)  # Passando o DataFrame diretamente

        # Exibindo os resultados da validação
        if sucesso:
            st.success(mensagem)
        else:
            st.error("Erro de validação encontrado:")
            st.json(mensagem)  # Para mostrar os erros de validação em formato JSON

    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
