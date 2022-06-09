
from operator import concat
from unidad import *


class Jugador():
    "Un Jugador tiene un nombre, puntos_vida, monedas y unidades. Un jugador no puede deudas, es decir, no puede tener un numero de monedas negativo"

    def __init__(self, nombre, puntos_vida=20):
        self.nombre = nombre
        self._puntos_vida = puntos_vida
        self.monedas = 10
        self.unidades = []

    @property
    def puntos_vida(self):
        return self._puntos_vida

    @puntos_vida.setter
    def puntos_vida(self, puntos):
        self._puntos_vida = puntos
    
    def descansar(self):
        """Hace que la primera unidad, si la hay, descanse"""
        if len(self.unidades) > 0:
            self.unidades[0].descansar()

    def get_monedas(self):
        """Devuelve el numero de monedas actual del jugador"""
        return self.monedas

    def set_monedas(self, value):
        """Modifica el numero de monedas por el valor value"""
        if value >= 0:
            self.monedas = value
        pass
