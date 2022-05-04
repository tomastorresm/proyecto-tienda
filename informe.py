from datetime import date
from producto import Producto
from venta import Venta
from inventario import Inventario

class Informe:
    FechaInicial:date
    FechaFinal:date
    CantidadVendidaProducto:int
    CantidadTotalVendida:int
    TotalDinero:float
    Producto:Producto
    Venta:Venta
    Inventario:Inventario

    def __init__(self,Producto):
        self.Producto=Producto
    def __init__(self,Venta):
        self.Venta=Venta
    def __init__(self,Inventario):
        self.Inventario=Inventario

    
    


