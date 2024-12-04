from .Reservuar import Reservuar
import math


class ReservuarShestiugolnikTreugolnik(Reservuar):
    def __init__(self, material, volume, c_coefficient):
        super().__init__(material, volume, c_coefficient)

    def compute_area_from_outer_size_and_height(self, R, H):
        sqrt3 = math.sqrt(3)
        c = self.c_coefficient

        return 3*R*H*(1 + 2*c) + R * R * sqrt3 / 2 * (1 - 6*c*c)

    def compute_outer_size_R(self, h):
        sqrt3 = math.sqrt(3)
        c = self.c_coefficient

        #R = math.sqrt(2*self.volume/(sqrt3*(1/2-3*c*c)*h))

        R = math.sqrt((4 * sqrt3 * self.volume) / (3 * h * (1 - 6*c*c)))

        return R

    def compute_area_from_height(self, h):
        R = self.compute_outer_size_R(h)

        return self.compute_area_from_outer_size_and_height(R, h)



    def optimize(self):
        sqrt3 = math.sqrt(3)
        c = self.c_coefficient

        # self.__RR = math.cbrt(2*sqrt3*(1+2*c)*self.volume/((1/2-3*c*c)*(sqrt3-6*c*c)))
        # R = self.__RR
        # self.__HH = 2*self.volume/(sqrt3*(1/2-3*c*c)*R*R)
        # H = self.__HH

        a = 1 - 6*c*c
        self.__RR = math.cbrt((4 * (1 + 2*c) * self.volume) / (a * a))
        R = self.__RR
        self.__HH = (4 * sqrt3 * self.volume) / (3 * R * R * (1 - 6*c*c))
        H = self.__HH

        self.__FF = self.compute_area_from_outer_size_and_height(R, H)
