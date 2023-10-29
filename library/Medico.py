from Enfermero import cEnfermero
from Paciente import cPaciente
class cMedico:

    def __int__(self, DNI: str, Nombre: str, Apellido: str, ListaPac: list[cPaciente]):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.ListaPac = ListaPac
    def OrdenarGreedy(self, ListaPac: list[cPaciente], pac:cPaciente)->None:

        for i in range(len(ListaPac)-1):
            if pac.tiempo() < ListaPac[i].tiempo():
                ListaPac.insert(i,pac) #esto me desplaza el resto de los pacientes hacia abajo sin sobreescribir ningun paciente?

        if pac.tiempo()<1:
            ListaPac.insert(0,pac)

        else:
            ListaPac.append(pac)