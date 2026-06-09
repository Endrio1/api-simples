from flask import Flask, request, jsonify, abort
import uuid

app = Flask(__name__)

# Estrutura simples de armazenamento em memória
items = {}


@app.route('/items/', methods=['POST'])
def cria_item():
    data = request.get_json() or {}
    nome = data.get('nome')
    preco = data.get('preco')
    # validação mínima
    if nome is None or preco is None:
        return jsonify({'detail': 'Campos obrigatórios ausentes'}), 400

    item_id = str(uuid.uuid4())
    novo_item = {
        'id': item_id,
        'nome': nome,
        'descricao': data.get('descricao'),
        'preco': preco,
    }
    items[item_id] = novo_item
    return jsonify({'message': 'Item criado', 'item': novo_item})


@app.route('/items/', methods=['GET'])
def mostrar_items():
    return jsonify({'items': list(items.values())})


@app.route('/items/<item_id>', methods=['GET'])
def buscar_item(item_id: str):
    if item_id not in items:
        return jsonify({'detail': 'Item não encontrado'}), 404
    return jsonify({'item': items[item_id]})


@app.route('/items/<item_id>', methods=['PUT'])
def atualiza_item(item_id: str):
    if item_id not in items:
        return jsonify({'detail': 'Item não encontrado'}), 404
    data = request.get_json() or {}
    # Espera o objeto completo com 'id' e campos
    items[item_id] = {
        'id': item_id,
        'nome': data.get('nome'),
        'descricao': data.get('descricao'),
        'preco': data.get('preco'),
    }
    return jsonify({'message': 'Item atualizado', 'item': items[item_id]})


@app.route('/item/<item_id>', methods=['DELETE'])
def apagar_item(item_id: str):
    if item_id not in items:
        return jsonify({'detail': 'Item não encontrado'}), 404
    apaga_item = items.pop(item_id)
    return jsonify({'message': 'Item deletado', 'Item': apaga_item})


def criar_app():
    # Limpa estado compartilhado e retorna a instância da aplicação.
    items.clear()
    return app


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
