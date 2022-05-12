class Usuario:
    Nombre:str
    DocumentoUsuario:int
    Contraseña:str
    def __init__(self,Nombre,DocumentoUsuario,Contraseña):
        self.Nombre=Nombre
        self.DocumentoUsuario=DocumentoUsuario
        self.Contraseña=Contraseña

    def printdatos(self):
        print(self.Nombre,self.DocumentoUsuario,self.Contraseña)    
x=Usuario("tomas","1002544519","123")
x.printdatos()

