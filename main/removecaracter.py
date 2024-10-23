'''with open('models.py', 'r', encoding='utf-8') as file:
    content = file.read()

content = content.replace('\x00', '')  # Remove caracteres nulos

with open('models.py', 'w', encoding='utf-8') as file:
    file.write(content)
'''

import os

# Obtenha o caminho absoluto do diretório atual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Caminho completo para o arquivo models.py
models_file_path = os.path.join(current_directory, 'models.py')

try:
    # Tente abrir o arquivo para leitura usando 'latin-1' para decodificação
    with open(models_file_path, 'r', encoding='latin-1') as file:
        content = file.read()

    # Remova caracteres nulos
    content = content.replace('\x00', '')

    # Reabra o arquivo para escrever o conteúdo modificado
    with open(models_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Caracteres nulos removidos com sucesso do arquivo {models_file_path}")

except FileNotFoundError:
    print(f"Arquivo {models_file_path} não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
