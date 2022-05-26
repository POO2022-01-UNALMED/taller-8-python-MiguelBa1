class Deportista:
    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
        self._añosPracticados = añosPracticando

    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._añosPracticados

    def setDeporte(self, deporte):
        self._deporte = deporte

    def setAñosPracticados(self, añosPracticando):
        self._añosPracticados = añosPracticando
