from producto import Producto

class pantalon(Producto):
    TipoTela:str
    Rotos:bool
    

    def __init__(self, Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto,TipoTela,Rotos):
        super().__init__(Referencia, NombreProducto, ValorProducto, Talla, Genero, CantidadProducto)
        self.TipoTela=TipoTela
        self.Rotos=Rotos
     def pantalon():
        outfile = open('Productos.txt','a')
        TipoTela= input("Indique el tipo de tela del pantalon, jean o sudadera: ")
        Rotos= input("Indique si o no, si el pantalon tiene rotos: ")
        outfile.write("tipo de proucto: pantalon"+"\n")
        outfile.write("Cuello: " + TipoTela+ "\n")
        outfile.write("cremallera: " + Rotos+"\n" )  
        outfile.write("___________________________________________________________"+"\n")

    pantalon()
