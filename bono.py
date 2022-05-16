from cliente import Cliente
from usuario import Usuario
class Bono:
    valor:int
    CantidadDescuento:str
    DocumentoUsuario:Usuario
    Documento:Cliente
    def __init__(self,valor,CantidadDescuentos,DocumentoUsuario,Documento):
        self.valor=valor
        self.CantidadDescuento=CantidadDescuentos
        self.DocumentoUsuario=DocumentoUsuario
        self.Documento=Documento
