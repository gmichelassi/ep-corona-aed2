from Grafo import Grafo
from BreadthFirstSearch import BuscaEmLargura
import matplotlib.pyplot as plt
import time
import numpy as np

a
def diametro():
    grafo = Grafo('traducao3.txt')

    # dicio = { tamanho: quantidade }

    dicio = {}
    for i in range(grafo.getV()):
        bfs = BuscaEmLargura(grafo, i)

        for j in range(grafo.getV()):
            if i != j: 
                pilha = bfs.pathTo(j)

                if pilha != []:
                    distancia = pilha.size() - 1

                    # print(f'Entre {i} e {j} = {distancia}')
                    if distancia in dicio.keys():
                        dicio[distancia] += 1
                    else:
                        dicio[distancia] = 1
    
    orderedDict, soma, pesos = {}, 0, 0
    chaves = sorted(dicio)
    
    for chave in chaves:
        orderedDict[chave] = int(dicio[chave] / 2)
        soma += chave * orderedDict[chave]
        pesos += orderedDict[chave]

    media = soma / pesos
    print(f'Diâmetro médio: {media}')
    
    eixo_x = orderedDict.keys()
    eixo_y = orderedDict.values()

    plt.figure(figsize=(15.0, 9))
    plt.bar(x=[i for i in range(1, len(eixo_x) + 1)], height=eixo_y, log=True)
    plt.xticks([i for i in range(1, len(eixo_x) + 1)], labels=eixo_x, rotation='vertical')
    plt.title("Quantidade de distâncias entre pares de nós (sem repetição)")
    plt.xlabel("Distância")
    plt.ylabel("Quantidade")

    # plt.show()
    plt.savefig("./fig.png")

    

if __name__ == "__main__":
    start_time = time.time()
    diametro()
    print("--- Total execution time: %s seconds ---" % ((time.time() - start_time)))
