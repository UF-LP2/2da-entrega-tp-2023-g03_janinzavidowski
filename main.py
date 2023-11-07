from library.archivos import cargar_pacientes_desde_csv
from library.enfermero import cEnfermero
from library.archivos import leerenfermeros
from library.archivos import leermedicos
import multiprocessing
def main() -> None:

  global tiempo

  lista_enfermeros = leerenfermeros("enfermerosrandom")
  lista_pacientes_archivo = cargar_pacientes_desde_csv("pacientes.csv")
  lista_medicos = leermedicos("medicosrandom")
  listapacientes = []

  for tiempo in range (1200):
    if(tiempo>=0 and tiempo<400):
      sublista_medicos = lista_medicos[:6]
    if(tiempo>=400 and tiempo<800):
      sublista_medicos = lista_medicos[6:12]
    else:
      sublista_medicos = lista_medicos[12:]

    if(tiempo>=1150 or tiempo<300):
      enfermero = lista_enfermeros[0]


    # Seleccionar un paciente al azar
    paciente_azar = enfermero.seleccionar_paciente_azar(lista_pacientes_archivo)
    enfermero.OrdenarGreedy(enfermero.listapacientes, paciente_azar)

    if (tiempo >= 300 and tiempo < 500): #en este horario tengo dos medicos
      enfermero1 = lista_enfermeros[1]
      enfermero2 = lista_enfermeros[2]
      paciente1= enfermero1.seleccionar_paciente_azar(lista_pacientes_archivo)
      paciente2 = enfermero2.seleccionar_paciente_azar(lista_pacientes_archivo)

      proceso1= multiprocessing.Process(target=enfermero1.AsignarColor, args=(paciente1,))
      proceso2= multiprocessing.Process(target=enfermero2.AsignarColor, args=(paciente2,))
      try:
          proceso1.start()
          proceso2.start()

          proceso1.join()
          proceso2.join()
      except Exception:
        tiempo = tiempo + 3
        enfermero1.agregarpaciente(paciente1,listapacientes)
        enfermero2.agregarpaciente(paciente2, listapacientes)

        enfermero1.actualizar_tiempo(listapacientes)

        enfermero1.ordenar_mergesort(listapacientes)

        medicoaux = enfermero1.asignarMedico(sublista_medicos)
        pacienteaux= enfermero1.enviarpaciente(listapacientes)
        medicoaux.atenderpaciente(pacienteaux)
        tiempo = tiempo + 4

    if (tiempo >= 500 and tiempo < 800): #en este horario tengo dos medicos
      enfermero1 = lista_enfermeros[3]
      enfermero2 = lista_enfermeros[4]
      enfermero3 = lista_enfermeros[5]
      enfermero4 = lista_enfermeros[6]
      enfermero5 = lista_enfermeros[7]

      paciente1= enfermero1.seleccionar_paciente_azar(lista_pacientes_archivo)
      paciente2 = enfermero2.seleccionar_paciente_azar(lista_pacientes_archivo)
      paciente3 = enfermero3.seleccionar_paciente_azar(lista_pacientes_archivo)
      paciente4 = enfermero4.seleccionar_paciente_azar(lista_pacientes_archivo)
      paciente5 = enfermero5.seleccionar_paciente_azar(lista_pacientes_archivo)

      proceso1= multiprocessing.Process(target=enfermero1.AsignarColor, args=(paciente1,))
      proceso2= multiprocessing.Process(target=enfermero2.AsignarColor, args=(paciente2,))
      proceso3 = multiprocessing.Process(target=enfermero3.AsignarColor, args=(paciente3,))
      proceso4 = multiprocessing.Process(target=enfermero4.AsignarColor, args=(paciente4,))
      proceso5 = multiprocessing.Process(target=enfermero5.AsignarColor, args=(paciente5,))

      try:
          proceso1.start()
          proceso2.start()
          proceso3.start()
          proceso4.start()
          proceso5.start()


          proceso1.join()
          proceso2.join()
          proceso3.join()
          proceso4.join()
          proceso5.join()
      except Exception:

        tiempo = tiempo+3
        enfermero1.agregarpaciente(paciente1,listapacientes)
        enfermero2.agregarpaciente(paciente2, listapacientes)
        enfermero3.agregarpaciente(paciente3,listapacientes)
        enfermero4.agregarpaciente(paciente4, listapacientes)
        enfermero5.agregarpaciente(paciente5,listapacientes)

        enfermero1.actualizar_tiempo(listapacientes,tiempo)

        enfermero1.ordenar_mergesort(listapacientes)

        medicoaux = enfermero1.asignarMedico(sublista_medicos)
        pacienteaux= enfermero1.enviarpaciente(listapacientes)
        medicoaux.atenderpaciente(pacienteaux)
        tiempo = tiempo + 4



if __name__ == '__main__':


