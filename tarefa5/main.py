from Grafo import Grafo
from Transmissao import Transmissao
import random
import matplotlib.pyplot as plt

def modeloContagio(c=0.9, r=0.4):
    grafo = Grafo('traducao3.txt')
    print(f'Calculando para contagio: {c}, recuperacao: {r}')

    transmissao = Transmissao(grafo, c, r)

    status = transmissao.getStatus()
    n_passos = transmissao.getPassos()
    momentos = transmissao.getMomentos()

    labels = [i+1 for i in range(n_passos)]
    infectados, recuperados = [], []
    
    for i in range(n_passos):
        infectados.append(momentos[i]['I'])
        recuperados.append(momentos[i]['R'])

    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, infectados, width, label='Infectados')
    ax.bar(labels, recuperados, width, bottom=infectados, label='Recuperados')
    
    ax.set_ylabel('Nº de Pessoas')
    ax.set_xlabel('Nº de Passos')
    ax.set_title(f'Relação Recuperados x Infectados\nc = {c}, r = {r}')
    ax.legend()

    plt.savefig(f"./fig_{c}_{r}.png")


if __name__ == "__main__":
    # c, r = 0.8, 0.2
    # modeloContagio(c, r)

    # c, r = 0.5, 0.4
    # modeloContagio(c, r)

    c, r = 0.7, 0.6
    modeloContagio(c, r)
