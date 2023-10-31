from library.Enfermero import cEnfermero
from library.Paciente import cPaciente
from library.archivo import cargar_pacientes_desde_csv

def main() -> None:
  lista_pacientes_archivo = cargar_pacientes_desde_csv("pacientes.csv")
  # Seleccionar un paciente al azar
  paciente_azar = seleccionar_paciente_azar(lista_pacientes_archivo)

  # Llamar a la función OrdenarGreedy con el paciente seleccionado
  enfermero.OrdenarGreedy(listapacientes, paciente_azar)
if __name__ == '__main__':
