class ComponentesConexas(object):
    def __init__(self, grafo):
        self.__count = 0
        self.__marked = []
        self.__id = []

        for i in range(grafo.getV()):
            self.__id.append(-1)
            self.__marked.append(False)

        for i in range(grafo.getV()):
            if not self.__marked[i]:
                self.__dfs(grafo, i)
                self.__count += 1

    def __dfs(self, grafo, v):
        self.__marked[v] = True
        self.__id[v] = self.__count
        for w in grafo.getAdj(v):
            if not self.__marked[w]:
                self.__dfs(grafo, w)

    def isConnected(self, v, w):
        return self.__id[v] == self.__id[w]

    def getId(self, v):
        return self.__id[v]

    def getCount(self):
        return self.__count
