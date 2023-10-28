# Importar bibliotecas
from pathlib import Path
import shutil

# Definindo os caminhos utilizando pathlib
BASE_DIR = Path(__file__).resolve().parent
CAMINHO_ENTRADA = BASE_DIR / "../data/input"
CAMINHO_VALIDOS = BASE_DIR / "../data/output_validos"

# Criar uma função para mover os arquivos
def mover_arquivo(caminho_arquivo, destino):
    """
    Move o arquivo para o diretório correspondente.
    """
    shutil.move(str(caminho_arquivo), destino / caminho_arquivo.name)

# Criar função principal
def main():
    arquivos_json = CAMINHO_ENTRADA.glob('*.json')

    for arquivo in arquivos_json:
        mover_arquivo(arquivo, CAMINHO_VALIDOS)

    # Logando a mensagem final com base se houve erro ou não
    status_final = "com sucesso"
    print(f"Pipeline finalizada {status_final}.")

if __name__ == "__main__":
    main()