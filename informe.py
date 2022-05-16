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

    def __init__(self,FechaInicial,FechaFinal,CantidadVendidaProducto,CantidadTotalVendida,TotalDinero,Producto,Venta,Inventario):
        self.Producto=Producto
        self.Venta=Venta
        self.Inventario=Inventario
        self.FechaInicial=FechaInicial
        self.FechaFinal=FechaFinal
        self.CantidadVendidaProducto=CantidadVendidaProducto
        self.CantidadTotalVendida=CantidadTotalVendida
        self.TotalDinero=TotalDinero

    
    


