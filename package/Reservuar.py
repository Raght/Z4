from enum import Enum
from abc import ABC, abstractmethod
import math


class Shape:
    CIRCLE = "circle"
    TRIANGLE = "triangle"
    SQUARE = "square"
    PENTAGON = "pentagon"
    HEXAGON = "hexagon"


class Material:
    STEEL = "Сталь ХВГ"
    TITANIUM_ALLOY = "Титановый сплав Т12"
    BRASS = "Латунь 113"
    ALUMINIUM_ALLOY = "Алюминиевый сплав А231"
    POLYMER_COMPOSITE = "Полимерный композит ПК 421"


class Subscriptable(type):
    items: list = []

    def __getitem__(cls, i):
        return cls.items[i]


class Reservuar(metaclass=Subscriptable):
    items = []

    def __init__(self, material, volume, c_coefficient):
        super().__init__()
        self.__material = material
        self.__volume = volume
        self.__c_coefficient = c_coefficient
        self.__HH = 0
        self.__RR = 0
        self.__FF = 0

    @property
    def material(self):
        return self.__material

    @property
    def volume(self):
        return self.__volume

    @property
    def c_coefficient(self):
        return self.__c_coefficient

    @property
    def height(self):
        return self.__HH

    @property
    def outer_size(self):
        return self.__RR

    @property
    def surface_area(self):
        return self.__FF

    @abstractmethod
    def optimize(self):
        pass

