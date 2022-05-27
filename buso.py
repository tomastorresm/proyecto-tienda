from producto import Producto


class buso(Producto):
    Capota:bool
    Cremallera:bool
    Bolsillo:bool

    def __init__(self, Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto,Capota,Cremallera,Bolsillo):
        super().__init__(Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto)
        self.Capota=Capota
        self.Cremallera=Cremallera
        self.Bolsillo=Bolsillo
        
    # al iniciarlo nos pide los datos del main creado en la clase padre y ademas de los datos pedidos en esta clase y guarda la informacion 
#completa em el archivo de texto
    def busoo():
        outfile = open('Productos.txt','a')
        capota= input("Indique si o no, si el buso tien capota: ")
        cremallera= input("Indique si o no, si el buso tien cremallera: ")
        bolsillo=input("Indique si o no, si el buso tien bolsillo: ")
        outfile.write("tipo de producto: buso"+"\n")
        outfile.write("capota: " + capota+ "\n")
        outfile.write("cremallera: " + cremallera+"\n" )
        outfile.write("bolsillo: "+bolsillo+"\n" )  
        outfile.write("___________________________________________________________"+"\n")
                  
    busoo()    

    
