# Componenteas conexas do grafo dos encontros

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

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

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

## Alunos

- [Ana Beatriz Machado Cuelbas](https://github.com/anabcuelbas) - 11207881
- [Gabriel de Castro Michelassi](https://github.com/gmichelassi) - 11208162
- [Guilherme Balog Gardino](https://github.com/GuilhermeBalog) - 11270649
- [Laura Zitelli de Souza](https://github.com/LauraZitelli) - 11207814

O repositório está disponivel no GitHub em [https://github.com/gmichelassi/ep-corona-aed2](https://github.com/gmichelassi/ep-corona-aed2)
