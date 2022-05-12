from usuario import Usuario
class Vendedor(Usuario):
    Telefono:str
    CorreoElectronico:str
    DireccionResidencia:str
    Sexo:bool

    def __init__(self, Nombre, DocumentoUsuario, Contraseña, Telefono, CorreoElectronico,DireccionResidencia,Sexo):
        super().__init__(Nombre, DocumentoUsuario, Contraseña)
        self.Telefono=Telefono
        self.CorreoElectronico=CorreoElectronico
        self.DireccionResidencia=DireccionResidencia
        self.Sexo=Sexo




