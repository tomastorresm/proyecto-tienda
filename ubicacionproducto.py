from producto import Producto
from bodega import Bodega

class UbicacionProducto:
    Bodega:Bodega
    Producto:Producto
    NumeroStand:int
    Fila:int
    Columna:int

    def __init__(self,Bodega):
        self.Bodega=Bodega
    def __init__(self,Producto):
        self.Producto=Producto
