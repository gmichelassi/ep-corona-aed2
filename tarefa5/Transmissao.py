from random import random, randint, seed

class Transmissao(object):
    def __init__(self, grafo, c, r):
        self.__status = []
        self.__c = c
        self.__r = r
        
        self.__passos = []

        # Inicializar
        for i in range(grafo.getV()):
            self.__status.append("S")

        # Paciente zero
        vertice_infectado = 0
        self.__status[vertice_infectado] = "I"
        

        quantidades = { 'S': grafo.getV() - 1, 'I': 1, 'R': 0 }      
        self.__passos.append(quantidades.copy())
        # print(f'Passos {self.__passos}')
        # print(f'passos[{0}]:{quantidades} ', end=" -->> ")
        # print(f'passos[{0}]:{self.__passos[0]} ')

        cont = 0
        while quantidades['I'] != 0:
            if self.__status[vertice_infectado] != "I":
                for i in range(len(self.__status)):
                    if self.__status[i] == "I":
                        vertice_infectado = i
                        break
            
            quantidades = self.__dfs(grafo, vertice_infectado, quantidades)
            # self.__passos.append(quantidades.copy())
            # print(f'passos[{cont + 1}]:{quantidades} ', end=" -->> ")
            # print(f'passos[{cont + 1}]:{self.__passos[cont + 1]} ')
            cont += 1

        print(f"\nwhile rodou {cont} vezes")


    def __dfs(self, grafo, v, quantidades):        
        if self.__status[v] == "I":
            prob_recuperacao = random() # Já sorteia entre 0 e 1 por padrão
            if prob_recuperacao < self.__r:
                self.__status[v] = "R"
#                print(f'{v} se recuperou')
                quantidades['I'] -= 1
                quantidades['R'] += 1
            else:
                for w in grafo.getAdj(v):
                    if self.__status[w] == "S":
                        prob_contagio = random()

                        if prob_contagio <= self.__c:
                            self.__status[w] = "I"
                            quantidades['I'] += 1
                            quantidades['S'] -= 1
                            quantidades = self.__dfs(grafo, w, quantidades)
        
        self.__passos.append(quantidades.copy())
        return quantidades

    
    def getStatus(self):
        return self.__status

    def getPassos(self):
        return self.__passos
