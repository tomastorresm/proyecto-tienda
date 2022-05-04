
from producto import Producto
from vendedor import Vendedor


class Venta:
    Producto:Producto
    CantidadProducto:int
    TotalPagar:float
    Vendedor:Vendedor

    def __init__(self,Producto):
        self.Producto=Producto
    def __init__(self,Vendedor):
        self.Vendedor=Vendedor
