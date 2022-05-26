from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Futbolista.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    @staticmethod
    def  getListaFutbolistas() :
        return Futbolista.listaFutbolistas

    @staticmethod
    def setListaFutbolistas( listaFutbolistas) :
        Futbolista.listaFutbolistas = listaFutbolistas

    def  getGolesMarcados(self) :
        return self._golesMarcados

    def setGolesMarcados(self, _golesMarcados) :
        self._golesMarcados = _golesMarcados

    def  getTarjetasRojas(self) :
        return self._tarjetasRojas

    def set_tarjetasRojas(self, _tarjetasRojas) :
        self._tarjetasRojas = _tarjetasRojas

    def  getPiernaHabil(self) :
        return self._piernaHabil

    def setPiernaHabil(self, _piernaHabil) :
        self._piernaHabil = _piernaHabil
