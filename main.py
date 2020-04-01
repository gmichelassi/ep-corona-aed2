import pandas as pd
import Local


def lerArquivo():
    dados = pd.read_csv('OD_2017.csv')
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
        inserirDict(coords, '{0}'.format(linha['CO_O_X']), '{0}'.format(linha['CO_O_Y']), id_pess)
        inserirDict(coords, '{0}'.format(linha['CO_D_X']), '{0}'.format(linha['CO_D_Y']), id_pess)

        if linha['CO_T1_X'] != 0 and linha['CO_T1_Y'] != 0:
            print('entrou 1')
            inserirDict(coords, '{0}'.format(linha['CO_T1_X']), '{0}'.format(linha['CO_T1_Y']), id_pess)

        if linha['CO_T2_X'] != 0 and linha['CO_T2_Y'] != 0:
            print('entrou 2')
            inserirDict(coords, '{0}'.format(linha['CO_T2_X']), '{0}'.format(linha['CO_T2_Y']), id_pess)

        if linha['CO_T3_X'] != 0 and linha['CO_T3_Y'] != 0:
            print('entrou 3')
            inserirDict(coords, '{0}'.format(linha['CO_T3_X']), '{0}'.format(linha['CO_T3_Y']), id_pess)
    print(coords)


if __name__ == '__main__':
    processar()
