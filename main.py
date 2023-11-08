from library.archivos import cargar_pacientes_desde_csv
from library.enfermero import cEnfermero
from library.archivos import leerenfermeros
from library.archivos import leermedicos
import multiprocessing
import tkinter as tk
def main() -> None:

  global tiempo
  tiempo = 0

  lista_enfermeros = leerenfermeros("enfermerosrandom")
  lista_pacientes_archivo = cargar_pacientes_desde_csv("pacientes.csv")
  lista_medicos = leermedicos("medicosrandom")
  listapacientes = []

  for tiempo in range (1200):
    if(tiempo>=0 and tiempo<400): #cada 8 horas cambian los turnos
      sublista_medicos = lista_medicos[:6]
    if(tiempo>=400 and tiempo<800):
      sublista_medicos = lista_medicos[6:12]
    else:
      sublista_medicos = lista_medicos[12:]

    if(tiempo>=1150 or tiempo<300):
      enfermero = lista_enfermeros[0]
      paciente1 = enfermero.seleccionar_paciente_azar(lista_pacientes_archivo)
      enfermero.AsignarColor(paciente1)
      tiempo = tiempo+3
      enfermero.agregarpaciente(paciente1, listapacientes)
      enfermero.actualizar_tiempo(listapacientes, tiempo)
      enfermero.ordenar_mergesort(listapacientes)
      medicoaux = enfermero.asignarMedico(sublista_medicos)
      if medicoaux is not None:
        paciente1=enfermero.enviarpaciente(listapacientes)
        medicoaux.atenderpaciente(paciente1)

      tiempo = tiempo+4

    if (tiempo >= 300 and tiempo < 500): #en este horario tengo dos enfermeros
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

        enfermero1.actualizar_tiempo(listapacientes,tiempo)

        enfermero1.ordenar_mergesort(listapacientes)

        medicoaux1 = enfermero1.asignarMedico(sublista_medicos)
        if medicoaux1 is not None:
          pacienteaux1= enfermero1.enviarpaciente(listapacientes)
          medicoaux1.atenderpaciente(pacienteaux1)

        medicoaux2= enfermero2.asignarMedico(sublista_medicos)
        if medicoaux2 is not None:
          pacienteaux2= enfermero2.enviarpaciente(listapacientes)
          medicoaux2.atenderpaciente(pacienteaux2)

        tiempo = tiempo + 4

    if (tiempo >= 500 and tiempo < 800): #en este horario tengo cinco enfermeros
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

        medicoaux1 = enfermero1.asignarMedico(sublista_medicos)
        if medicoaux1 is not None:
          pacienteaux1= enfermero1.enviarpaciente(listapacientes)
          medicoaux1.atenderpaciente(pacienteaux1)
        medicoaux2 = enfermero2.asignarMedico(sublista_medicos)
        if medicoaux2 is not None:
          pacienteaux2= enfermero2.enviarpaciente(listapacientes)
          medicoaux2.atenderpaciente(pacienteaux2)
        medicoaux3 = enfermero3.asignarMedico(sublista_medicos)
        if medicoaux3 is not None:
          pacienteaux3= enfermero3.enviarpaciente(listapacientes)
          medicoaux3.atenderpaciente(pacienteaux3)
        medicoaux4 = enfermero4.asignarMedico(sublista_medicos)
        if medicoaux4 is not None:
          pacienteaux4= enfermero4.enviarpaciente(listapacientes)
          medicoaux4.atenderpaciente(pacienteaux4)
        medicoaux5 = enfermero5.asignarMedico(sublista_medicos)
        if medicoaux5 is not None:
          pacienteaux5= enfermero5.enviarpaciente(listapacientes)
          medicoaux5.atenderpaciente(pacienteaux5)

        tiempo = tiempo + 4

    if (tiempo >= 800 and tiempo < 1150): #en este horario tengo tres enfermeros
      enfermero1 = lista_enfermeros[8]
      enfermero2 = lista_enfermeros[9]
      enfermero3 = lista_enfermeros[10]


      paciente1= enfermero1.seleccionar_paciente_azar(lista_pacientes_archivo)
      paciente2 = enfermero2.seleccionar_paciente_azar(lista_pacientes_archivo)
      paciente3 = enfermero3.seleccionar_paciente_azar(lista_pacientes_archivo)


      proceso1= multiprocessing.Process(target=enfermero1.AsignarColor, args=(paciente1,))
      proceso2= multiprocessing.Process(target=enfermero2.AsignarColor, args=(paciente2,))
      proceso3 = multiprocessing.Process(target=enfermero3.AsignarColor, args=(paciente3,))

      try:
          proceso1.start()
          proceso2.start()
          proceso3.start()

          proceso1.join()
          proceso2.join()
          proceso3.join()
      except Exception:

        tiempo = tiempo+3
        enfermero1.agregarpaciente(paciente1,listapacientes)
        enfermero2.agregarpaciente(paciente2, listapacientes)
        enfermero3.agregarpaciente(paciente3,listapacientes)

        enfermero1.actualizar_tiempo(listapacientes,tiempo)

        enfermero1.ordenar_mergesort(listapacientes)

        medicoaux1 = enfermero1.asignarMedico(sublista_medicos)
        if medicoaux1 is not None:
          pacienteaux1 = enfermero1.enviarpaciente(listapacientes)
          medicoaux1.atenderpaciente(pacienteaux1)

        medicoaux2 = enfermero2.asignarMedico(sublista_medicos)
        if medicoaux2 is not None:
          pacienteaux2 = enfermero2.enviarpaciente(listapacientes)
          medicoaux2.atenderpaciente(pacienteaux2)

        medicoaux3 = enfermero3.asignarMedico(sublista_medicos)
        if medicoaux3 is not None:
          pacienteaux3 = enfermero3.enviarpaciente(listapacientes)
          medicoaux3.atenderpaciente(pacienteaux3)

      tiempo = tiempo + 4

  class InterfazPacientes(tk.Tk):
    def __init__(self, listapacientes):
      super().__init__()

      self.listapacientes = listapacientes
      self.indice_paciente_actual = 0

      self.title("Interfaz de Pacientes")

      self.label_nombre = tk.Label(self, text="Nombre:")
      self.label_sintoma = tk.Label(self, text="Síntoma:")
      self.label_color = tk.Label(self, text="Color:")
      self.label_tiempo_max = tk.Label(self, text="Tiempo Máximo:")

      self.label_nombre.pack()
      self.label_sintoma.pack()
      self.label_color.pack()
      self.label_tiempo_max.pack()

      self.button_siguiente = tk.Button(self, text="Siguiente", command=self.mostrar_siguiente_paciente)
      self.button_siguiente.pack()

      self.mostrar_paciente_actual()

    def mostrar_paciente_actual(self):
      if self.indice_paciente_actual < len(self.listapacientes):
        paciente_actual = self.listapacientes[self.indice_paciente_actual]

        self.label_nombre.config(text=f"Nombre: {paciente_actual.Nombre} {paciente_actual.Apellido}")
        self.label_sintoma.config(text=f"Síntoma: {paciente_actual.Sintoma}")
        self.label_color.config(text=f"Color: {paciente_actual.Color}")
        self.label_tiempo_max.config(text=f"Tiempo Máximo: {paciente_actual.Tiempo_max}")
      else:
        self.label_nombre.config(text="No hay más pacientes")

    def mostrar_siguiente_paciente(self):
      self.indice_paciente_actual += 1
      self.mostrar_paciente_actual()

  app = InterfazPacientes(listapacientes)
  app.mainloop()

  if __name__ == '__main__':
