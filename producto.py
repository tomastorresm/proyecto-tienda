class Producto:
    Referencia: int
    NombreProducto:str
    ValorProducto:float
    Talla:float
    Genero:bool
    CantidadProducto:int

    def __init__(self,Referencia,NombreProducto,ValorProducto,Talla,Genero,CantidadProducto):
        self.Referencia=Referencia
        self.NombreProducto=NombreProducto
        self.ValorProducto=ValorProducto
        self.Talla=Talla
        self.Genero=Genero
        self.CantidadProducto=CantidadProducto

