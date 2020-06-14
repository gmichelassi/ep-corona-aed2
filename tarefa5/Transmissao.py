from random import random, randint, seed

class Transmissao(object):
    def __init__(self, grafo, c, r):
        self.__status = []
        self.__c = c
        self.__r = r
        
        self.__momentos = []

        # Inicializar
        for i in range(grafo.getV()):
            self.__status.append("S")

        # Paciente zero
        
        vertice_inicial = 178
        self.__status[vertice_inicial] = "I"
        self.__dfs(grafo, vertice_inicial)

        

    def __dfs(self, grafo, v):        
        if self.__status[v] == "I":
            prob_recuperacao = random() # Já sorteia entre 0 e 1 por padrão
            if prob_recuperacao <= self.__r:
                self.__status[v] = "R"
            else:
                for w in grafo.getAdj(v):
                    if self.__status[w] == "S":
                        prob_contagio = random()

                        if prob_contagio <= self.__c:
                            self.__status[w] = "I"
                            self.__dfs(grafo, w)
        
        quantidades = {'S': 0, 'I': 0, 'R': 0}
        for s in self.__status:
            quantidades[s] += 1

        self.__momentos.append(quantidades)

    
    def getStatus(self):
        return self.__status

    def getMomentos(self):
        return self.__momentos

    def getPassos(self):
        return len(self.__momentos)
