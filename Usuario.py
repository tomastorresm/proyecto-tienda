class Usuario:
    Nombre:str
    DocumentoUsuario:int
    Contrasena:str
    
    def __init__(self,Nombre,DocumentoUsuario,Contrasena,contrasea2):
        self.Nombre=Nombre
        self.DocumentoUsuario=DocumentoUsuario
        self.Contrasena=Contrasena
    
    def main():
        outfile=open("Usuario.txt","a")
        Nombre=input("Ingrese su nombre: ")
        DocumentoUsuario=input("Ingrese su documento: ")
        Contrasena=input("Ingrese la contraseña: ")
        outfile.write("Nombre: "+Nombre+"\n")
        outfile.write("Documento: "+DocumentoUsuario+"\n")
        outfile.write("Contrasena: "+Contrasena+"\n")
    main()

