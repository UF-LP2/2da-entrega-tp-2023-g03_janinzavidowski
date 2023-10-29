from Paciente import cPaciente

class cEnfermero:
    def __int__(self, ID: int, Nombre: str, Apellido: str, Turno_laboral: int):
        self.ID = ID
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Turno_laboral = Turno_laboral

    def AsignarColor (self, pac: cPaciente) -> None:
        if pac.Sintoma == "Politraumatismo grave" :
            pac.Color = "Rojo"
            pac.Puntos = 50
            pac.Tiempo_max = 0
        elif pac.Sintoma == "Coma" or "Convulsion" or "Hemorragia digestiva" or "Isquemia" :
            pac.Color = "Naranja"
            pac.Puntos = 30
            pac.Tiempo_max = 10
        elif pac.Sintoma == "Cefalea brusca" or "Paresia" or "Hipertension arterial" or "Vertigo con afectacion vegetativa" or "Sincope" or "Urgencia psiquiatrica" :
            pac.Color = "Amarillo"
            pac.Puntos = 20
            pac.Tiempo_max = 60
        elif pac.Sintoma == "Otalgia" or "Odontalgia" or "Dolores inespecificos leves" or "Traumatismos" or "Esguince":
            pac.Color = "Verde"
            pac.Puntos = 10
            pac.Tiempo_max = 120
        else:
            pac.Color = "Azul"
            pac.Puntos = 0
            pac.Tiempo_max = 240