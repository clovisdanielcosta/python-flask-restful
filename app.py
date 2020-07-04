from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Daniel',
        'habilidades': ['Html', 'Javascript']},
    {
        'id': 1,
        'nome': 'Costa',
        'habilidades': ['React', 'Python']},
]

# Lista, altera e exclui um desenvolvedor pelo ID
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':"Erro", 'mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Contato do adminsitrador da API"
            response = {'status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})

# Lista todos os desnvolvedores e insere um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)