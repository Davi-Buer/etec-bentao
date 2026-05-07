#!/usr/bin/env python3
"""
Script para fazer upload de arquivos para o Azure Storage Account.

Uso:
    python upload_file.py meu-arquivo.txt
    python upload_file.py foto.jpg
"""

import os
import sys
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Carrega as variáveis do arquivo .env
load_dotenv()

def upload_file(file_path):
    """
    Faz upload de um arquivo para o Azure Storage.

    Args:
        file_path: Caminho do arquivo local que será enviado
    """

    # Pega a connection string do arquivo .env
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("CONTAINER_NAME", "documentos")

    # Verifica se a connection string foi configurada
    if not connection_string or connection_string == "sua-connection-string-aqui":
        print("❌ ERRO: Configure sua AZURE_STORAGE_CONNECTION_STRING no arquivo .env")
        print("   Copie a connection string do Portal Azure > Storage Account > Access keys")
        sys.exit(1)

    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        print(f"❌ ERRO: Arquivo '{file_path}' não encontrado!")
        sys.exit(1)

    # Pega apenas o nome do arquivo (sem o caminho completo)
    blob_name = os.path.basename(file_path)

    try:
        print(f"📤 Fazendo upload de '{file_path}'...")

        # Conecta ao Azure Storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Pega o container
        container_client = blob_service_client.get_container_client(container_name)

        # Cria um blob client (representa o arquivo na nuvem)
        blob_client = container_client.get_blob_client(blob_name)

        # Faz o upload do arquivo
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        # Pega o tamanho do arquivo
        file_size = os.path.getsize(file_path)
        file_size_mb = file_size / (1024 * 1024)

        print(f"✅ Upload concluído com sucesso!")
        print(f"   📁 Container: {container_name}")
        print(f"   📄 Nome no Azure: {blob_name}")
        print(f"   💾 Tamanho: {file_size_mb:.2f} MB ({file_size:,} bytes)")

    except Exception as e:
        print(f"❌ ERRO durante o upload: {e}")
        print("\n💡 Dicas:")
        print("   - Verifique se a connection string está correta no .env")
        print(f"   - Verifique se o container '{container_name}' existe")
        print("   - Crie o container no Portal Azure ou use create_container.py")
        sys.exit(1)

if __name__ == "__main__":
    # Verifica se o usuário passou o nome do arquivo
    if len(sys.argv) < 2:
        print("❌ Uso: python upload_file.py <arquivo>")
        print("\nExemplos:")
        print("  python upload_file.py documento.pdf")
        print("  python upload_file.py foto.jpg")
        print("  python upload_file.py relatorio.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    upload_file(file_path)
