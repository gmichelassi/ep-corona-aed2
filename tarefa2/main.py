from Grafo import Grafo
import matplotlib.pyplot as plt


def gerarGrafo():
    grafo = Grafo('./tarefa2/OD_graph.txt')

    eixos = {}
    for i in range(grafo.maxDegree() + 1):
        eixos[i] = 0

    for vertice in range(grafo.getV()):
        chave = grafo.degree(vertice)
        eixos[chave] += 1

    eixos = {x: y for x, y in eixos.items() if y != 0}

    eixo_x = eixos.keys()
    eixo_y = eixos.values()

    plt.figure(figsize=(50.0, 9))
    plt.bar(x=[i for i in range(1, len(eixo_x) + 1)], height=eixo_y, log=True)
    plt.xticks([i for i in range(1, len(eixo_x) + 1)], labels=eixo_x, rotation='vertical')
    plt.title("ENCONTROS PRESENCIAIS DA RMSP")
    plt.xlabel("Grau dos vértices")
    plt.ylabel("Qtd de vértices")

    plt.savefig("./tarefa2/fig.png")


if __name__ == '__main__':
    gerarGrafo()
