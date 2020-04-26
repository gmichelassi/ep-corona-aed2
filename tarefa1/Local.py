class Local(object):
    def __init__(self, coordenada_x, coordenada_y, frequentadores):
        self.__coordenada_x = coordenada_x
        self.__coordenada_y = coordenada_y
        self.__frequentadores = frequentadores

    def getCoordX(self):
        return self.__coordenada_x

    def getCoordY(self):
        return self.__coordenada_y

    def getFrequentadores(self):
        return self.__frequentadores
