from flask import Flask, jsonify, request
from flask_cors import CORS  # Importe o CORS

app = Flask(__name__)
CORS(app)  # Ativa o CORS no Flask

import csv
import os

# Função para carregar o CSV
def carregar_csv():
    caminho_arquivo = r'C:\Users\jamil\OneDrive\Área de Trabalho\IntuitiveCare\p4_api\backend\Relatorio_cadop.csv'
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo não foi encontrado em {caminho_arquivo}")
    
    with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile, delimiter=';')
        dados = [linha for linha in leitor]
    return dados

# Rota de busca
@app.route('/buscar')
def buscar():
    query = request.args.get('query', '').strip().lower()  # Usar strip() para remover espaços extras
    dados = carregar_csv()

    # Se a query estiver vazia, retornar uma lista vazia
    if not query:
        return jsonify([])

    # Filtro refinado: procurar nos campos Razao_Social e CNPJ
    resultados = [item for item in dados if 
                  query in item['Razao_Social'].lower() or 
                  query in item['CNPJ'].lower()]

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
