from datetime import datetime
class cPaciente:
    def __init__ (self, DNI: str, Nombre:str, Apellido:str, Sintoma: str, Hllegada: int, Hactual: int, Color: str, Tiempo_max:int, Puntos: int):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Sintoma = Sintoma
        self.Hllegada = Hllegada
        self.Hactual = Hactual
        self.Color = Color
        self.Tiempo_max = Tiempo_max
        self.Puntos = Puntos
