class Hospital():

    def __init__(self):
        self.lista_pacientes = []  # Inicializa la lista de pacientes
        self.actual = 0

    def dar_paciente_actual(self):
        return self.lista_pacientes[self.actual]

    def agregar_paciente(self):
        # Agrega un nuevo paciente a la lista (debes definir cómo obtener los datos)
        nuevo_paciente = {"Nombre": "Nuevo Paciente", "Sintoma": "Nuevo Sintoma", "Tiempo": 0}
        self.lista_pacientes.append(nuevo_paciente)
        self.actual = len(self.lista_pacientes) - 1

