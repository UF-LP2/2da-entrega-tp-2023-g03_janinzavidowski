from enfermero import cEnfermero
from paciente import cPaciente
class cMedico:
    def __init__(self, DNI: str, Nombre: str, Apellido: str, Ocupado: bool = False):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Ocupado = Ocupado

    def asignarMedico(self,listamedicos: list['cMedico']): #hacer testing
        for i in range(len(listamedicos) - 1):
            if(listamedicos[i].Ocupado==False):
                self.listamedicos[i].Ocupado == True
                return listamedicos[i]
            else:
                return None

    def atenderpaciente(self,pac:cPaciente):
        #incrementar tiempo
        self.Ocupado==False
        return 0