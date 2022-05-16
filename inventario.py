from producto import Producto
from administrador import Administrador

class Inventario:
    CantidadEntrada:int
    CantidadSalida:int
    Precio:float
    CantidadTotalProductos:int
    Producto:Producto
    Administrador:Administrador

    def __init__(self,Producto,CantidadEntrada,CantidadSalida,Precio,CantidadTotalProducto,Administrador):
        self.CantidadEntrada=CantidadEntrada
        self.CantidadSalida=CantidadSalida
        self.Precio=Precio
        self.CantidadTotalProductos
        self.Producto=Producto
        self.Administrador=Administrador    
