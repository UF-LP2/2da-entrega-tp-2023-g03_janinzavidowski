import csv
import random
from medico import cMedico, cPaciente

class cEnfermero:

    listamedicos = []
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
            elif pac.Sintoma == "Coma" or pac.Sintoma == "Convulsion" or pac.Sintoma == "Hemorragia digestiva" or pac.Sintoma == "Isquemia":
                pac.Color = "Naranja"
                pac.Puntos = 30
                pac.Tiempo_max = 10
            elif pac.Sintoma == "Cefalea brusca" or pac.Sintoma == "Paresia" or pac.Sintoma == "Hipertension arterial" or pac.Sintoma == "Vertigo con afectacion vegetativa" or pac.Sintoma == "Sincope" or pac.Sintoma == "Urgencia psiquiatrica" :
                pac.Color = "Amarillo"
                pac.Puntos = 20
                pac.Tiempo_max = 60
            elif pac.Sintoma == "Otalgia" or pac.Sintoma == "Odontalgia" or pac.Sintoma == "Dolores inespecificos leves" or pac.Sintoma == "Traumatismos" or pac.Sintoma == "Esguince":
                pac.Color = "Verde"
                pac.Puntos = 10
                pac.Tiempo_max = 120
            elif pac.Sintoma=="No urgente":
                pac.Color = "Azul"
                pac.Puntos = 0
                pac.Tiempo_max = 240
            else :
                raise ValueError("Síntoma no válido para asignar color.")


    def seleccionar_paciente_azar(self,lista_pacientes_archivo):  # Función para seleccionar un paciente al azar
        return random.choice(lista_pacientes_archivo)

    def buscarpaciente(self,listapacientes: list[cPaciente], pac:cPaciente)->bool: #chequeamos que el paciente que vamos a agregar no se encuentre en la lista
        for i in range(len(listapacientes) ):

            if pac.ID == listapacientes[i].ID:
                return True
        return False
    def agregarpaciente(self, pac:cPaciente, listapacientes):
        if (self.buscarpaciente(listapacientes, pac)==False):#chequeo que no este en la lista
            listapacientes.append(pac)


    def ordenar_mergesort(self,listapacientes):
        if len(listapacientes) <= 1:  # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
            return listapacientes

        medio = len(listapacientes) // 2
        lista_izq = listapacientes[:medio]
        lista_der = listapacientes[medio:]

        lista_izq = self.ordenar_mergesort(lista_izq)  # Llamada recursiva para ordenar la mitad izquierda
        lista_der = self.ordenar_mergesort(lista_der)  # Llamada recursiva para ordenar la mitad derecha

        i = j = k = 0

        while i < len(lista_izq) and j < len(lista_der) :
            if lista_izq[i].Tiempo_max < lista_der[j].Tiempo_max or (lista_izq[i].Tiempo_max == lista_der[j].Tiempo_max and lista_izq[i].Puntos < lista_der[j].Puntos):
                listapacientes[k] = lista_izq[i]
                i += 1
            else:
                listapacientes[k] = lista_der[j]
                j += 1
            k += 1

        while i < len(lista_izq):
            listapacientes[k] = lista_izq[i]
            i += 1
            k += 1

        while j < len(lista_der):
            listapacientes[k] = lista_der[j]
            j += 1
            k += 1

        return listapacientes

    def enviarpaciente(self, listapacientes):
        auxiliar=listapacientes[0]
        del listapacientes[0]
        return

    def asignarMedico(self,sublista_medicos):
        for i in range(len(sublista_medicos)):
            if(sublista_medicos[i].Ocupado==False):
                sublista_medicos[i].Ocupado = True
                return sublista_medicos[i]
        return None

    def actualizartiempo(self, listapacientes, tiempo):
        for i in range(len(listapacientes)):
            listapacientes[i].Tiempo_max = listapacientes[i].Tiempo_max - tiempo
            return listapacientes


