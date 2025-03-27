#    Projeto - Transformação de dados


# 1. Extrair os dados da tabela Rol de Procedimentos e Eventos em Saúde do PDF do Anexo I do projeto 1 (todas as páginas)


import tabula
import pandas as pd
import zipfile
import os


def processar_tabela_pdf(nome_arquivo_pdf, nome_arquivo_csv, nome_arquivo_zip):
    """
    Extrai dados de um PDF, processa e salva em CSV e compacta em ZIP.

    Args:
        nome_arquivo_pdf (str): Nome do arquivo PDF de entrada.
        nome_arquivo_csv (str): Nome do arquivo CSV de saída.
        nome_arquivo_zip (str): Nome do arquivo ZIP de saída.
    """

    # 1. Extrair os dados da tabela do PDF
    tabelas = tabula.read_pdf(
        nome_arquivo_pdf, pages='all', multiple_tables=True)

    # Remover a primeira tabela da lista
    if tabelas:
        tabelas.pop(0)

    # Identificar as colunas esperadas (assumindo que a primeira tabela restante tem a estrutura correta)
    colunas_esperadas = tabelas[0].columns.tolist()

    # Padronizar e remover cabeçalhos duplicados
    tabelas_padronizadas = []
    for tabela in tabelas:
        for coluna in colunas_esperadas:
            if coluna not in tabela.columns:
                tabela[coluna] = pd.NA
        tabela = tabela[colunas_esperadas]  # Garante a ordem das colunas

        # Remover linhas que são cabeçalhos duplicados
        tabela = tabela[~tabela.apply(lambda row: all(row.astype(
            str) == pd.Series(colunas_esperadas).astype(str)), axis=1)]

        tabelas_padronizadas.append(tabela)

    # Concatenar todas as tabelas em um único DataFrame
    df = pd.concat(tabelas_padronizadas, ignore_index=True)

    # 2. Substituir as abreviações das colunas
    df.rename(columns={'OD': 'Odontológica',
              'AMB': 'Ambulatorial'}, inplace=True)

    # 3. Salvar os dados em um arquivo CSV
    df.to_csv(nome_arquivo_csv, index=False)

    # 4. Compactar o CSV em um arquivo ZIP
    with zipfile.ZipFile(nome_arquivo_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(nome_arquivo_csv)

    print(
        f"Arquivo CSV '{nome_arquivo_csv}' criado e compactado em '{nome_arquivo_zip}' com sucesso!")


# Uso da função
nome_do_arquivo_pdf = 'p1_web_scraping\downloads\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
nome_do_arquivo_csv = 'tabela_processada.csv'
nome_do_arquivo_zip = 'Teste_seu_nome.zip'  # Substitua 'seu_nome' pelo seu nome

processar_tabela_pdf(nome_do_arquivo_pdf,
                     nome_do_arquivo_csv, nome_do_arquivo_zip)


# 2. Substitua as abreviações das colunas OD (Odontológica) e AMB (Ambulatorial) pelas descrições completas.
# 3. Salve os dados em uma tabela estruturada, em formato csv.
# 4. Compacte o csv em um arquivo denominado "Teste_{seu_nome}.zip".
