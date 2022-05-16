
from producto import Producto
from vendedor import Vendedor


class Venta:
    Producto:Producto
    CantidadProducto:int
    TotalPagar:float
    Vendedor:Vendedor

    def __init__(self,Producto,CantidadProducto,Totalpagar,Vendedor):
        self.CantidadProducto=CantidadProducto
        self.TotalPagar=Totalpagar
        self.Vendedor=Vendedor
        self.Producto=Producto
        self.Vendedor=Vendedor
