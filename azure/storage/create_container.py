#!/usr/bin/env python3
"""
Script para criar um novo container no Azure Storage Account.

Uso:
    python create_container.py meu-container
    python create_container.py imagens
"""

import os
import sys
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, PublicAccess

# Carrega as variáveis do arquivo .env
load_dotenv()

def create_container(container_name, public_access=False):
    """
    Cria um novo container no Azure Storage.

    Args:
        container_name: Nome do container a ser criado
        public_access: Se True, permite acesso público aos blobs
    """

    # Pega a connection string do arquivo .env
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    # Verifica se a connection string foi configurada
    if not connection_string or connection_string == "sua-connection-string-aqui":
        print("❌ ERRO: Configure sua AZURE_STORAGE_CONNECTION_STRING no arquivo .env")
        print("   Copie a connection string do Portal Azure > Storage Account > Access keys")
        sys.exit(1)

    # Valida o nome do container
    # Regras do Azure: letras minúsculas, números e hífens, entre 3-63 caracteres
    if not container_name.islower() or len(container_name) < 3 or len(container_name) > 63:
        print("❌ ERRO: Nome do container inválido!")
        print("\n📋 Regras para nomes de containers:")
        print("   - Apenas letras minúsculas (a-z)")
        print("   - Números (0-9)")
        print("   - Hífens (-) no meio do nome")
        print("   - Entre 3 e 63 caracteres")
        print("\n✅ Exemplos válidos: documentos, imagens, backup-2024")
        print("❌ Exemplos inválidos: Documentos, docs_2024, -backup")
        sys.exit(1)

    try:
        print(f"📦 Criando container '{container_name}'...")

        # Conecta ao Azure Storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Define o nível de acesso
        if public_access:
            access_level = PublicAccess.Blob
            access_msg = "público (qualquer pessoa pode baixar os arquivos)"
        else:
            access_level = PublicAccess.OFF
            access_msg = "privado (apenas você pode acessar)"

        # Cria o container
        container_client = blob_service_client.create_container(
            name=container_name,
            public_access=access_level
        )

        print(f"✅ Container criado com sucesso!")
        print(f"   📁 Nome: {container_name}")
        print(f"   🔒 Acesso: {access_msg}")
        print(f"\n💡 Para fazer upload de arquivos:")
        print(f"   python upload_file.py seu-arquivo.txt")
        print(f"\n💡 Para usar este container por padrão, edite o .env:")
        print(f"   CONTAINER_NAME=\"{container_name}\"")

    except Exception as e:
        # Verifica se o erro é de container já existente
        if "ContainerAlreadyExists" in str(e):
            print(f"⚠️  Container '{container_name}' já existe!")
            print(f"   Use outro nome ou delete o existente no Portal Azure.")
        else:
            print(f"❌ ERRO ao criar container: {e}")
            print("\n💡 Dicas:")
            print("   - Verifique se a connection string está correta no .env")
            print("   - Verifique se você tem permissão para criar containers")
        sys.exit(1)

if __name__ == "__main__":
    # Verifica se o usuário passou o nome do container
    if len(sys.argv) < 2:
        print("❌ Uso: python create_container.py <nome-do-container> [--public]")
        print("\nExemplos:")
        print("  python create_container.py documentos")
        print("  python create_container.py imagens --public")
        print("  python create_container.py backup-2024")
        sys.exit(1)

    container_name = sys.argv[1]

    # Verifica se o usuário quer acesso público
    public_access = "--public" in sys.argv

    if public_access:
        print("⚠️  ATENÇÃO: Você está criando um container PÚBLICO!")
        print("   Qualquer pessoa com o link poderá baixar os arquivos.")
        response = input("   Tem certeza? (s/n): ")
        if response.lower() != 's':
            print("❌ Operação cancelada.")
            sys.exit(0)

    create_container(container_name, public_access)
