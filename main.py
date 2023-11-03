from src.enfermero import cEnfermero
from src.paciente import cPaciente
from src.archivo import cargar_pacientes_desde_csv

def main() -> None:
  enfermero = cEnfermero()
  lista_pacientes_archivo = cargar_pacientes_desde_csv("pacientes.csv")
  # Seleccionar un paciente al azar
  paciente_azar = enfermero.seleccionar_paciente_azar(lista_pacientes_archivo)

  # Llamar a la función OrdenarGreedy con el paciente seleccionado
  enfermero.ordenar_mergesort(enfermero.listapacientes) # PREGUNTAR A SOL
if __name__ == '__main__':
  cEnfermero

