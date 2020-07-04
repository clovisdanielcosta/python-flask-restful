from flask_restful import Resource

lista_habilidades = ['Python', 'HTML', 'CSS3', 'Javascript']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades

