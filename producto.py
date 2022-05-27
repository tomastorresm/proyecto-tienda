class Producto:
    Referencia: int
    NombreProducto:str
    ValorProducto:float
    Talla:float
    Genero:bool
    CantidadProducto:int

    def __init__(self,Referencia,NombreProducto,ValorProducto,Talla,Genero,CantidadProducto):
        self.Referencia=Referencia
        self.NombreProducto=NombreProducto
        self.ValorProducto=ValorProducto
        self.Talla=Talla
        self.Genero=Genero
        self.CantidadProducto=CantidadProducto
    def main():
        Productos = int(input("Ingrese el número de productos a registrar: "))
        

        for i in range(Productos):
            outfile = open('Productos.txt','a')  
            Referencia= input("Ingrese la referencia: ")
            NombreProducto= input("Ingrese el nombre del producto: ")
            ValorProducto=input("ingrese el costo del producto: ")
            outfile.write("Referencia del producto: " + Referencia+ "\n")
            outfile.write("Nombre: " + NombreProducto+"\n" )
            outfile.write("Valor del producto: "+ValorProducto+"\n" )
            
            
    main()    

