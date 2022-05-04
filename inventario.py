from producto import Producto
from administrador import Administrador

class Inventario:
    CantidadEntrada:int
    CantidadSalida:int
    Precio:float
    CantidadTotalProductos:int
    Producto:Producto
    Administrador:Administrador

    def __init__(self,Producto):
        self.Producto=Producto
    def __init__(self,Administrador):
        self.Administrador=Administrador    
