from enfermero import cEnfermero, cPaciente, cMedico


def test_rojo():
    paciente = cPaciente(4322, "Juan", "Lopez", "Politraumatismo grave", "Rojo", 0, 50, )
    enf = cEnfermero(3299, "Camila", "Garcia", 16)

    enf.AsignarColor(paciente)
    assert paciente.Color == "Rojo"
    assert paciente.Puntos == 50


def test_naranja():
    paciente = cPaciente(2321, "Emilia", "Janin", "Coma", "Naranja", 10, 30)
    enf = cEnfermero(2273, "Lourdes", "Perez", 16)

    enf.AsignarColor(paciente)
    assert paciente.Color == "Naranja"
    assert paciente.Puntos == 30


def test_amarillo():
    paciente = cPaciente(5653, "Pedro", "Traboni", "Paresia", "Amarillo", 60, 20)
    enf = cEnfermero(1123, "Jose", "Garcia", 21)

    enf.AsignarColor(paciente)
    assert paciente.Color == "Amarillo"
    assert paciente.Puntos == 20


def test_verde():
    paciente = cPaciente(4322, "Juan", "Lopez", "Dolores inespecificos leves", "Verde", 120, 10)
    enf = cEnfermero(9554, "Daniela", "Vazques", 19)

    enf.AsignarColor(paciente)
    assert paciente.Color == "Verde"
    assert paciente.Puntos == 10


def test_azul():
    paciente = cPaciente(3123, "Maria", "Caseres", "No urgente", "Azul", 240, 0)
    enf = cEnfermero(3454, "Mariano", "Asurmendi", 22)

    enf.AsignarColor(paciente)
    assert paciente.Color == "Azul"
    assert paciente.Puntos == 0


def test_novalido():
    paciente = cPaciente(2322, "Sofía", "González", "Síntoma Inválido", "Azul", 240, 10)
    enf = cEnfermero(2274, "Ana", "López", 8)
    try:
        enf.AsignarColor(paciente)
    except Exception as e:
        assert str(e) == "Síntoma no válido para asignar color."
    else:
        assert False, "Se esperaba una excepción, pero no se generó."


def test_seleccionar_paciente_azar():
    pacientes_muestra = [
        cPaciente(4322, "Juan", "Lopez", "Dolores inespecificos leves", "Verde", 120, 10),
        cPaciente(2321, "Emilia", "Janin", "Coma", "Naranja", 10, 30),
        cPaciente(3123, "Maria", "Caseres", "No urgente", "Azul", 240, 0),
        cPaciente(3993, "Maria", "Juanes", "Coma", "Naranja", 10, 30),
    ]

    # Llamar a la función para seleccionar un paciente al azar
    enfermero = cEnfermero(1, "Enfermero1", "Apellido1", 16)
    paciente_seleccionado = enfermero.seleccionar_paciente_azar(pacientes_muestra)

    # Verificar que el paciente seleccionado esté en la lista de muestra
    assert paciente_seleccionado in pacientes_muestra


def test_buscar_paciente_existente():
    pacientes = [
        cPaciente(4322, "Juan", "Lopez", "Dolores inespecificos leves", "Verde", 120, 10),
        cPaciente(2321, "Emilia", "Janin", "Coma", "Naranja", 10, 30),
        cPaciente(3123, "Maria", "Caseres", "No urgente", "Azul", 240, 0),
        cPaciente(3993, "Maria", "Juanes", "Coma", "Naranja", 10, 30),
    ]
    enfermero = cEnfermero(21, "Lautaro", "Gomez", 23)
    paciente_existente = cPaciente(2321, "Emilia", "Janin", "Coma", "Naranja", 10, 30)
    assert enfermero.buscarpaciente(pacientes, paciente_existente) == True


def test_buscar_paciente_inexistente() -> None:
    pacientes = [
        cPaciente(2211, "Emilia", "Rios", "Coma", "Naranja", 10, 30),
        cPaciente(3123, "Laura", "Caseres", "No urgente", "Azul", 240, 0)
    ]
    enfermero = cEnfermero(31, "Lautaro", "Gomez", 23)
    paciente_nuevo = cPaciente(3, "Maria", "Perez", "No urgente", "Azul", 240, 0)
    assert False == enfermero.buscarpaciente(pacientes, paciente_nuevo)

def test_agregarpaciente():
    enfermero = cEnfermero(51, "Maia", "Gomez", 23)
    lista_pacientes = []
    paciente_nuevo = cPaciente(1, "Paciente1", "Apellido1", "Politraumatismo", "Rojo",0,50 )
    enfermero.agregarpaciente(paciente_nuevo, lista_pacientes)
    assert paciente_nuevo in lista_pacientes


def test_agregarpaciente_existente():  # quiero verificar que no lo agregue dos veces
    enfermero = cEnfermero(221, "Lucila", "Garcia", 23)
    lista_pacientes = []
    paciente_existente = cPaciente(1, "Paciente1", "Apellido1", "Politraumatismo", "Rojo", 0, 50)
    lista_pacientes.append(paciente_existente)

    enfermero.agregarpaciente(paciente_existente, lista_pacientes)
    # La longitud de la lista no debe cambiar
    assert len(lista_pacientes) == 1


def test_ordenar_mergesort():
    paciente1 = cPaciente(7211, "Emilia", "Rios", "Coma", "Naranja", 10, 30)
    paciente2 = cPaciente(2891, "Juana", "Maguire", "Cefalea brusca", "Amarillo", 60, 20)
    paciente3 = cPaciente(2176, "Rocio", "Perez", "Coma", "Naranja", 10, 30)
    lista_pacientes = [paciente1, paciente2, paciente3]  # lista desordenada
    enfermero = cEnfermero(551, "Pedro", "Gomez", 23)

    lista_ordenada = enfermero.ordenar_mergesort(lista_pacientes)

    # Verificar si la lista se ordena
    for i in range(1, len(lista_ordenada)):
        assert lista_ordenada[i - 1].tiempo <= lista_ordenada[i].tiempo


def test_ordenar_tiempoigual():
    paciente1 = cPaciente(324, "Juan", "Perez", "Coma", "Naranja", 10, 30)
    paciente2 = cPaciente(5432, "Maria", "Gomez", "Cefalea brusca", "Amarillo", 60, 20)
    paciente3 = cPaciente(9320, "Pedro", "Rodriguez", "Traumatismos", "Verde", 120, 10)
    lista_pacientes = [paciente1, paciente2, paciente3]  # lista desordenada
    enfermero = cEnfermero(522, "Maia", "Gomez", 23)

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

    enfermero = cEnfermero(92, "Javier", "Gomez", 10)
    # Intenta asignar un médico disponible
    medico_asignado = enfermero.asignarMedico(lista_medicos)

    assert medico_asignado is not None  # Verifica que se asignó un médico
    assert medico_asignado.Ocupado is True  # Verifica que el médico esté marcado como ocupado


def test_todosocupados():
    medico1 = cMedico("12345", "Lucas", "Pérez", True)
    medico2 = cMedico("67890", "Laura", "Fernandez", True)
    medico3 = cMedico("54321", "Carla", "Pala", True)
    lista_medicos = [medico1, medico2, medico3]
    enfermero = cEnfermero(392, "Paula", "Rodriguez", 23)
    # Intenta asignar un médico cuando todos están ocupados
    medico_asignado = enfermero.asignarMedico(lista_medicos)
    assert medico_asignado is None  # Verifica que no se haya asignado ningún médico
