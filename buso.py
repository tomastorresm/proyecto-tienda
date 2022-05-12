from producto import Producto


class buso(Producto):
    Capota:bool
    Cremallera:bool
    Bolsillo:bool

    def __init__(self, Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto,Capota,Cremallera,Bolsillo):
        super().__init__(Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto)
        self.Capota=Capota
        self.Cremallera=Cremallera
        self.Bolsillo=Bolsillo

    