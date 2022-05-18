class Usuario:
    Nombre:str
    DocumentoUsuario:int
    Contrasena:str
    contrasea2:str
    def __init__(self,Nombre,DocumentoUsuario,Contrasena,contrasea2):
        self.Nombre=Nombre
        self.DocumentoUsuario=DocumentoUsuario
        self.Contrasena=Contrasena
        self.contrasea2=contrasea2

    def printdatos(self):
        print(self.Nombre,self.DocumentoUsuario,self.Contrasena)    
x=Usuario("tomas","1002544519","123","1234")
x.printdatos()

