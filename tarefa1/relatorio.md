# Processando dados da pesquisa Origem Destino

Decidimos usar a linguagem python pois existem bibliotecas específicas para processamento e plotagem de dados.

Primeiramente utilizamos a biblioteca pandas, para carregar o arquivo `OD_2017.csv` em uma estrutura do pandas chamda `dataframe` e selecionamos apenas as colunas da tabela que nos interessam:

- Coordenadas X e Y da Origem
- Coordenadas X e Y do Destino
- Coordenadas X e Y das Transferências
- ID da Pessoa

E então iteramos sobre as linhas da tabela para criar um `dicionário` (estrutura da linguagem, no formato chave valor), com o seguinte formato:

```json
{
  "x1": {
    "y1": [
      "id1",
      "id2"
    ],
    "y2": [
      "id1",
      "id3"
    ]
  }
}
```

Com essa estrutura formada, podemos iteram sobre os seus itens e fazer uma lista de `Locais` (classe que criamos conforme a especificação da tarefa) e a partir dessa lista contamos o número de frequentadores por local

Uma vez que temos todos os dados necessários, podemos plotar o gráfico com a biblioteca matplotlib:

![Gráfico Gerado](fig.png)

### Tempo de execução

Em números absolutos, rodando em um computador com a seguinte configuração

- **Sistema Operacional:** Ubuntu 18.04.4 64bits  
- **Memória:** 3,6 GiB
- **Processador:** Intel® Core™ i5-7200U CPU @ 2.50GHz × 4 
- **Placa Gráfica:** Intel® HD Graphics 620 (Kaby Lake GT2)

O tempo de execução é de aproximadamente 45 segundos

Em nossos testes percebemos que a resolução do gráfico influencia bastante no tempo de execução

Pensando em complexidade assintótica, em termos de número de entrevistados **`e`** e número de locais **`l`**, temos os seguintes passos:

- Iteramos uma vez sobre a tabela da pesquisa, que tem **`e`** linhas para construir o dicionário mencionado
- Iteramos sobre esse dicionário que contém os **`l`** locais
- Iteramos sobre a lista de **`l`** locais para plotar o gráfico

Então temos o tempo de **`e + 2l`**, mas em termos de complexidade podemos desprezar a constante **`2`**, então a complexidade é de **`e + l`** 

## Alunos

- [Ana Beatriz Machado Cuelbas](https://github.com/anabcuelbas) - 11207881
- [Gabriel de Castro Michelassi](https://github.com/gmichelassi) - 11208162
- [Guilherme Balog Gardino](https://github.com/GuilhermeBalog) - 11270649
- [Laura Zitelli de Souza](https://github.com/LauraZitelli) - 11207814

O repositório está disponivel no GitHub em [https://github.com/gmichelassi/ep-corona-aed2](https://github.com/gmichelassi/ep-corona-aed2)
