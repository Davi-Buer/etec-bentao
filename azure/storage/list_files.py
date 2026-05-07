#!/usr/bin/env python3
"""
Script para listar todos os arquivos de um container no Azure Storage.

Uso:
    python list_files.py
    python list_files.py imagens
"""

import os
import sys
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
from datetime import datetime

# Carrega as variáveis do arquivo .env
load_dotenv()

def format_size(bytes):
    """
    Converte bytes para formato legível (KB, MB, GB).

    Args:
        bytes: Tamanho em bytes

    Returns:
        String formatada (ex: "1.5 MB")
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} TB"

def list_files(container_name=None):
    """
    Lista todos os arquivos de um container.

    Args:
        container_name: Nome do container (se não informado, usa o do .env)
    """

    # Pega a connection string do arquivo .env
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    if not container_name:
        container_name = os.getenv("CONTAINER_NAME", "documentos")

    # Verifica se a connection string foi configurada
    if not connection_string or connection_string == "sua-connection-string-aqui":
        print("❌ ERRO: Configure sua AZURE_STORAGE_CONNECTION_STRING no arquivo .env")
        print("   Copie a connection string do Portal Azure > Storage Account > Access keys")
        sys.exit(1)

    try:
        print(f"📂 Listando arquivos do container '{container_name}'...\n")

        # Conecta ao Azure Storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Pega o container
        container_client = blob_service_client.get_container_client(container_name)

        # Lista todos os blobs (arquivos)
        blobs = container_client.list_blobs()

        # Converte para lista para poder contar
        blob_list = list(blobs)

        if not blob_list:
            print("📭 Container vazio! Nenhum arquivo encontrado.")
            print(f"\n💡 Faça upload de arquivos com:")
            print(f"   python upload_file.py seu-arquivo.txt")
            return

        # Cabeçalho da tabela
        print(f"{'Nome':<40} {'Tamanho':<15} {'Última modificação':<20}")
        print("-" * 75)

        total_size = 0

        # Mostra cada arquivo
        for blob in blob_list:
            # Pega propriedades do blob
            name = blob.name
            size = blob.size
            modified = blob.last_modified

            # Formata a data
            modified_str = modified.strftime("%d/%m/%Y %H:%M")

            # Formata o tamanho
            size_str = format_size(size)

            # Trunca o nome se for muito longo
            if len(name) > 39:
                display_name = name[:36] + "..."
            else:
                display_name = name

            print(f"{display_name:<40} {size_str:<15} {modified_str:<20}")

            total_size += size

        # Mostra o resumo
        print("-" * 75)
        print(f"\n📊 Resumo:")
        print(f"   Total de arquivos: {len(blob_list)}")
        print(f"   Tamanho total: {format_size(total_size)}")

    except Exception as e:
        print(f"❌ ERRO ao listar arquivos: {e}")
        print("\n💡 Dicas:")
        print("   - Verifique se a connection string está correta no .env")
        print(f"   - Verifique se o container '{container_name}' existe")
        print("   - Crie o container no Portal Azure ou use create_container.py")
        sys.exit(1)

if __name__ == "__main__":
    # O usuário pode passar o nome do container como argumento
    container_name = sys.argv[1] if len(sys.argv) > 1 else None
    list_files(container_name)
