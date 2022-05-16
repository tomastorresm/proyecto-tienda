from datetime import date
class InformacionTienda:
    NombreTienda:str
    DireccionTienda:str
    FechaFundacion:date
    Fundador:str
    
    def __init__(self,NombreTienda,DireccionTienda,FechaFundacion,Fundador):
        self.NombreTienda=NombreTienda
        self.DireccionTienda=DireccionTienda
        self.FechaFundacion=FechaFundacion
        self.Fundador=Fundador
