from producto import Producto

class pantalon(Producto):
    TipoTela:str
    Rotos:bool
    Tipo:str

    def __init__(self, Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto,TipoTela,Rotos,Tipo):
        super().__init__(Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto)
        self.TipoTela=TipoTela
        self.Rotos=Rotos
        self.Tipo=Tipo
