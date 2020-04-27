# Transmissão de Corona Vírus na RMSP

Trabalhos desenvolvidos para a disciplina AED2, com o objetivo de aplicar os conceitos de Algoritmos e Estruturas de dados, como Grafos, análise assintótica e processamento de dados no contexto da transmissão de corona vírus na Região Metropolitana de São Paulo. 

- [Processando dados da pesquisa Origem Destino](/tarefa1)
- [Construindo um grafo de encontros presenciais da RMSP](/tarefa2)

## Como rodar os programas

**Requisitos:**

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/) (gerenciador de pacotes)

Por questões de compatibilidade, recomendamos instalar o `virtualenv`, basta executar o seguinte comando na pasta do projeto:

```bash
pip install virtualenv
```

Com o virtualenv instalado, execute:

```bash
virtualenv venv
```

E então instale os pacotes listados nos requerimentos:

```bash
pip install -r requirements.txt
```

Uma vez que tudo está instalado, basta rodar o programa desejado (normalmente é o `main.py`).

Por exemplo para a [primeira tarefa](/tarefa1), com o comando

```bash
cd tarefa1
python main.py
```

> **Atenção:** Em alguns sistemas em que tanto o pyhton 2 quanto o python 3 estão instalados, os comandos `python` e `pip` devem ser substituídos respectivamente por `python3` e `pip3`

## Autores

Esse é um trabalho desenvolvido pelos alunos
- [Ana Beatriz Machado Cuelbas](https://github.com/anabcuelbas)
- [Gabriel de Castro Michelassi](https://github.com/gmichelassi)
- [Guilherme Balog Gardino](https://github.com/GuilhermeBalog)
- [Laura Zitelli de Souza](https://github.com/LauraZitelli)

Como trabalho proposto pelo professor [Márcio Moretto Ribeiro](http://lattes.cnpq.br/2153927915438535)