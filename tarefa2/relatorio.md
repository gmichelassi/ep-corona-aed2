# Construindo um grafo de encontros presenciais da RMSP

Optamos novamente pela linguagem python, pois mais uma vez precisamos plotar dados de maneira semelhante à primeira tarefa.

Escolhemos o cenário **1**, em que tudo está funcionando.

Primeiramente fizemos nossa implementação de Grafo com a representação em lista de adjacência e métodos úteis, baseado no livro de referência *Algorithms, 4th Edition*, fazendo as alterações necessárias, pois os autores implementam em Java.

As duas maiores diferenças foram a utilização das listas do python, que funcionam como listas ligadas, e a leitura de arquivo.

Para gerar o gráfico, criamos o Grafo a partir do arquivo OD_graph.txt que contém as informações necessárias:

- O número de vértices `V`
- O número de arestas (edges) `E`
- Os pares de vértices que representam cada aresta

Para os fazer eixos do gráfico, iteramos sobre os vértices do grafo e computamos o grau de cada um com o método `degree()`, e com a biblioteca matplotlib geramos o seguinte gráfico:

![Encontros Presenciais da RMSP](fig.png)

O gráfico utiliza escala logarítmica devido a grande diferença entre os maiores valores e os menores.

## Alunos

- [Ana Beatriz Machado Cuelbas](https://github.com/anabcuelbas) - 11207881
- [Gabriel de Castro Michelassi](https://github.com/gmichelassi) - 11208162
- [Guilherme Balog Gardino](https://github.com/GuilhermeBalog) - 11270649
- [Laura Zitelli de Souza](https://github.com/LauraZitelli) - 11207814

O repositório está disponivel no GitHub em [https://github.com/gmichelassi/ep-corona-aed2](https://github.com/gmichelassi/ep-corona-aed2)
