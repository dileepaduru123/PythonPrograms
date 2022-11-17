from multipul_Inharitance.Parent1File import Parent1File
from multipul_Inharitance.ParentFile import ParentFile


class Children(ParentFile, Parent1File):
    def __init__(self, cars, bikes, bus, houses, lands, money):
        ParentFile.__init__(self,cars,bikes,bus)
        Parent1File.__init__(self, houses, lands, money)




