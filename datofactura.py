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
    
    def __init__(self,fecha,NombreTienda,Telefono,NumeroFactura,MetodoPago,Cliente,Vendedor,Producto,Venta,InformacionTienda):
        self.Cliente=Cliente
        self.Vendedor=Vendedor
        self.Producto=Producto
        self.Venta=Venta 
        self.InformacionTienda=InformacionTienda
        self.Fecha=fecha
        self.NombreTienda=NombreTienda
        self.Telefono=Telefono
        self.NumeroDeFactura=NumeroFactura
        self.MetodoPago=MetodoPago
    GenerarFactura()    

