from datetime import datetime
class cPaciente:
    def __init__ (self, ID: str, Nombre:str, Apellido:str, Sintoma: str, Hllegada: float, Hactual: float, Color: str, Tiempo_max:int, Puntos: int):
        self.ID = ID
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Sintoma = Sintoma
        self.Hllegada = Hllegada
        self.Hactual = Hactual
        self.Color = Color
        self.Tiempo_max = Tiempo_max
        self.Puntos = Puntos

    def tiempo(self):
        return self.Hllegada - self.Hactual
