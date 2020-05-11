from Grafo import Grafo
from ComponentesConexas import ComponentesConexas
import sys


def analisaComponentes():
    sys.setrecursionlimit(1500)     # Aumentar o limite de recursão do python
    grafo = Grafo('./cenarios/cenario3.txt')
    cc = ComponentesConexas(grafo)
    numberOfComponents = cc.getCount()

    print(str(numberOfComponents) + " componentes")
    
    componentes = []
    # inicializa
    for i in range(numberOfComponents):
        componentes.append([])
        
    # preenche
    for v in range(grafo.getV()):
        componenteDeV = cc.getId(v)
        componentes[componenteDeV].append(v)

    tabela = {}

    for i in range(numberOfComponents):
        size = len(componentes[i])

        if size in tabela:
            tabela[size] += 1
        else:
            tabela[size] = 1
    
    print('-' * 35)
    for chave in sorted(tabela, key = tabela.get):
        tamanho = chave
        qtdComponentes = tabela[chave]
        print(f'{qtdComponentes:^5} componentes com {tamanho:^4} vertices')

    print('-' * 35)

if __name__ == '__main__':
    analisaComponentes()


    
