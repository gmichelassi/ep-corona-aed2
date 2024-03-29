# Componentes conexas do grafo dos encontros

## Introdução ao Problema

Vimos que podemos podemos implementar um grafo de três maneiras diferentes 
e que essa escolha muda a eficiência em termos de tempo de processamento das operações 
básicas em grafos e espaço na memória.
Para testar nossos novos conhecimentos, construímos o [grafo dos encontros](../tarefa2/) 
entre entrevistados na pesquisa [Origem/Destino](http://www.metro.sp.gov.br/pesquisa-od/) 
e calculamos o [histograma](../tarefa2/fig.png) do número de entrevistados que frequentam os mesmos lugares.

Vimos uma técnica recursiva simples para “passear” por um grafo chamada *busca em profundidade*. 
Essa técnica é eficaz para extrair informações importantes sobre o grafo que estamos estudando. 
Em particular, com uma busca em profundidade somos capazes de testar se um grafo é conexo, 
ou seja, se entre quaisquer dois nós existe um caminho entre eles.
Caso o grafo não seja conexo, uma sequência de buscas em profundidade 
pode nos indicar quantas *componentes conexas* o grafo possui.

Em nosso exemplo, uma pessoa infecta outras apenas quando há um encontro entre elas. 
Assim, uma pessoa nunca infectará outra que esteja fora de sua componente conexa. 
Daí a importância de estudar essa propriedade.

## Tarefa

A terceira tarefa consiste em implementar a busca em profundidade 
para computar o número e o tamanho das componentes conexas no grafo construído na tarefa anterior. 
O relatório deve conter uma tabela indicando quantos entrevistados estão isolados, 
quantas componentes existem de tamanho 2, quantas existem de tamanho 3 etc. 
Façam uma tabela e não um gráfico e omitam os tamanhos em que não há nenhuma componente.

Provavelmente haverá uma componenete muito maior do que as demais.
Essa é chamada de *componente gigante*. 
No nosso caso, quanto maior a componente gigante, mais pessoas estão suscitíveis a serem contaminadas.
Dos cenários considerados pelos grupos, qual será que tem maior componente gigante?

## Solução

Escolhemos o **cenário 3**, em que apenas serviços essenciais estão abertos: incluem apenas a casa, trajetos com finalidade de saúde e assuntos pessoais.

Utilizando nossa [implementação de grafo](Grafo.py), fizemos o algoritmo de [busca em profundidade](ComponentesConexas.py), analisando as componentes conexas.

Como o grafo tem muitas arestas e o algoritmo é recursivo, precisamos aumentar o limite de recursões do python:

```python
sys.setrecursionlimit(1500)
```

Para saber o tamanho das componentes fazemos uma lista em que cada posição é uma componente, representada como a lista de seus vértices:

```plain
componente 0 : [441,  801,  835, ...]
componente 1 : [294,  347,  397, ...]
componente 2 : [346,  359,  131, ...]
componente 3 : [517,  506,  505, ...]
...
```

Desta forma para saber o tamanho de um componente basta saber o tamanho da lista que o representa, utilizando a função `len()`

Para agrupar as componentes de mesmo tamanho, usamos novamente a estratégia de dicionário, utilizando a o tamanho como chave e a quantidade de componentes como valor.

```js
{
  '1': 81137, 
  '2': 719, 
  '3': 198, 
  '2368': 1, 
  ...
}
```

Com isso tivemos o seguinte resultado:

|                     82193 componentes conexas                      |
| :----------------------------------------------------------------: |
| **1** componente com **2368** entrevistados (*componente gigante*) |
|             **1** componente com **29** entrevistados              |
|             **1** componente com **16** entrevistados              |
|             **1** componente com **10** entrevistados              |
|             **1** componente com **11** entrevistados              |
|             **2** componentes com **20** entrevistados             |
|             **2** componentes com **14** entrevistados             |
|             **4** componentes com **8** entrevistados              |
|             **5** componentes com **9** entrevistados              |
|             **9** componentes com **7** entrevistados              |
|             **16** componentes com **6** entrevistados             |
|             **27** componentes com **5** entrevistados             |
|             **69** componentes com **4** entrevistados             |
|            **198** componentes com **3** entrevistados             |
|            **719** componentes com **2** entrevistados             |
|                **81137** entrevistados **isolados**                |
