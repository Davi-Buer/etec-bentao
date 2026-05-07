#!/usr/bin/env python3
"""
Script de teste para verificar se o Azure Storage está configurado corretamente.

Uso:
    python test_setup.py
"""

import os
import sys
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Carrega as variáveis do arquivo .env
load_dotenv()

def test_connection():
    """
    Testa a conexão com o Azure Storage e verifica as configurações.
    """

    print("🔍 Testando configuração do Azure Storage...\n")

    # 1. Verifica se o arquivo .env existe
    if not os.path.exists(".env"):
        print("❌ Arquivo .env não encontrado!")
        print("   Execute: cp .env.example .env")
        print("   E configure sua connection string.")
        return False

    # 2. Verifica se a connection string foi configurada
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("CONTAINER_NAME", "documentos")

    if not connection_string:
        print("❌ AZURE_STORAGE_CONNECTION_STRING não configurada no .env")
        return False

    if connection_string == "sua-connection-string-aqui":
        print("❌ AZURE_STORAGE_CONNECTION_STRING não foi alterada!")
        print("   Abra o .env e cole sua connection string real do Azure.")
        return False

    print("✅ Arquivo .env encontrado e configurado")

    # 3. Testa a conexão
    try:
        print("🔌 Testando conexão com Azure Storage...")
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Tenta listar containers (isso valida a connection string)
        account_info = blob_service_client.get_account_information()

        print("✅ Conexão estabelecida com sucesso!")
        print(f"   Tipo de conta: {account_info['account_kind']}")

    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        print("\n💡 Verifique:")
        print("   - Se a connection string está completa (começa com DefaultEndpointsProtocol=)")
        print("   - Se não tem espaços extras no início/fim")
        print("   - Se você copiou do lugar certo: Portal > Storage Account > Access keys")
        return False

    # 4. Verifica se o container padrão existe
    try:
        print(f"\n📦 Verificando container '{container_name}'...")
        container_client = blob_service_client.get_container_client(container_name)

        # Tenta acessar as propriedades do container
        properties = container_client.get_container_properties()

        print(f"✅ Container '{container_name}' existe!")
        print(f"   Última modificação: {properties['last_modified']}")

        # Conta quantos arquivos tem
        blobs = list(container_client.list_blobs())
        print(f"   Arquivos no container: {len(blobs)}")

    except Exception as e:
        if "ContainerNotFound" in str(e):
            print(f"⚠️  Container '{container_name}' não existe ainda.")
            print(f"\n💡 Crie o container com:")
            print(f"   python create_container.py {container_name}")
            print(f"\n   Ou crie manualmente no Portal Azure:")
            print(f"   Storage Account > Containers > + Container")
        else:
            print(f"⚠️  Erro ao verificar container: {e}")

    # 5. Testa listagem de containers
    try:
        print(f"\n📂 Listando todos os containers disponíveis...")
        containers = blob_service_client.list_containers()
        container_list = list(containers)

        if not container_list:
            print("   Nenhum container encontrado.")
            print(f"\n💡 Crie seu primeiro container:")
            print(f"   python create_container.py documentos")
        else:
            print(f"   Total de containers: {len(container_list)}")
            for container in container_list:
                print(f"   - {container['name']}")

    except Exception as e:
        print(f"⚠️  Erro ao listar containers: {e}")

    print("\n" + "="*60)
    print("🎉 CONFIGURAÇÃO VALIDADA!")
    print("="*60)
    print("\n📚 Próximos passos:")
    print("   1. Crie um arquivo de teste: echo 'Olá Azure!' > teste.txt")
    print("   2. Faça upload: python upload_file.py teste.txt")
    print("   3. Liste arquivos: python list_files.py")
    print("   4. Baixe de volta: python download_file.py teste.txt teste-download.txt")

    return True

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
