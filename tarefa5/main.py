from Grafo import Grafo
from Transmissao import Transmissao
import random
import matplotlib.pyplot as plt
import sys

def modeloContagio(c=0.9, r=0.4):
    grafo = Grafo('traducao3.txt')
    print(f'Calculando para contagio: {c}, recuperacao: {r}')

    transmissao = Transmissao(grafo, c, r)

    status = transmissao.getStatus()
    passos = transmissao.getPassos()
    n_passos = len(passos)

    # print(passos)
    # print(n_passos)
    cont = 0
    for passo in passos:
        # print(f"Tamanho das barras: {passo['I'] + passo['R']}")
        cont += 1
        if cont > 10:
            break


    labels = [i+1 for i in range(n_passos)]
    infectados, recuperados = [], []
    
    for i in range(n_passos):
        infectados.append(passos[i]['I'])
        recuperados.append(passos[i]['R'])

    width = 0.35
    print("Gerando gráfico...")
    fig, ax = plt.subplots(figsize=(30.0, 10.0))

    ax.bar(labels, infectados, width, label='Infectados')
    ax.bar(labels, recuperados, width, bottom=infectados, label='Recuperados')
    
    ax.set_ylabel('Nº de Pessoas', fontsize=25)
    ax.set_xlabel('Nº de Passos', fontsize=25)
    ax.set_title(f'Relação Recuperados x Infectados\nc = {c}, r = {r}', fontsize=25)
    ax.legend(fontsize=25)

    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.savefig(f"./fig_{c}_{r}.png")


if __name__ == "__main__":
    sys.setrecursionlimit(2500)
    c, r = 0.5, 0.4
    modeloContagio(c, r)

    # c, r = 0.7, 0.1
    # modeloContagio(c, r)

    # c, r = 0.9, 0.2
    # modeloContagio(c, r)
