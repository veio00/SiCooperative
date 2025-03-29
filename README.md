# SiCooperative

## Descrição
SiCooperative é um projeto de ingestão de dados com transformação e normalização, projetado para facilitar consultas e a construção de modelos analíticos. O objetivo é processar massas de dados brutas, aplicar ETL (Extract, Transform, Load) e gerar arquivos estruturados para análises posteriores, utilizando ferramentas modernas e escaláveis.

## Funcionalidades
- Ingestão de dados brutos a partir de uma massa de dados.
- Transformação e normalização de dados utilizando Python ou Scala.
- Geração de arquivos CSV com os dados processados.
- Testes automatizados para validar as etapas de ETL.

## Tecnologias Utilizadas
- **Python**: Para ingestões em batch e execução de ETL mais simples.
- **Scala**: Para processamentos rápidos e escaláveis (NRT).
- **Apache Spark**: Framework principal para manipulação de dados em larga escala.
- **MySQL**: Banco de dados relacional para armazenamento estruturado.
- **unittest**: Biblioteca nativa do Python para testes leves e eficientes.
- **Docker**: Para criação de um ambiente isolado e replicável via Jupyter Notebook.

## Pré-requisitos
- Docker instalado na máquina.
- Powershell (para usuários Windows) ou terminal compatível (Linux/Mac).
- Conexão à internet para baixar dependências iniciais.

## Como Instalar e Usar
1. **Baixe o projeto**:
   - Clone o repositório com
    ```
     git clone https://github.com/veio00/SiCooperative.git
    ``` 
   - ou faça o download manualmente.

2. **Inicie o ambiente**:
   - Abra o Powershell (ou terminal) na pasta raiz do projeto.
   - Execute o comando: 
     ```
     docker-compose up --build
     ```
   - Aguarde até que o Jupyter Notebook esteja ativo.

3. **Acesse o Jupyter Notebook**:
   - Abra o link no navegador: 
     ```
     http://localhost:8888/tree`.
     ```

4. **Processamento dos dados**:
   - Navegue até a pasta `massa_dados` no Jupyter.
   - Execute o notebook correspondente ao seu gosto:
   - Para Python: rode o notebook com a massa de dados em Python.
   - Para Scala: rode o notebook com a massa de dados em Scala.
   - Volte uma pasta e execute o notebook `movimento_flat_{python ou scala}`.
   - Esses notebooks contêm o ETL completo (extract, load e transform) e os testes associados.
   - O resultado será um arquivo CSV gerado na pasta `csv` (na raiz do Jupyter) ou dentro da pasta `notebooks` na raiz do projeto.
   - **Limpeza da massas de dados**: Caso deseje criar uma nova massa de dados, utilize os notebooks `limpar_base_python` ou `limpar_base_scala`, localizados na pasta `notebooks`. Eles são scripts de limpeza que zeraram as tabelas.

## Estrutura do Projeto
   - `/massa_dados`: Contém os dados brutos para ingestão.
   - `/notebooks`: Notebooks com o ETL e testes.
   - `/csv`: Pasta onde os arquivos processados são salvos.
   - `docker-compose.yml`: Configuração do ambiente Docker.

## Observações Técnicas
   - **Conflitos Resolvidos**:
   - Na tabela `conta`, o campo `tipo` foi definido como `varchar` no MySQL, pois o banco não suporta tipagem de objetos. Essa escolha facilita conversões futuras, se necessário.
   - O campo `data_criacao_cartao`, solicitado no arquivo final `movimento_flat`, não existe na massa de dados original. Foi removido do resultado, mas o código foi estruturado para fácil inclusão futura caso a informação seja fornecida ou uma regra de negócio seja definida.

   - **Escolhas Técnicas**:
   - **Spark"**: Escolhido por ser o framework mais popular para manipulação de dados em larga escala.
   - **Python e Scala**: Python para processamentos em batch (lentos e simples), Scala para NRT (rápidos e escaláveis), atendendo a diferentes cenários de volume e velocidade.
   - **MySQL**: Banco amplamente utilizado e confiável.
   - **unittest**: Biblioteca nativa, leve e suficiente para os testes, evitando sobrecarga no fluxo.
   - **Jupyter Notebook**: Adotado para acelerar o desenvolvimento e promover colaboração, oferecendo um ambiente interativo e documentado.

## Status do Projeto
O projeto está funcional e foi desenvolvido como uma solução prática para ingestão e transformação de dados. Está aberto a melhorias e ajustes conforme novas demandas ou regras de negócio surgirem.

## Como Contribuir
- Faça um fork do repositório.
- Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
- Commit suas mudanças e envie um pull request com uma descrição clara.

## Contato
Para dúvidas ou sugestões, entre em contato pelo GitHub Issues ou diretamente com o mantenedor (@veio00).
