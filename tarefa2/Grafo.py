class Grafo(object):
    def inicializar(self):
        for v in range(self.__V + 1):
            self.__adj.append([])

    def __init__(self, path='', V=5):
        self.__adj = []
        if path == '':
            self.__V = V
            self.__E = 0
            self.inicializar()
        else:
            with open(path, 'r') as file:
                self.__V = int(file.readline().rstrip('\n'))
                self.inicializar()
                self.__E = int(file.readline().rstrip('\n'))

                for n_line in range(self.__E):
                    line = file.readline().rstrip('\n')
                    v, w = line.split()
                    self.addEdge(int(v), int(w))

    def getV(self):
        return self.__V

    def getE(self):
        return self.__E

    def addEdge(self, v, w):
        self.__adj[v].append(w)
        self.__adj[w].append(v)

    def getAdj(self, v):
        return self.__adj[v]

    def degree(self, v):
        return len(self.__adj[v])

    def maxDegree(self):
        maxDegree = 0
        for i in range(self.__V):
            if self.degree(i) > maxDegree:
                maxDegree = self.degree(i)
        return maxDegree
