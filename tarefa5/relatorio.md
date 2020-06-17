# Contágio SIR

Para contruir uma simulação de contágio do Coronavírus na Região Metropolitana da Cidade de São Paulo, nos basemos no modelo epidemiológico SIR (Susceptible, Infected, Removed), considerando dois paramêtros: a probabilidade de contágio e a probabilidade de recuperação.

A fim de construir um modelo de contágio semelhante ao mencionado acima utilizamos os cenários preparados e estudados anteriormente e utilizamos alguns algoritmos explorados em aula.

Primeiramente, ao carregar a componente gigante do grafo dos encontros, todos os vértices foram marcados como suscetíveis (S) e aleatoriamente foi escolhido um vértice inicial (uma pessoa) para ser marcada como infectada (I). Para manter a consistência dos testes, o vértice inicial foi mantido para todos os seguintes testes.

A partir disso, tendo uma pessoa infectada, foi executada uma Busca em Profundidade (*Depth First Search*, DFS) para percorrer todo o grafo, partindo do vértice infectado inicial. Dessa forma, os vértices adjascentes ao mesmo, foram as pessoas que tiveram contato com a infectada, portanto tendo uma certa probabilidade *c* de contágio. Uma pessoa infectada também poderia, eventualmente, se recuperar, com uma dada probabilidade *r*.

O algoritmo então verifica: para uma pessoa infectada, primeiro verificamos se ela se recuperou (sorteando um número *0 <= N < 1*, e verificando se N <= *r*, então ela se recuperou), neste caso, evitando de contaminar outras pessoas com a doença; caso contrário, se ela entrou em contato com pessoas sucetíveis a se infectar, então veríficamos se houve o contágio (sorteando um número *0 <= M < 1*, e verificando se M <= *c*, então ela se recuperou). Esse algoritmo é repetido para todos os vértices do grafo e suas listas de adjascências.







Com os parâmetros c e r fixos, o que deve ocorrer nos diferentes cenários
que investigamos?

## c, r = 0.8, 0.2

<p style="text-align: center">
  <img src="fig_0.8_0.2.png" style="width: 80%" />
</p>

## c, r = 0.5, 0.4

<p style="text-align: center">
  <img src="fig_0.5_0.4.png" style="width: 80%" />
</p>

## c, r = 0.7, 0.6

<p style="text-align: center">
  <img src="fig_0.7_0.6.png" style="width: 80%" />
</p>

## Alunos

- [Ana Beatriz Machado Cuelbas](https://github.com/anabcuelbas) - 11207881
- [Gabriel de Castro Michelassi](https://github.com/gmichelassi) - 11208162
- [Guilherme Balog Gardino](https://github.com/GuilhermeBalog) - 11270649
- [Laura Zitelli de Souza](https://github.com/LauraZitelli) - 11207814

O repositório está disponivel no GitHub em [https://github.com/gmichelassi/ep-corona-aed2](https://github.com/gmichelassi/ep-corona-aed2)
