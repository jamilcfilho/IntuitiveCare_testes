
import os
import mysql.connector

# Converter a codificação dos arquivos para utf-8
# Função para converter codificação de arquivos CSV para UTF-8
def convert_to_utf8(file_path):
    try:
        with open(file_path, 'r', encoding='latin1') as file:  # Tente ler com a codificação Latin-1
            content = file.read()
        with open(file_path, 'w', encoding='utf-8') as file:  # Salve no formato UTF-8
            file.write(content)
        print(f"Arquivo '{file_path}' convertido para UTF-8 com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o arquivo '{file_path}': {e}")


# Caminho onde estão os arquivos CSV
folder_path = "C:\\Users\\jamil\\OneDrive\\Área de Trabalho\\IntuitiveCare\\p3_banco_dados"
# Itera sobre todos os arquivos CSV na pasta e os converte
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        file_path = os.path.join(folder_path, file_name)
        convert_to_utf8(file_path)



# Conectar ao banco de dados MySQL
db = mysql.connector.connect(
    host="xxxx",
    port="xxxx",
    user="xxxx",
    password="xxxx",
    database="ans_projeto"
)
cursor = db.cursor()

# Caminho onde estão os arquivos CSV
# Substitua pelo caminho correto
folder_path = "C:\\Users\\jamil\\OneDrive\\Área de Trabalho\\IntuitiveCare\\p3_banco_dados"

# Função para importar CSV para MySQL


def import_csv_to_mysql(file_path):
    try:
        query = f"""
        LOAD DATA LOCAL INFILE '{file_path}'
        INTO TABLE sua_tabela
        CHARACTER SET utf8
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES;
        """
        cursor.execute(query)
        db.commit()
        print(f"Arquivo '{file_path}' importado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao importar o arquivo '{file_path}': {err}")


# Iterar sobre todos os arquivos CSV na pasta e importá-los
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        file_path = os.path.join(folder_path, file_name)
        import_csv_to_mysql(file_path)

# Fechar a conexão
cursor.close()
db.close()
