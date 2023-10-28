# app.py
import streamlit as st
import pandas as pd
from pydantic import ValidationError
from models import Vendas  # Ajuste o caminho se necessário

def validar_dados(dataframe):
    """
    Valida os dados com base no modelo Pydantic.
    """
    erros = []
    for _, row in dataframe.iterrows():  # Iterando através das linhas do DataFrame
        try:
            # Convertendo a linha do DataFrame para um dicionário e validando
            Vendas(**row.to_dict())
        except ValidationError as e:
            erros.append(e.errors())

    if erros:
        return False, erros  # Retornando os erros se existirem

    return True, "Todos os registros são válidos!"  # Retornando mensagem de sucesso

# Título da aplicação
st.title('Validador de Dados de Vendas')

# Upload do arquivo Excel
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=['xlsx'])

if uploaded_file:
    try:
        # Ler o arquivo Excel com o Pandas
        df = pd.read_excel(uploaded_file, engine='openpyxl', index_col=None)

        # Validação dos dados com o esquema Pydantic
        sucesso, mensagem = validar_dados(df)  # Passando o DataFrame diretamente

        # Exibindo os resultados da validação
        if sucesso:
            st.success(mensagem)  # Aqui usamos a mensagem de retorno da validação
        else:
            st.error("Erro de validação encontrado:")
            for erro in mensagem:  # Iterando sobre cada erro e imprimindo-o
                st.json(erro)  # Mostrando os detalhes do erro

    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

