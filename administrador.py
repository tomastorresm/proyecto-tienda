from usuario import Usuario

class Administrador(Usuario):
    IdAdministrador:int
    def __init__(self, Nombre, DocumentoUsuario, Contraseña,IdAdministrador):
        super().__init__(Nombre, DocumentoUsuario, Contraseña)
        self.IdAdministrador=IdAdministrador
    
    def Administrador():
        outfile =open("Usuario.txt","a")
        IdAdministrador=input("Ingrese su id de administrador: ")
        outfile.write("IdAdministrador: "+IdAdministrador*"\n")
        outfile.write("Tipo de usuario: Administrador: ")
        outfile.write("________________________________________")
    Administrador()    
        
   





    
