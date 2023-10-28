# app.py
import streamlit as st
import pandas as pd
from pydantic import ValidationError
from models import Vendas  # Ajuste o caminho se necessário
import json

def validar_dados(dados):
    """
    Valida os dados com base no modelo Pydantic.
    """
    erros = []
    for item in dados:  # Validando cada registro individualmente
        try:
            Vendas(**item)  # Se os dados forem inválidos, isso levantará uma ValidationError
        except ValidationError as e:
            erros.append(e.errors())  # Coletando os erros para cada item inválido

    if erros:
        return False, erros  # Se houver algum erro, retorne False junto com os erros coletados
    return True, "Todos os registros são válidos!"

# Título da aplicação
st.title('Validador de Dados de Vendas')

# Upload do arquivo Excel
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=['xlsx'])

if uploaded_file:
    try:
        # Ler o arquivo Excel com o Pandas
        df = pd.read_excel(uploaded_file, engine='openpyxl')

        # Converter o DataFrame em JSON e depois de volta para garantir um formato de dicionário adequado
        json_str = df.to_json(orient='records')
        dados = json.loads(json_str)

        # Validação dos dados com o esquema Pydantic
        sucesso, mensagem = validar_dados(dados)

        # Exibindo os resultados da validação
        if sucesso:
            st.success(mensagem)
        else:
            st.error("Erro de validação encontrado:")
            st.json(mensagem)  # Para mostrar os erros de validação em formato JSON

    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
