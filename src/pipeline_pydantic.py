# src/pipeline.py
from pathlib import Path
import shutil
from models import Vendas
from pydantic import ValidationError
import json

# Definindo os caminhos utilizando pathlib
BASE_DIR = Path(__file__).resolve().parent
CAMINHO_ENTRADA = BASE_DIR / "../data/input"
CAMINHO_VALIDOS = BASE_DIR / "../data/output_validos"
CAMINHO_INVALIDOS = BASE_DIR / "../data/output_invalidos"

def validar_json(caminho_arquivo):
    """
    Valida o arquivo com base no schema.
    """
    try:
        data = json.loads(caminho_arquivo.read_text(encoding='utf-8'))
        Vendas.model_validate(data)
        return CAMINHO_VALIDOS
    except ValidationError as e:
        print(f"Erro de validação: {e}")
        return CAMINHO_INVALIDOS

def mover_arquivo(caminho_arquivo, destino):
    """
    Move o arquivo para o diretório correspondente.
    """
    shutil.move(str(caminho_arquivo), destino / caminho_arquivo.name)

def main():
    arquivos_json = CAMINHO_ENTRADA.glob('*.json')
    houve_erro = False

    for arquivo in arquivos_json:
        valido = validar_json(arquivo)
        if not valido:
            houve_erro = True
        mover_arquivo(arquivo, valido)

    # Logando a mensagem final com base se houve erro ou não
    status_final = "com sucesso" if houve_erro else "com erros"
    print(f"Pipeline finalizada {status_final}.")

if __name__ == "__main__":
    main()