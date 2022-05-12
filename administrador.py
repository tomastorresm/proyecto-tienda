from usuario import Usuario

class Administrador(Usuario):
    IdAdministrador:int
    def __init__(self, Nombre, DocumentoUsuario, Contraseña,IdAdministrador):
        super().__init__(Nombre, DocumentoUsuario, Contraseña)
        self.IdAdministrador=IdAdministrador
    
        
   





    
