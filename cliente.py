class Cliente:
    Documento:int
    Celular:int
    Correo:str
    def __init__(self,Documento,Celular,Correo):
        self.Documento=Documento
        self.Celular=Celular
        self.Correo=Correo
        
    def cliente():
        outfile = open('Clientes.txt','a')
        Nombre=input("Ingrese su nombre: ")
        Documento= input("Ingrese su documento: ")
        Celular= input("Ingrese su numero de celular: ")
        Correo= input("Ingrese su correo electronico: ")
        outfile.write("Nombre: "+Nombre+"\n")
        outfile.write("Correo electronico"+Correo+"\n")
        outfile.write("Documento: " + Documento+ "\n")
        outfile.write("celular: " + Celular+"\n" )  
        outfile.write("___________________________________________________________"+"\n")

    cliente()    
