from paciente import cPaciente
import csv
def cargar_pacientes_desde_csv(PacientesRandom):
    lista_pacientes_archivo = []
    with open(PacientesRandom, 'r') as archivo:
        lector_csv = csv.DictReader(archivo)
        next(lector_csv)  # Saltar la primera fila (encabezado)
        for fila in lector_csv:
            id = fila['id']
            first_name = fila['first_name']
            last_name = fila['last_name']
            sintomas = fila['sintomas']
            horario_entrada = fila['horario_entrada']
            paciente = cPaciente(id, first_name, last_name, sintomas, horario_entrada)
            lista_pacientes_archivo.append(paciente)
    return lista_pacientes_archivo
