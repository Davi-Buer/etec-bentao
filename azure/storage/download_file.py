#!/usr/bin/env python3
"""
Script para baixar arquivos do Azure Storage Account.

Uso:
    python download_file.py arquivo.txt
    python download_file.py foto.jpg
"""

import os
import sys
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Carrega as variáveis do arquivo .env
load_dotenv()

def download_file(blob_name, local_path=None):
    """
    Baixa um arquivo do Azure Storage.

    Args:
        blob_name: Nome do arquivo no Azure
        local_path: Onde salvar localmente (se não informado, usa o mesmo nome)
    """

    # Pega a connection string do arquivo .env
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("CONTAINER_NAME", "documentos")

    # Verifica se a connection string foi configurada
    if not connection_string or connection_string == "sua-connection-string-aqui":
        print("❌ ERRO: Configure sua AZURE_STORAGE_CONNECTION_STRING no arquivo .env")
        print("   Copie a connection string do Portal Azure > Storage Account > Access keys")
        sys.exit(1)

    # Se não foi informado onde salvar, usa o mesmo nome do arquivo
    if not local_path:
        local_path = blob_name

    try:
        print(f"📥 Baixando '{blob_name}' do Azure...")

        # Conecta ao Azure Storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Pega o container
        container_client = blob_service_client.get_container_client(container_name)

        # Pega o blob client
        blob_client = container_client.get_blob_client(blob_name)

        # Baixa o arquivo
        with open(local_path, "wb") as download_file:
            download_data = blob_client.download_blob()
            download_file.write(download_data.readall())

        # Pega o tamanho do arquivo baixado
        file_size = os.path.getsize(local_path)
        file_size_mb = file_size / (1024 * 1024)

        print(f"✅ Download concluído com sucesso!")
        print(f"   📁 Container: {container_name}")
        print(f"   📄 Nome no Azure: {blob_name}")
        print(f"   💾 Salvo em: {local_path}")
        print(f"   📦 Tamanho: {file_size_mb:.2f} MB ({file_size:,} bytes)")

    except Exception as e:
        print(f"❌ ERRO durante o download: {e}")
        print("\n💡 Dicas:")
        print("   - Verifique se a connection string está correta no .env")
        print(f"   - Verifique se o container '{container_name}' existe")
        print(f"   - Verifique se o arquivo '{blob_name}' existe no container")
        print("   - Use list_files.py para ver os arquivos disponíveis")
        sys.exit(1)

if __name__ == "__main__":
    # Verifica se o usuário passou o nome do arquivo
    if len(sys.argv) < 2:
        print("❌ Uso: python download_file.py <nome-do-arquivo> [caminho-local]")
        print("\nExemplos:")
        print("  python download_file.py documento.pdf")
        print("  python download_file.py foto.jpg ./downloads/foto.jpg")
        print("  python download_file.py relatorio.txt")
        sys.exit(1)

    blob_name = sys.argv[1]
    local_path = sys.argv[2] if len(sys.argv) > 2 else None
    download_file(blob_name, local_path)
