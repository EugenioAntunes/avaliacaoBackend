from flask import Flask, request
from flask_restful import Resource, Api

import json

app = Flask(__name__)
api = Api(app)

receitas_leves = [
    {
        "nome": "Salada de Beterraba com Molho de Gorgonzola",
        "ingredientes": [
            "1 kg de Beterraba",
            "4 Maçãs verde",
            "1/2 Chícara de Passas",
            "Folhas de Alface Americana",
            "200gr de Queijo Gorgonzola",
            "1 Iogurte Natural Desnatado",
            "100ml de Creme de Leite"
        ],
        "Modo de Preparo": [
            "Cozinhar a Beterraba por 10min e Ralar Grosseiramente",
            "Ralar as Maçãs Grossiramente",
            "Misture a Maçã, a Beterraba e as Passas",
            "Tempere com vinagre, azeite, sal e pimenta do reino",
            "Para o molho de Gorgonzola basta bater no liquidificardor o Iogurte Natural, o queijo e o creme de leite",
            "Recheie as Folhas de Alface com a mistura já temperadae coloque um pouco do molho por cima e está pronto para Servir"
        ],
        "yield": ["Serve 4 Porções"]
    },
    {
        "nome": "Salada de Acelfa com Molho de Abacaxi",
        "ingredientes": [
            "2 pés de acelga",
            "1/2 chícara de passas brancas",
            "2 chícaras de abacaxi contado em cubos pequenos",
            "2 colheres de sopa de vinagre",
            "1 colher de sopa de mostarda",
            "1 colher de chá de maisena",
            "1 colher de sopa de maionese",
            "sal e pimenta do reino a gosto"
        ],
        "Modo de Preparo": [
            "Lave as folhas de acelga e deixe de molho(em água e vinagre)por 15min",
            "Corte as folhas em tiras finas ",
            "Coloque em um recipiente, bem vedado, e deixe na geladeira até a hora de servir",
            "Em uma panela aquecida, coloque as passas e o abacaxi, vinagre, mostarda e tempere com sal e pimenta.",
            "Misture a maisena com um pouco de água e coloque na panela. Tire do fogo assim que engrossar.",
            "Junte a maionese",
            "Na hora de servir misture o molho com as folhas e Bom Apetite"
        ],
        "yield": ["Rende 5 porções"]
    },
    {
        "nome": "Salada Verde com Presunto",
        "ingredientes": [
            "10 folhas de Rúcula",
            "2 folhas de Alface Americana",
            "2 folhas de Alface Roxa",
            "2 folhas de Alface Crespa",
            "4 fatias de Presunto de Peru Defumado"
            "2 colheres de sopa de Cream Cheese",
            "1 colher de sopa de mel",
            "1 colher de sopa de mostarda amarela",
            "Sal e pimenta do reino a gosto"

        ],
        "Modo de Preparo": [
            "Higienizar e secar bem todas as folhas",
            "Rasgue grosseiramente e coloque no prato que irá servir",
            "Corte as fatias de poresunto ao meio e enrole-as, como pequenos canudos",
            "Disponha pequenas porções de Cream Cheese uniformemente por toda sala",
            "Misture o mel e a mostarda, coloque sobre a salada ou sirva a parte",
            "Tempere com sal e pimenta do reino e pode servir"
        ],
        "yield": ["Rende 1 porção"]
    }
]

class Receitas(Resource):
    def get(self):
        return {"status": 200, "Data": receitas_leves}

    def post(self):
        new_receitas = json.loads(request.data)
        receitas_leves.append(new_receitas)
        return {
            "message": "Uma nova Receita foi Adicionada!",
            "newValue": new_receitas
        }

class Receita(Resource):
    def get(self, indice):
        try:
            return receitas_leves[indice]
        except IndexError:
            mensagem = "O índice informado {} não pode ser encontrado!".format(indice)
            return {
                "status": "Erro not found",
                "message": mensagem,
            }
        except:
            mensagem = "Erro Desconhecido"
            return {
                "status": "Erro de índice",
                "message": mensagem,
            }

    def put(self, indice):
        newValue = json.loads(request.data)
        receitas_leves[indice] = newValue
        return {
            "message": "Receitinha atualizada!",
            "newValue": newValue
        }

    def delete(self, indice):
        receitas_leves.pop(indice)
        return {
            "message": "Receita deletada!",
            "arrayAtual": receitas_leves
        }

api.add_resource(Receitas, '/receitas/')
api.add_resource(Receita, '/receitas/<int:indices>')

if __name__ == '__main__':
    app.run(debug=True)
