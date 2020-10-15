# coding: utf-8
__author__ = 'CotherArt'


class Vector:

    def __init__(self, cords):
        self.cordenadas = tuple(cords)

    def get_cords(self):
        return self.cordenadas

    # def __init__(self):
    #     self.inicio = (0, 0)
    #     self.final = (0, 0)
    #     self.scalar = 0

    # def __init__(self, x1=0, y1=0, x2=0, y2=0):
    #     self.inicio = (x1, y1)
    #     self.final = (x2, y2)
    #     self.scalar = 0

    # def __init__(self, inicio=(0, 0), final=(0, 0)):
    #     self.inicio = inicio
    #     self.final = final
    #     self.scalar = 0