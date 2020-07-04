from flask import Flask, request
from flask_restful import Resource
import json

listagem_habilidades = [
    {
        'id': 0,
        'habilidade': 'Python'
    },

    {
        'id': 1,
        'habilidade': 'HTML'
    },

    {
        'id': 2,
        'habilidade': 'CSS3'
    },

    {
        'id': 3,
        'habilidade': 'Javascript'
    }
]
# Lista, altera e exclui um desenvolvedor pelo ID
class Habilidades(Resource):
    def get(self, id):
        try:
            response = listagem_habilidades[id]
        except IndexError:
            mensagem = 'Habilidade de ID {} não existe'.format(id)
            response = {'status': "Erro", 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Contato do adminsitrador da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response

    def put(self, id):
            dados = json.loads(request.data)
            listagem_habilidades[id] = dados
            return dados

    def delete(self, id):
        listagem_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}

# Lista todos os desnvolvedores e insere um novo desenvolvedor
class ListaHabilidades(Resource):
    def get(self):
        return listagem_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(listagem_habilidades)
        dados['id'] = posicao
        listagem_habilidades.append(dados)
        return listagem_habilidades[posicao]

