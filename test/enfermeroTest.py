from Enfermero import cEnfermero

def test_AsignarColor():

    paciente1 = cPaciente(2321, "Emilia", "Janin", "Coma", 21.30, 21.40, "Naranja", 10, 30)
    enf1 = cEnfermero(2273, "Camila", "Zavidowski", 16)

    enf1.AsignarColor(paciente1)
    assert paciente1.color == "Naranja"
    assert paciente1.puntos == 30

