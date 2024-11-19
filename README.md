# WW2 Data

<p>
    Esta API fornece informações sobre as perdas humanas na 2ª Guerra Mundial. Os dados incluem mortes militares, civis, totais e percentuais relacionados à população inicial de cada país. A API permite consultas gerais e específicas com base em diferentes critérios. Os dados utilizados estão em dois datasets disponíveis no Kaggle:
    <a>https://www.kaggle.com/datasets/notkrishna/world-war-2-causalities-by-country</a>
    <a>https://www.kaggle.com/datasets/benmann2448/world-war-2-deaths</a>
</p>

<h2>Quickstart</h2>

Para iniciar o projeto localmente é preciso ter o Python3 instalado em seu computador, a versão utilizada foi `Python 3.12.2`. Além disso siga os passos abaixo.

- Baixe ou clone esse repositório para seu computador e navegue até ele no terminal

- Execute o comando a seguir: ` python venv_script.py`

- Ative o ambiente virtual com ` venv/Scripts/Activate` no Windows ou `source venv/bin/activate` no Linux ou Mac

- Em seguida faça as migrações para criar o banco de dados executando `python manage.py makemigrations` e em seguida <code>python manage.py migrate</code>

- Para popular o banco de dados rode o script load_data com <code>python load_data.py</code>. Esse script irá criar um arquivo csv com os dados de mortes totais, mortes civis, mortes militares e população inicial (em1939) para 40 países. Além de calcular e adicionar ao BD o percentual de mortes em relação a população inicial e o percentual de mortes de militares e civis em relação as mortes totais.

  <h2>Rotas e Views</h2>

  

  <h3>1 - Todos os Países</h3>

  **URL:** `/geral`

  **Método:** `GET`

  **Descrição:** Retorna todos países do banco de dados.

  <h3>2 - Países por Número de Mortes Totais</h3>

  **URL:** `/paises-mortes-totais`

  **Método:** `GET`

  **Parâmetro:**

  - `mt`: Número mínimo de mortes totais.
  - `comparison`: Operador de comparação (`gte` para maior ou igual, `lte` para menor ou igual).

  **Descrição:** Retorna os países filtrados com base no número de mortes totais.

  **Exemplo de Requisição:** `/paises?1000000&comparison=gte`



<h3>3 - Países por Percentual de Mortes Totais em Relação à População</h3>



**URL:** `/percentual-mortes-totais/`

**Método:** `GET` ou `POST`

**Parâmetros:**

- `pm`: Percentual de mortes totais em relação à população inicial.
- `comparison`: Operador de comparação (`gte` para maior ou igual, `lte` para menor ou igual).

**Descrição:** Retorna os países filtrados com base no percentual de mortes totais.

**Exemplo de Requisição:** `/percentual-mortes-totais?pm=2&comparison=gte`



<h3>4 - Países por Percentual de Mortes Militares em Relação a Mortes Totais</h3>

**URL:** `/percentual-mortes-militares/`

**Método:** `GET` ou `POST`

**Parâmetros:**

- `pm`: Percentual de mortes militares em relação ao total de mortes.
- `comparison`: Operador de comparação (`gte` para maior ou igual, `lte` para menor ou igual).

**Descrição:** Retorna os países filtrados com base no percentual de mortes militares.

**Exemplo de Requisição:** `/percentual-mortes-militares?pm=50&comparison=lte`



<h3>5 - Países por Percentual de Mortes Civis em Relação a Mortes Totais</h3>

**URL:** `/percentual-mortes-civis/`

**Método:** `GET` ou `POST`

**Parâmetros:**

- `pm`: Percentual de mortes civis em relação ao total de mortes.
- `comparison`: Operador de comparação (`gte` para maior ou igual, `lte` para menor ou igual).

**Descrição:** Retorna os países filtrados com base no percentual de mortes civis.

**Exemplo de Requisição:** `/percentual-mortes-civis?pm=40&comparison=gte`