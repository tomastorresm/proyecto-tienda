from heapq import nsmallest
from producto import Producto
from bodega import Bodega

class UbicacionProducto:
    Bodega:Bodega
    Producto:Producto
    NumeroStand:int
    Fila:int
    Columna:int

    def __init__(self,Bodega,Producto,NumeroStand,Fila,Columna):
        self.NumeroStand=NumeroStand
        self.Fila=Fila
        self.Columna=Columna
        self.Bodega=Bodega
        self.Producto=Producto
