import csv
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Ativar o CORS do Flask

# Função para carregar o arquivo CSV
def carregar_csv():
    caminho_arquivo = r'C:\Users\jamil\OneDrive\Área de Trabalho\IntuitiveCare\p4_api\backend\Relatorio_cadop.csv'

    with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=';')
        dados = [linha for linha in leitor]
    return dados

# Rota para realizar busca textual nos cadastros


@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '')  # Parâmetro de busca (term)
    dados = carregar_csv()

    # Filtrando os registros que contenham o termo de busca em qualquer campo
    resultados = [
        registro for registro in dados
        if any(termo.lower() in str(valor).lower() for valor in registro.values())
    ]

    return jsonify(resultados)


if __name__ == '__main__':
    app.run(debug=True)
