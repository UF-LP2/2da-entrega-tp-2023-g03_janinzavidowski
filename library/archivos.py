
from library.medico import cMedico
import csv
def cargar_pacientes_desde_csv(PacientesRandom): #nos dimos cuenta que la hora de llegada no la queremos asi que no la leemos y listo
    try:
        lista_pacientes_archivo = []
        with open(PacientesRandom, 'r') as archivo:
            lector_csv = csv.DictReader(archivo)
            next(lector_csv)  # Saltar la primera fila (encabezado)
            for fila in lector_csv:
                id = fila['id']
                first_name = fila['first_name']
                last_name = fila['last_name']
                sintomas = fila['sintomas']
                paciente = cPaciente(id, first_name, last_name, sintomas )
                lista_pacientes_archivo.append(paciente)
        return lista_pacientes_archivo
    except FileNotFoundError:
        raise Exception("No encontro el archivo")

def leermedicos(medicosrandom):

    try:
        listamedicos = []
        with open(medicosrandom, 'r') as archivo:
            lector_csv = csv.DictReader(archivo)
            next(lector_csv)  # Saltar la primera fila (encabezado)
            for fila in lector_csv:
                id = fila['id']
                first_name = fila['first_name']
                last_name = fila['last_name']
                medico = cMedico(id, first_name, last_name)
                listamedicos.append(medico)
        return listamedicos
    except FileNotFoundError:
        raise Exception("No se encontro el archivo")

def leerenfermeros(enfermerosrandom):
    try:
        listaenfermeros = []
        with open(enfermerosrandom, 'r') as archivo:
            lector_csv = csv.DictReader(archivo)
            next(lector_csv)  # Saltar la primera fila (encabezado)
            for fila in lector_csv:
                id = fila['id']
                first_name = fila['first_name']
                last_name = fila['last_name']
                turno = fila['turno']
                enfermero = cEnfermero(id, first_name, last_name, turno)
                listaenfermeros.append(enfermero)
        return listaenfermeros
    except FileNotFoundError:
        raise Exception("No se encontro el archivo")


