from producto import Producto

class camiseta(Producto):
    TipoCuello:str
    Estampada:bool
    Botones:bool

    def __init__(self, Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto,TipoCuello,Estampada,Botones):
        super().__init__(Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto)
        self.TipoCuello=TipoCuello
        self.Estampada=Estampada
        self.Botones=Botones

