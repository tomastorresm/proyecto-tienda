from producto import Producto

class camiseta(Producto):
    TipoCuello:str
    Estampada:bool
    Botones:bool

    def __init__(self, Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto,TipoCuello,Estampada,Botones):
        super().__init__(Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto)
        self.TipoCuello=TipoCuello
        self.Estampada=Estampada
        self.Botones=Botones
    # al iniciarlo nos pide los datos del main creado en la clase padre y ademas de los datos pedidos en esta clase y guarda la informacion 
#completa em el archivo de texto
    def camiseta():
        outfile = open('Productos.txt','a')
        TipoCuello= input("Indique el tipo de cuello de la camiseta, redondo o v : ")
        Estampada= input("Indique si o no, si la camiseta es estampada: ")
        Botones =input("Indique si o no, si la camseta tiene botones: ")
        outfile.write("tipo de proucto: camiseta")
        outfile.write("Cuello: " + TipoCuello+ "\n")
        outfile.write("cremallera: " + Estampada+"\n" )
        outfile.write("botones: "+Botones+"\n" )    
        outfile.write("___________________________________________________________"+"\n")

    camiseta()        

