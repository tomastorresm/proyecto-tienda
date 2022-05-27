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
    
    def vendedor():
        outfile =open("Usuario.txt","a")
        Telefono=input("Ingrese su id de administrador")
        CorreoElectronico=input("Ingrese su correo electronico: ")
        DireccionResidencia=input("Ingrese su direccion de residencia: ")
        Sexo=input("Ingrese su sexo: ")
        outfile.write("Telefono: "+Telefono+"\n")
        outfile.write("Tipo de usuario: Vendedor")
        outfile.write("Correo electronico : "+CorreoElectronico+"\n")
        outfile.write("Direccion de residencia : "+DireccionResidencia+"\n")
        outfile.write("Sexo: "+Sexo+"\n")
        outfile.write("________________________________________")
    vendedor() 




