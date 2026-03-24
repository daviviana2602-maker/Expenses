# 📊 Controle de Gastos (Expenses Tracker)
Programa em Python via CLI para controlar e gerenciar despesas pessoais, categorizadas como **residencial** ou **variável**, usando **PostgreSQL** para armazenamento dos dados.

------------------------------------------------------------------------------------------------

# 🛠 Funcionalidades

* Registrar despesas com descrição, categoria, valor e data.
* Gerar relatórios para um período específico:

  * Total de gastos
  * Total de gastos residenciais
  * Total de gastos variáveis
* Visualizar uma tabela detalhada de todas as despesas em um período selecionado.
* Interface colorida e clara no terminal, facilitando o uso.

------------------------------------------------------------------------------------------------

# 📝 Tecnologias Utilizadas

* Python 3.x
* SQLAlchemy (ORM)
* PostgreSQL
* Colorama (para cores no terminal)
* Tabulate (para tabelas bonitinhas)
* Módulo customizado (fanymodules) para validação de entradas

------------------------------------------------------------------------------------------------

# ⚙ Instruções de Configuração

* Clonar o repositório:

  ```bash
  git clone https://github.com/SEU_USUARIO/expenses.git
  cd expenses
  ```
* Instalar dependências:

  ```bash
  pip install sqlalchemy psycopg2-binary colorama tabulate
  ```
* Configurar PostgreSQL:

  * Atualize a variável `DATABASE_URL` no arquivo `main.py`:

    ```python
    DATABASE_URL = "postgresql+psycopg2://usuario:senha@localhost:5432/nome_do_banco"
    ```
  * Certifique-se de que o servidor PostgreSQL está rodando.
* Executar o programa:

  ```bash
  python main.py
  ```

------------------------------------------------------------------------------------------------

# 🧭 Como Usar

* Opções do Menu:

  * **Registrar Despesa** – Inserir detalhes da despesa (descrição, categoria, valor, data)
  * **Relatório por Período** – Mostra total de gastos, gastos residenciais e variáveis dentro do período selecionado
  * **Ver Tabela de Despesas** – Mostra uma tabela detalhada de todas as despesas no período escolhido

* Encerrar Programa

------------------------------------------------------------------------------------------------

# 💡 Observações

* Todas as entradas são validadas pelo módulo customizado `fanymodules`.
* As datas devem ser inseridas no formato **DD/MM/AAAA**.
* Suporta tanto despesas **residenciais (fixas)** quanto **variáveis (flexíveis)**.
