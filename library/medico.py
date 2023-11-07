from src.paciente import cPaciente
class cMedico:

    def __init__(self, DNI: str, Nombre: str, Apellido: str, Ocupado: bool = False):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Ocupado = Ocupado

    def atenderpaciente(self,pac:cPaciente):
        #incrementar tiempo
        self.Ocupado==False
        return 0