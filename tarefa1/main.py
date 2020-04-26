import pandas as pd
import time
import matplotlib.pyplot as plt
from Local import Local


def lerArquivo():
    dados = pd.read_csv('./tarefa1/OD_2017.csv')
    return dados[
        ['CO_O_X', 'CO_O_Y',
         'CO_D_X', 'CO_D_Y',
         'CO_T1_X', 'CO_T1_Y',
         'CO_T2_X', 'CO_T2_Y',
         'CO_T3_X', 'CO_T3_Y',
         'ID_PESS']
    ]


def inserirDict(coords: 'dict', x: 'str', y: 'str', id_pess: 'int'):
    if x in coords.keys():
        if y in coords[x].keys():
            if id_pess not in coords[x][y]:
                coords[x][y].append(id_pess)
        else:
            coords[x][y] = [id_pess]
    else:
        coords[x] = {y: [id_pess]}


def processar():
    coords = {}
    dados = lerArquivo()
    for index, linha in dados.iterrows():
        id_pess = linha['ID_PESS']

        if linha['CO_O_X'] != 0 and linha['CO_O_Y'] != 0:
            inserirDict(coords, '{0}'.format(linha['CO_O_X']), '{0}'.format(linha['CO_O_Y']), id_pess)

        if linha['CO_D_X'] != 0 and linha['CO_D_Y'] != 0:
            inserirDict(coords, '{0}'.format(linha['CO_D_X']), '{0}'.format(linha['CO_D_Y']), id_pess)

        if linha['CO_T1_X'] != 0 and linha['CO_T1_Y'] != 0:
            inserirDict(coords, '{0}'.format(linha['CO_T1_X']), '{0}'.format(linha['CO_T1_Y']), id_pess)

        if linha['CO_T2_X'] != 0 and linha['CO_T2_Y'] != 0:
            inserirDict(coords, '{0}'.format(linha['CO_T2_X']), '{0}'.format(linha['CO_T2_Y']), id_pess)

        if linha['CO_T3_X'] != 0 and linha['CO_T3_Y'] != 0:
            inserirDict(coords, '{0}'.format(linha['CO_T3_X']), '{0}'.format(linha['CO_T3_Y']), id_pess)

    locais = []
    freq_max = 0
    for x in coords.keys():
        for y in coords[x].keys():
            local = Local(int(x), int(y), coords[x][y])
            locais.append(local)
            if len(local.getFrequentadores()) > freq_max:
                freq_max = len(local.getFrequentadores())

    # eixo y = [1, 2, 3, 4, ..., n]
    # eixo x = [0, 0, 0, 0, ..., 0]

    eixos = {}
    for i in range(1, freq_max+1):
        eixos[i] = 0

    for local in locais:
        chave = len(local.getFrequentadores())
        eixos[chave] += 1

    eixos = {x: y for x, y in eixos.items() if y != 0}

    eixo_y = eixos.values()     # n LUGARES
    eixo_x = eixos.keys()       # FREQUENTADOS por m pessoas

    plt.figure(figsize=(21.0, 9))
    plt.bar(x=[i for i in range(1, len(eixo_x)+1)], height=eixo_y, log=True)
    plt.xticks([i for i in range(1, len(eixo_x)+1)], labels=eixo_x, rotation='vertical')
    plt.title("RELAÇÃO ENTRE FREQUENTADORES E LUGARES FREQUENTADOS")
    plt.xlabel("Nro de frequentadores")
    plt.ylabel("Qtd de lugares")

    plt.savefig("./fig.png")


if __name__ == '__main__':
    start_time = time.time()
    processar()
    print("--- Total execution time: %s minutes ---" % ((time.time() - start_time) / 60))
