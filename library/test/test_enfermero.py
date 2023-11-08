from enfermero import cEnfermero, cPaciente, cMedico

""" def test_rojo():
    paciente = cPaciente(4322, "Juan", "Lopez", "Politraumatismo grave", 20.30, 21.40, "Rojo", 0, 50)
    enf = cEnfermero(3299, "Camila", "Garcia", 16)

    enf.AsignarColor(paciente)
    assert paciente.color == "Rojo"
    assert paciente.puntos == 50
def test_naranja():

    paciente = cPaciente(2321, "Emilia", "Janin", "Coma", 21.30, 21.40, "Naranja", 10, 30)
    enf = cEnfermero(2273, "Lourdes", "Perez", 16)

    enf.AsignarColor(paciente)
    assert paciente.color == "Naranja"
    assert paciente.puntos == 30

def test_amarillo():
    paciente = cPaciente(5653, "Pedro", "Traboni", "Paresia", 00.30, 00.40, "Amarillo", 60, 20)
    enf = cEnfermero(1123, "Jose", "Garcia", 21)

    enf.AsignarColor(paciente)
    assert paciente.color == "Amarillo"
    assert paciente.puntos == 20

def test_rojo():
    paciente = cPaciente(4322, "Juan", "Lopez", "Dolores inespecificos leves", 12.30, 12.40, "Rojo", 120, 10)
    enf = cEnfermero(9554, "Daniela", "Vazques", 19)

    enf.AsignarColor(paciente)
    assert paciente.color == "Verde"
    assert paciente.puntos == 10

def test_rojo():
    paciente = cPaciente(3123, "Maria", "Caseres", "No urgente", 12.30, 12.40, "Azul", 240, 0)
    enf = cEnfermero(3454, "Mariano", "Asurmendi", 22)

    enf.AsignarColor(paciente)
    assert paciente.color == "Azul"
    assert paciente.puntos == 0

def test_novalido():
    paciente = cPaciente(2322, "Sofía", "González", "Síntoma Inválido", 22.30, 22.40, "Azul", 0, 240)
    enf = cEnfermero(2274, "Ana", "López", 8)
    try:
        enf.AsignarColor(paciente)
    except Exception as e:
        assert str(e) == "Síntoma no válido para asignar color."
    else:
        assert False, "Se esperaba una excepción, pero no se generó."

def test_seleccionar_paciente_azar():
    pacientes_muestra = [
        cPaciente(1, "Pac1", "Sintoma1"),
        cPaciente(2, "Pac2", "Sintoma2"),
        cPaciente(3, "Pac3", "Sintoma3"),
        cPaciente(4, "Pac4", "Sintoma4"),
    ]

    # Llamar a la función para seleccionar un paciente al azar
    enfermero = cEnfermero(1, "Enfermero1", "Apellido1", 1)
    paciente_seleccionado = enfermero.seleccionar_paciente_azar(pacientes_muestra)

    # Verificar que el paciente seleccionado esté en la lista de muestra
    assert paciente_seleccionado in pacientes_muestra

def test_buscar_paciente_existente():
    pacientes = [
        cPaciente(1, "Juan"),
        cPaciente(2, "Laura"),
        cPaciente(3, "Lucas")
    ]
    enfermero = cEnfermero()
    paciente_existente = cPaciente(2, "Laura")
    assert enfermero.buscarpaciente(pacientes, paciente_existente) == True

def test_buscar_paciente_inexistente():
    pacientes = [
        cPaciente(1, "Juan"),
        cPaciente(2, "Laura")
    ]
    enfermero = cEnfermero()
    paciente_nuevo = cPaciente(3, "Maria")
    assert enfermero.buscarpaciente(pacientes, paciente_nuevo) == False

def test_agregarpaciente():
    enfermero = cEnfermero()
    lista_pacientes = []
    paciente_nuevo = cPaciente(1, "Paciente1", "Apellido1", "Rojo")
    enfermero.agregarpaciente(paciente_nuevo, lista_pacientes)
    assert paciente_nuevo in lista_pacientes

def test_agregarpaciente_existente(): #quiero verificar que no lo agregue dos veces
    enfermero = cEnfermero()
    lista_pacientes = []
    paciente_existente = cPaciente(1, "Paciente1", "Apellido1", "Rojo")
    lista_pacientes.append(paciente_existente)

    enfermero.agregarpaciente(paciente_existente, lista_pacientes)
    # La longitud de la lista no debe cambiar
    assert len(lista_pacientes) == 1

def test_ordenar_mergesort():
    paciente1 = cPaciente(21,"Juan", 30)
    paciente2 = cPaciente("Maria", 20)
    paciente3 = cPaciente("Pedro", 25)
    lista_pacientes = [paciente1, paciente2, paciente3] #lista desordenada
    enfermero = cEnfermero()

    lista_ordenada = enfermero.ordenar_mergesort(lista_pacientes)

    # Verificar si la lista se ordena
    for i in range(1, len(lista_ordenada)):
        assert lista_ordenada[i - 1].tiempo <= lista_ordenada[i].tiempo

def test_ordenar_tiempoigual():
    paciente1 = cPaciente("Juan","Perez","Coma",13.45, 14.00, "Naranja", 10, 30)
    paciente2 = cPaciente("Maria","Gomez","Cefalea brusca",13.45, 14.00, "Amarillo", 60, 20)
    paciente3 = cPaciente("Pedro","Rodriguez","Traumatismos",13.55, 14.00, "Verde", 120, 10)
    lista_pacientes = [paciente1, paciente2, paciente3]  # lista desordenada
    enfermero = cEnfermero()

    lista_ordenada = enfermero.ordenar_mergesort(lista_pacientes)

    for i in range(1, len(lista_ordenada)):
            if lista_ordenada[i - 1].tiempo == lista_ordenada[i].tiempo:
                # Si el tiempo es el mismo, verifica los puntos
                assert lista_ordenada[i - 1].puntos <= lista_ordenada[i].puntos
            else:
                assert lista_ordenada[i - 1].tiempo <= lista_ordenada[i].tiempo


def test_asignarMedico():
    medico1 = cMedico("12345", "Lucas", "Pérez", False)
    medico2 = cMedico("67890", "Laura", "Fernandez", True)
    medico3 = cMedico("54321", "Carla", "Pala", False)
    lista_medicos = [medico1, medico2, medico3]

    enfermero = cEnfermero()
    # Intenta asignar un médico disponible
    medico_asignado = enfermero.asignarMedico(lista_medicos)

    assert medico_asignado is not None  # Verifica que se asignó un médico
    assert medico_asignado.Ocupado is True  # Verifica que el médico esté marcado como ocupado

def test_todosocupados():
    medico1 = cMedico("12345", "Lucas", "Pérez", True)
    medico2 = cMedico("67890", "Laura", "Fernandez", True)
    medico3 = cMedico("54321", "Carla", "Pala", True)
    lista_medicos = [medico1, medico2, medico3]
    enfermero = cEnfermero()
    # Intenta asignar un médico cuando todos están ocupados
    medico_asignado = enfermero.asignarMedico(lista_medicos)
    assert medico_asignado is None  # Verifica que no se haya asignado ningún médico """