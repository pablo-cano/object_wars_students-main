from abc import ABC, abstractmethod

from numpy import recarray

MAX_VIDA = 10

class Unidad(ABC):
    """Clase abstracta que modela una unidad"""

    def __init__(self):
        """Creadora del objecto Unidad"""
        self._puntos_vida = MAX_VIDA
        self.monedas = 0
        self._puntos_ataque = 0
        self.puntos_restaura = 0

    @abstractmethod
    def descansar(self):
        """ Metodo abastracto, restaura puntos de vida a la unidad"""
        if (self._puntos_vida + self.puntos_restaura) > MAX_VIDA:
            self._puntos_vida = MAX_VIDA
        else:
            self._puntos_vida += self.puntos_restaura

    def atacar(self):
        """Este metodo debe ser usado para consultar los puntos de ataque, en caso de que la unidad este atacando"""
        return self._puntos_ataque

    @property
    def puntos_vida(self):
        return self._puntos_vida

    @puntos_vida.setter
    def puntos_vida(self, puntos):
        if self._puntos_vida + puntos > 0:
            self._puntos_vida = puntos
        else:
            self._puntos_vida = 0

class Soldado(Unidad):
    """Unidad soldado, tiene un coste de 5 monedas, tiene 3 puntos de ataque y restaura 5 puntos de vida al descansar"""
    def __init__(self):
        Unidad.__init__(self)
        self.monedas = 5
        self._puntos_ataque = 3
        self.puntos_restaura = 5
    def descansar(self):
        return super().descansar()

class Arquero(Unidad):
    """ Unidad Arquero, tiene un coste de 6 monedas, tiene 8 puntos de ataque y restaura 2 puntos de vida al decansar
    Los arqueros atacan 1 de cada 2 veces ya que deben recargar, empiezan la partida sin estar preparados para atacar"""
    def __init__(self):
        Unidad.__init__(self)
        self.monedas = 6
        self._puntos_ataque = 8
        self.puntos_restaura = 2
        self.recarga = True
    def atacar(self):
        if self.recarga == False:
            self.recarga = not self.recarga
            return self._puntos_ataque      
        else:
            self.recarga = not self.recarga
            return 0  

    def descansar(self):
        return super().descansar()

class Caballero(Unidad):
    """ Unidad Caballero, tiene un coste de 9 monedas, tiene 5 puntos de ataque, y al descansar no restaura puntos de vida"""
    def __init__(self):
        Unidad.__init__(self)
        self.monedas = 9
        self._puntos_ataque = 5
        self.puntos_restaura = 0
    def descansar(self):
        return super().descansar()