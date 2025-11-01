# Projeto Pandas

## 📚 Sumário
- [Como acessar o repositório](#-como-acessar-o-repositório)
- [Dependências necessárias](#-dependências-necessárias)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Instalação](#%EF%B8%8F-instalação)
- [Variáveis de ambiente](#%EF%B8%8F-variáveis-de-ambiente)
- [Documentação](#-documentação)

##  ▶ Como acessar o repositório

- Acesse o repositório por este link:

    https://github.com/GabrielFreitas836/projeto-pandas.git

##  🧰 Dependências necessárias
- Visual Studio Code: 
    https://code.visualstudio.com/download
- Python:
    https://www.python.org/downloads/
- Pandas:

    ```
    pip install pandas
    ```
- MySQL connector:

    ```
    pip install mysql-connector-python
    ```
- dotenv

    ```
    pip install dotenv
    ```
- openpyxl (permite ler arquivos excel)

    ```
    pip install openpyxl
    ```
- (opcional) tabulate

    ```
    pip install tabulate
    ```

## 🗂 Estrutura do projeto

```bash
projeto-pandas/
├── .venv/
├── src/
│   ├── entrada.py
│   └── main.py
├── .env
├── .gitignore
└── README.md  
```

## 💡Funcionalidades

O projeto foi desenvolvido para oferecer uma interface interativa em terminal que permite ao usuário ler, validar e visualizar dados provenientes de diferentes fontes (Excel e MySQL), utilizando a biblioteca Pandas como base para manipulação de dados.

🔹 **Menu principal**

- Exibe uma interface simples e clara no terminal.

- Oferece três opções principais:

    - Ler arquivo Excel

    - Ler arquivo de banco MySQL

    - Sair do programa

📘 **Leitura de arquivos Excel**

- Solicita ao usuário o caminho completo do arquivo .xlsx a ser lido.

- Realiza a leitura com pandas.read_excel().

- Verifica se o arquivo não está vazio antes de exibir.

- Mostra as primeiras linhas da planilha em formato de tabela estilizada com tabulate.

- Exibe mensagens de erro claras em caso de:

    - Caminho inválido

    - Arquivo vazio

    - Formato incorreto

🗄️ **Leitura de dados MySQL**

- Carrega automaticamente as variáveis de ambiente do arquivo .env (host, usuário e senha).

- Permite ao usuário informar o nome do banco de dados desejado.

- Exibe todas as tabelas disponíveis no banco, formatadas em tabela visual (tabulate).

- Permite selecionar uma tabela e visualizar as primeiras linhas via pandas.read_sql().

- Implementa tratamento de exceções específicas do mysql.connector para:

    - Erros de conexão

    - Erros de interface

    - Erros internos ou de execução

- Fecha automaticamente a conexão após o uso.

⏱️ Interações e usabilidade

- Utiliza delays com time.sleep() para tornar a interação mais fluida e natural.

- Mensagens são apresentadas com formatação e espaçamento para melhorar a leitura.

- Inclui tratamento de exceções gerais para evitar que o programa seja encerrado abruptamente.

🧰 Estrutura modular

- entrada.py: Contém a classe Entrada, responsável por todo o fluxo de entrada, leitura e validação.

- main.py: Ponto de partida do sistema, que instancia e executa o menu principal.

##  ⬇️ Instalação

Siga os passos abaixo para configurar o ambiente e executar o projeto localmente

1. Clone o repositório

    ```
    git clone https://github.com/GabrielFreitas836/projeto-pandas.git
    ```

1. Acesse o diretório do projeto
   
    ```
    cd projeto-pandas
    ```

3. (Opcional) Crie e ative um ambiente virtual

    ```
    python -m venv .venv
    ```

    . No Windows

    ```
    cd .venv\Scripts\activate
    ```
    

    . No Linux/Mac

   ```
   source .venv/bin/activate
   ```

5. Instale as dependências necessárias

    [Dependências necessárias](#-dependências-necessárias)
    
6. Execute o projeto
    ```
    python main.py
    ```

    
## ⚙️ Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env para realizar a conexão com o banco de dados

`DB_HOST`

`DB_USER`

`DB_PASSWORD`

## 📄 Documentação

Segue abaixo os links da documentação oficial de algumas das ferramentas utilizadas nesse projeto:

- [Python](https://docs.python.org/3/)

- [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)

- [Pandas](https://pandas.pydata.org/docs/)

- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)
