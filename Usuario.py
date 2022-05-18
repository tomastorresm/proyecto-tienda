class Usuario:
    Nombre:str
    DocumentoUsuario:int
    Contrasena:str
    
    def __init__(self,Nombre,DocumentoUsuario,Contrasena,contrasea2):
        self.Nombre=Nombre
        self.DocumentoUsuario=DocumentoUsuario
        self.Contrasena=Contrasena
        

    def printdatos(self):
        print(self.Nombre,self.DocumentoUsuario)    
x=Usuario("tomas","1002544519","123",)
x.printdatos()

