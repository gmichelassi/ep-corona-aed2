from Grafo import Grafo
from ComponentesConexas import ComponentesConexas
import sys


def analisaComponentes():
    sys.setrecursionlimit(0)
    print(sys.getrecursionlimit())
    grafo = Grafo('./OD_graph.txt')
    componentes = ComponentesConexas(grafo)
    print(str(componentes.getCount()) + " componentes")


if __name__ == '__main__':
    analisaComponentes()
