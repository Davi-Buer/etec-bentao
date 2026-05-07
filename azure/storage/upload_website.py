#!/usr/bin/env python3
"""
Script para fazer upload de um site completo para o Azure Static Website.

Uso:
    python upload_website.py
    python upload_website.py --folder ./meu-site
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Carrega as variáveis do arquivo .env
load_dotenv()

def get_content_type(file_path):
    """
    Retorna o Content-Type correto baseado na extensão do arquivo.

    Args:
        file_path: Caminho do arquivo

    Returns:
        String com o content-type
    """
    extension = Path(file_path).suffix.lower()

    content_types = {
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.json': 'application/json',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml',
        '.ico': 'image/x-icon',
        '.txt': 'text/plain',
        '.pdf': 'application/pdf',
    }

    return content_types.get(extension, 'application/octet-stream')

def upload_website(website_folder='./website'):
    """
    Faz upload de todos os arquivos de um site para o container $web.

    Args:
        website_folder: Pasta onde estão os arquivos do site
    """

    # Pega a connection string do arquivo .env
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    # Verifica se a connection string foi configurada
    if not connection_string or connection_string == "sua-connection-string-aqui":
        print("❌ ERRO: Configure sua AZURE_STORAGE_CONNECTION_STRING no arquivo .env")
        print("   Copie a connection string do Portal Azure > Storage Account > Access keys")
        sys.exit(1)

    # Verifica se a pasta do site existe
    if not os.path.exists(website_folder):
        print(f"❌ ERRO: Pasta '{website_folder}' não encontrada!")
        print("\n💡 Certifique-se de que a pasta website existe com os arquivos:")
        print("   - index.html")
        print("   - style.css")
        print("   - script.js")
        sys.exit(1)

    try:
        print(f"🌐 Fazendo upload do site para Azure Static Website...\n")

        # Conecta ao Azure Storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # O container para static websites é sempre $web
        container_name = '$web'
        container_client = blob_service_client.get_container_client(container_name)

        # Conta os arquivos
        arquivos_enviados = 0
        total_bytes = 0

        # Percorre todos os arquivos na pasta
        for root, dirs, files in os.walk(website_folder):
            for file_name in files:
                # Ignora arquivos ocultos e README
                if file_name.startswith('.') or file_name == 'README.md':
                    continue

                # Caminho completo do arquivo local
                file_path = os.path.join(root, file_name)

                # Nome do blob (remove o prefixo da pasta)
                blob_name = os.path.relpath(file_path, website_folder)

                # Detecta o content-type
                content_type = get_content_type(file_path)

                print(f"📤 Enviando: {blob_name} ({content_type})")

                # Faz o upload
                blob_client = container_client.get_blob_client(blob_name)

                with open(file_path, 'rb') as data:
                    blob_client.upload_blob(
                        data,
                        overwrite=True,
                        content_settings={'content_type': content_type}
                    )

                # Atualiza estatísticas
                file_size = os.path.getsize(file_path)
                total_bytes += file_size
                arquivos_enviados += 1

        # Converte bytes para MB
        total_mb = total_bytes / (1024 * 1024)

        print("\n" + "="*60)
        print("✅ Upload concluído com sucesso!")
        print("="*60)
        print(f"📁 Arquivos enviados: {arquivos_enviados}")
        print(f"💾 Tamanho total: {total_mb:.2f} MB ({total_bytes:,} bytes)")
        print(f"📦 Container: {container_name}")

        # Tenta pegar a URL do static website
        try:
            account_name = blob_service_client.account_name
            print(f"\n🌐 URL do site:")
            print(f"   https://{account_name}.z15.web.core.windows.net/")
            print("\n💡 Se a URL acima não funcionar, encontre a URL correta em:")
            print("   Portal Azure > Storage Account > Static website > Primary endpoint")
        except:
            print("\n💡 Para ver a URL do site:")
            print("   Portal Azure > Storage Account > Static website > Primary endpoint")

        print("\n📝 Arquivos enviados:")
        for root, dirs, files in os.walk(website_folder):
            for file_name in files:
                if not file_name.startswith('.') and file_name != 'README.md':
                    file_path = os.path.join(root, file_name)
                    blob_name = os.path.relpath(file_path, website_folder)
                    print(f"   ✓ {blob_name}")

    except Exception as e:
        print(f"❌ ERRO durante o upload: {e}")
        print("\n💡 Dicas:")
        print("   - Verifique se a connection string está correta no .env")
        print("   - Verifique se você habilitou 'Static website' no Portal Azure")
        print("   - O container $web é criado automaticamente quando você habilita Static website")
        sys.exit(1)

if __name__ == "__main__":
    # Permite especificar outra pasta
    website_folder = sys.argv[1] if len(sys.argv) > 1 else './website'

    print("🚀 Azure Static Website Upload\n")

    # Verifica se o .env existe
    if not os.path.exists('.env'):
        print("⚠️  Arquivo .env não encontrado!")
        print("   Execute: cp .env.example .env")
        print("   E configure sua connection string.\n")

    upload_website(website_folder)
