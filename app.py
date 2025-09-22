from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Funções auxiliares para ler/escrever JSON
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        return json.load(f)

def escrever_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f, indent=2)

# Rotas de Produtos
@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = ler_arquivo('produtos.json')
    return jsonify(produtos)

# Cadastro de Usuário
@app.route('/usuarios/cadastro', methods=['POST'])
def cadastro_usuario():
    usuarios = ler_arquivo('usuarios.json')
    dados = request.get_json()
    usuario = dados.get('usuario')
    senha = dados.get('senha')
    
    if any(u['usuario'] == usuario for u in usuarios):
        return jsonify({'message': 'Usuário já existe'}), 400

    novo_usuario = {
        'id': str(uuid.uuid4()),
        'usuario': usuario,
        'senha': senha,
        'historico': []
    }
    usuarios.append(novo_usuario)
    escrever_arquivo('usuarios.json', usuarios)
    return jsonify({'message': 'Cadastro realizado com sucesso'})

# Login de Usuário
@app.route('/usuarios/login', methods=['POST'])
def login_usuario():
    usuarios = ler_arquivo('usuarios.json')
    dados = request.get_json()
    usuario = dados.get('usuario')
    senha = dados.get('senha')
    user = next((u for u in usuarios if u['usuario']==usuario and u['senha']==senha), None)
    if not user:
        return jsonify({'message': 'Usuário ou senha incorretos'}), 400
    return jsonify(user)

# Criar Pedido
@app.route('/pedidos', methods=['POST'])
def criar_pedido():
    pedidos = ler_arquivo('pedidos.json')
    dados = request.get_json()
    usuarioId = dados.get('usuarioId')
    itens = dados.get('itens')

    pedido = {
        'id': str(uuid.uuid4()),
        'usuarioId': usuarioId,
        'itens': itens,
        'data': datetime.now().isoformat()
    }
    pedidos.append(pedido)
    escrever_arquivo('pedidos.json', pedidos)

    # Atualiza histórico do usuário
    usuarios = ler_arquivo('usuarios.json')
    usuario = next((u for u in usuarios if u['id'] == usuarioId), None)
    if usuario:
        usuario['historico'].append(pedido)
        escrever_arquivo('usuarios.json', usuarios)

    return jsonify({'message': 'Pedido realizado com sucesso', 'pedido': pedido})

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)
