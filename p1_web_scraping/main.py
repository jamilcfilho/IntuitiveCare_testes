#    Projeto - Web Scraping


# Pontos positivos do projeto:
# - Baixa os PDFs automaticamente sem abrir uma nova guia;
# - Lida com os cookies rejeitando-os;
# - Filtra e baixa apenas os arquivos desejados ("Anexo I" e "Anexo II");
# - Compacta os arquivos baixados em formato ZIP;

import os
import time
import zipfile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 1 - Acessar o site: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# A classe Service é usada para iniciar uma instância do Chrome webdriver
service = Service()

# Definindo o diretório onde os PDFs serão salvos indicando onde o script esta rodando e salvando na pasta "downloads"
base_diretorio = os.path.dirname(os.path.abspath(__file__))
diretorio_download = os.path.join(base_diretorio, "downloads")

# Como essa página para realizar o download dos arquivos abre uma nova guia para visualizar os PDFs antes, farei configuração no navegador para baixar os PDFs automaticamente.
# Configurações para o Chrome realizar automaticamente o download dos PDFs
configuracoes = Options()
# Definindo fazer o download em vez de abrir nova guia e não pergunta a onde salvar
preferencias = {"download.default_directory": diretorio_download,
                "plugins.always_open_pdf_externally": True, "download.prompt_for_download": False, }
configuracoes.add_experimental_option("prefs", preferencias)

# Inicia-se a instância do Chrome com respectivos "service" e "options"
driver = webdriver.Chrome(service=service, options=configuracoes)
driver.get(url)
time.sleep(2)


# 2 - Rejeitar os cookies do site, clicando em "Rejeitar cookies"
# XPATH - Identificador de elementos no site = //tag[@atributo='valor']
rejeitar_cookies = driver.find_element(
    By.XPATH, "//button[@class='br-button secondary small reject-all']")
rejeitar_cookies.click()
time.sleep(2)


# 3 - Realizar o download dos "Anexo I" e "Anexo II" em formato PDF
# Encontra e clica nos links dos PDFs
links = driver.find_elements(By.XPATH, '//a[contains(@href, ".pdf")]')
for link in links:
    href = link.get_attribute("href")
    print(href)
    if "Anexo_I" in href or "Anexo_II" in href:
        link.click()
        time.sleep(7)  # Tempo para aguardar o download


# 4 - Compactar todos os anexos baixados em um único arquivo em formato ZIP
# Definindo o caminho do arquivo ZIP
arquivo_zip = os.path.join(base_diretorio, "anexos.zip")

# Criando um arquivo ZIP para adicionar os PDFs
with zipfile.ZipFile(arquivo_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    for arquivo in os.listdir(diretorio_download):  # Para procurar os arquivos na pasta "downloads"
        if arquivo.endswith(".pdf"):  # Filtra apenas arquivos PDF
            file_path = os.path.join(diretorio_download, arquivo)
            zipf.write(file_path, os.path.basename(
                file_path))  # Adiciona ao ZIP
           
time.sleep(2)

# Finalizar a instancia 
driver.quit()

# input("")  # Comando necessário para o site não fechar após rodar etapas do código e conseguir ir clicando e verificando os XPATH - Desnecessário quando aplicação está pronta
