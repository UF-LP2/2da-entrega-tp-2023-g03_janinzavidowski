from Enfermero import cEnfermero

def test_rojo():
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

def test_except():
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