# Teste de nivelamento IntuitiveCare

Os projetos abordados nesse teste de nivelamento são conceitos básicos para refletir algumas tarefas do cotidiano da empresa.
Serão desenvolvidos projetos de "Web Scraping" (coleta de dados de um site), transformação de dados, de banco de dados (PostgreSQL) e utilização de API.


### Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/pt-br/)
* [PostgreSQL](https://www.postgresql.org/)


## Dependências e Versões Necessárias

As dependências estão armazenadas no arquivo "requirements.txt", na qual facilita realizar a instalação dessas dependências e assim conseguir executar o projeto com êxito.

Segue abaixo uma lista com as principais dependências do projeto:

* Python - Versão: 3.12.2

## 📌 Projetos realizados 📌

## ⏭️ Web Scraping

Possui as seguintes funções:
1. Acessar site: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
2. Realizar o download dos arquivos "Anexo I" e "Anexo II" no formato PDF;
3. Compactar os dois arquivos baixados em um único arquivo no formato ZIP.


## ⏭️ Transformação de dados

As tarefas realizadas nessa etapa são de:
1. Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do arquivo "Anexo I";
2. Salvar esses dados em uma tabela estruturada, em formato CSV;
3. Substituir as abreviações das colunas OD e AMB pelas descrições completas, conforme legenda no rodapé;
4. Compactar a tabela elaborada em um arquivo denominado "Teste_jamil.zip";


## ⏭️ Banco de dados

Como preparação para esse teste foi realizado o download dos arquivos dos pultimos dois anos do repositório: https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/
E também o download dos "Dados Cadastrais das Operadoras Ativas na ANS" no link: https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/

Após realizar essa preparação dos dados, o objetivo é de criar scripts .sql compatível com PostgreSQL que executa as terefas abaixo:
1. Criar queries para estruturar a tabelas necessárias para o arquivo CSV;
2. Elaborar queries para importar conteúdo dos arquivos preparados, atentando para o enconding correto;
3. Desenvolver uma query analítica para responder:
    * Quais as 10 operadoras com mais despesas em "EVENTOS / SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR" no último trimestre?
    * Quais as 10 operadoras com maiores despesas nessa categoria no último ano?


## ⏭️ API

Desenvolver uma interface web usando Vue.js que interaja com um servidor em Python utilizando os "Dados Cadastrais das Operadoras Ativas na ANS, baixado anteriormente, na qual realize as seguintes tarefas:
1. Criar o servidor com uma rota que realize a busca textual na lista de cadastro das operadoras e retorne os registros mais relevantes;
2. Elaborar uma coleção no Postman para demonstrar o resultado.