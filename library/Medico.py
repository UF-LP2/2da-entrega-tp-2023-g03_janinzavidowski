from Enfermero import cEnfermero
from Paciente import cPaciente
class cMedico:

    def __int__(self, DNI: str, Nombre: str, Apellido: str, ListaPac: list[cPaciente]):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.ListaPac = ListaPac

