from datetime import date
from informaciontienda import InformacionTienda
from venta import Venta
from producto import Producto
from vendedor import Vendedor
from cliente import Cliente


class DatoFactura:
    Fecha:date
    NombreTienda:str
    NumeroDeFactura:int
    Cliente:Cliente
    TelefonoTienda:int
    Vendedor:Vendedor
    Producto:Producto
    NumeroFactura:int
    Venta:Venta
    MetodoPago:str
    InformacionTienda: InformacionTienda

    def __init__(self,Cliente):
        self.Cliente=Cliente
    def __init__(self,Vendedor):
        self.Vendedor=Vendedor
    def __init__(self,Producto):
        self.Producto=Producto
    def __init__(self,Venta):
        self.Venta=Venta 
    def __init__(self,InformacionTienda):
        self.InformacionTienda=InformacionTienda

