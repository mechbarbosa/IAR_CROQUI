# ============================================================
# SISTEMA DE CROQUI INTERATIVO EM TEMPO REAL
# Backend Flask + Firebase Admin
# ============================================================


# Importa o módulo os para acessar arquivos locais
# e variáveis de ambiente do sistema.
import os


# Importa o módulo json para trabalhar com dados JSON.
import json


# Importa a classe Flask para criar a aplicação web.
# render_template permite carregar arquivos HTML da pasta templates.
# jsonify permite retornar respostas no formato JSON.
from flask import Flask, render_template, jsonify


# Importa o SDK administrativo do Firebase.
import firebase_admin


# Importa o módulo de credenciais do Firebase.
from firebase_admin import credentials


# Importa o módulo do Realtime Database.
from firebase_admin import db


# ============================================================
# CONFIGURAÇÃO DA APLICAÇÃO FLASK
# ============================================================


# Cria a aplicação Flask.
# template_folder define explicitamente a pasta dos arquivos HTML.
# static_folder define explicitamente a pasta dos arquivos CSS,
# JavaScript, imagens e outros arquivos estáticos.
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


# ============================================================
# CONFIGURAÇÃO DO FIREBASE
# ============================================================


# Define a URL do Firebase Realtime Database utilizada pelo projeto.
FIREBASE_DATABASE_URL = (
    "https://projetocroqui-105df-default-rtdb.firebaseio.com"
)


# Verifica se nenhuma aplicação Firebase foi inicializada ainda.
# Isso evita o erro causado por tentar inicializar o Firebase
# mais de uma vez durante a execução.
if not firebase_admin._apps:


    # ========================================================
    # OPÇÃO 1 - CREDENCIAL LOCAL
    # ========================================================


    # Verifica se existe o arquivo dados.json
    # na pasta onde o programa está sendo executado.
    if os.path.exists("dados.json"):


        # Carrega as credenciais diretamente do arquivo JSON.
        cred = credentials.Certificate(
            "dados.json"
        )


    # ========================================================
    # OPÇÃO 2 - VARIÁVEIS DE AMBIENTE
    # ========================================================


    else:


        # Obtém o ID do projeto Firebase armazenado
        # na variável de ambiente FIREBASE_PROJECT_ID.
        project_id = os.environ.get(
            "FIREBASE_PROJECT_ID"
        )


        # Obtém a chave privada Firebase armazenada
        # na variável de ambiente FIREBASE_PRIVATE_KEY.
        private_key = os.environ.get(
            "FIREBASE_PRIVATE_KEY"
        )


        # Obtém o e-mail da conta de serviço Firebase
        # armazenado na variável FIREBASE_CLIENT_EMAIL.
        client_email = os.environ.get(
            "FIREBASE_CLIENT_EMAIL"
        )


        # Verifica se a chave privada foi encontrada.
        if private_key:


            # Substitui os caracteres "\n" por quebras
            # de linha reais.
            #
            # Isso é necessário porque plataformas de hospedagem
            # costumam armazenar a chave privada em uma única linha.
            private_key = private_key.replace(
                "\\n",
                "\n"
            )


        # Cria um dicionário no formato esperado
        # pelo Firebase Admin SDK.
        firebase_credentials = {


            # Define o tipo de credencial.
            "type": "service_account",


            # Define o ID do projeto.
            "project_id": project_id,


            # Define a chave privada.
            "private_key": private_key,


            # Define o e-mail da conta de serviço.
            "client_email": client_email,


            # URL utilizada para autenticação Google.
            "auth_uri":
                "https://accounts.google.com/o/oauth2/auth",


            # URL utilizada para geração de token.
            "token_uri":
                "https://oauth2.googleapis.com/token",


            # URL dos certificados públicos do Google.
            "auth_provider_x509_cert_url":
                "https://www.googleapis.com/oauth2/v1/certs"

        }


        # Cria o objeto de credencial usando
        # o dicionário montado acima.
        cred = credentials.Certificate(
            firebase_credentials
        )


    # ========================================================
    # INICIALIZAÇÃO DO FIREBASE
    # ========================================================


    # Inicializa o Firebase Admin utilizando:
    #
    # 1. As credenciais carregadas anteriormente.
    # 2. A URL do Realtime Database.
    firebase_admin.initialize_app(
        cred,
        {
            "databaseURL": FIREBASE_DATABASE_URL
        }
    )


# ============================================================
# ROTA PRINCIPAL
# ============================================================


# Define a rota principal da aplicação.
#
# Quando o usuário acessar:
#
# http://127.0.0.1:5000/
#
# esta função será executada.
@app.route("/")
def index():


    # Renderiza o arquivo index.html localizado
    # dentro da pasta templates.
    return render_template(
        "index.html"
    )


# ============================================================
# ROTA DA API DE STATUS
# ============================================================


# Cria uma rota de API acessível em:
#
# /api/status
#
# O parâmetro methods=["GET"] informa que essa rota
# aceita requisições HTTP do tipo GET.
@app.route(
    "/api/status",
    methods=["GET"]
)
def api_status():


    # Retorna uma resposta JSON informando
    # que o servidor está funcionando.
    return jsonify(
        {
            "status": "Servidor rodando",
            "projeto": "projetocroqui-105df"
        }
    )


# ============================================================
# EXECUÇÃO LOCAL
# ============================================================


# Verifica se este arquivo está sendo executado
# diretamente pelo Python.
#
# Esse bloco não é executado quando o Flask
# é importado por outro sistema.
if __name__ == "__main__":


    # Inicia o servidor Flask.
    #
    # host="0.0.0.0"
    # permite aceitar conexões externas na rede local.
    #
    # port=5000
    # define a porta utilizada pelo servidor.
    #
    # debug=True
    # ativa recursos de desenvolvimento e recarregamento
    # automático quando o código é alterado.
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )