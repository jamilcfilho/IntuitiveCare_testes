# Teste de nivelamento IntuitiveCare

Os projetos abordados nesse teste de nivelamento são conceitos básicos para refletir algumas tarefas do cotidiano da empresa.
Serão desenvolvidos projetos de "Web Scraping" (coleta de dados de um site), transformação de dados, de banco de dados (MySQL) e utilização de uma API utilizando o Flask e o Vue.js.


### Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/pt-br/)
* [Pandas](https://pandas.pydata.org/)
* [MySQL](https://www.mysql.com/)
* [Flask](https://flask.palletsprojects.com/en/stable/)
* [Vue.js](https://vuejs.org/)
* [Postman](https://www.postman.com/)


## Dependências e Versões Necessárias

As dependências estão armazenadas no arquivo "requirements.txt", na qual facilita realizar a instalação dessas dependências e assim conseguir executar o projeto com êxito.

Segue abaixo uma lista com as principais dependências do projeto:

* Flask - Versão: 3.1.0
* Pandas - Versão: 2.2.3
* Python - Versão: 3.12.2
* Selenium - Versão: 4.30.0

## 📌 Projetos realizados 📌

## ⏭️ Web Scraping

Possui as seguintes funções:
1. Acessar site: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
2. Realizar o download dos arquivos "Anexo I" e "Anexo II" no formato PDF;
3. Compactar os dois arquivos baixados em um único arquivo no formato ZIP.

-> Foi realizado essa tarefa utilizando o Selenium para realizar a automação do processo de coleta de dados do site realizando o download dos arquivos e após através de códigos Python e de outras bibliotecas foi possível compactar os arquivos em formato ZIP.


## ⏭️ Transformação de dados

As tarefas realizadas nessa etapa são de:
1. Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do arquivo "Anexo I";
2. Salvar esses dados em uma tabela estruturada, em formato CSV;
3. Substituir as abreviações das colunas OD e AMB pelas descrições completas, conforme legenda no rodapé;
4. Compactar a tabela elaborada em um arquivo denominado "Teste_jamil.zip";

-> Para possuir melhor visualização dos dados e de como agir perante eo desafio, optei por utilizar a linguagem Python porém utilizando o Jupyter notebook para conseguir ir realizando as etapas e conseguir verificando as tabelas assim que escrevia o código. Utilizei para efetuar as tarefas as bibliotecas Pandas e o Tabula para realizar a análise dos dados e depois conseguir fazer a transformações deles.


## ⏭️ Banco de dados

Como preparação para esse teste foi realizado o download dos arquivos dos pultimos dois anos do repositório: https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/
E também o download dos "Dados Cadastrais das Operadoras Ativas na ANS" no link: https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/

Após realizar essa preparação dos dados, o objetivo é de criar scripts .sql compatível com PostgreSQL que executa as terefas abaixo:
1. Criar queries para estruturar a tabelas necessárias para o arquivo CSV;
2. Elaborar queries para importar conteúdo dos arquivos preparados, atentando para o enconding correto;
3. Desenvolver uma query analítica para responder:
    * Quais as 10 operadoras com mais despesas em "EVENTOS / SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR" no último trimestre?
    * Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

-> Utilizei o MySQL Workbench 8.0 para concluir essa tarefa, porém aqui encontrei dificuldade com as tabelas devido que mesmo realizando a conversão dos arquivos para UTF-8 não consegui alimentar devidamente a tabela devido a um erro com determinados caracteres que os arquivos contém. Como próximos passos vou verificar e ver o que houve para concluir 100%.

## ⏭️ API

Desenvolver uma interface web usando Vue.js que interaja com um servidor em Python utilizando os "Dados Cadastrais das Operadoras Ativas na ANS, baixado anteriormente, na qual realize as seguintes tarefas:
1. Criar o servidor com uma rota que realize a busca textual na lista de cadastro das operadoras e retorne os registros mais relevantes;
2. Elaborar uma coleção no Postman para demonstrar o resultado.

-> Para essa tarefa foram utilizados o Pandas novamente e separei os arquivos de backend quanto o de frontend para tornar o código mais fácil de realizar manutenção e através do Flask foi possível unir as aplicações realizando a leitura do arquivo e tornando possível realizar a buscar das operados via frontend do Vue.js, ainda aprendi a trabalhar de forma simples com o Postman, na qual não havia conhecimento sobre ele ainda e puder ver como ele é interessante para realizar testes nas aplicações em sites.