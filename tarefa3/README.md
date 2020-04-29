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
