from Paciente import cPaciente
import csv
import random

class cEnfermero:
    listapacientes = []
    def __init__(self, ID: int, Nombre: str, Apellido: str, Turno_laboral: int):
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

    def seleccionar_paciente_azar(self,lista_pacientes_archivo):  # Función para seleccionar un paciente al azar
        return random.choice(lista_pacientes_archivo)

    def buscarpaciente(self,listapacientes: list[cPaciente], pac:cPaciente)->bool: #chequeamos que el paciente que vamos a agregar no se encuentre en la lista
        for i in range(len(listapacientes) - 1):

            if pac.ID() == listapacientes[i].ID():
                return True
            return False

    def OrdenarGreedy(self, listapacientes: list[cPaciente], pac:cPaciente)->int:
        if self.buscarpaciente(listapacientes, pac) == True: #paciente ya esta en la lista, no lo vuelvo a agregar
            return -1
        else:
            for i in range(len(listapacientes)-1):

                if pac.tiempo() < listapacientes[i].tiempo():
                    listapacientes.insert(i,pac)

            if pac.tiempo()<1:
                listapacientes.insert(0,pac)

            else:
                listapacientes.append(pac)

        return 0