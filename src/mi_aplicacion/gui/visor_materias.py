from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QVBoxLayout
class Aplicacion_Gui(QWidget):

    def __init__(self):
        super().__init__()

        #Se establecen las características de la ventana
        self.title = 'Mi hospital'
        self.left = 80
        self.top = 80
        self.width = 300
        self.height = 320
        self.inicializar_GUI()
        self.logica = logica
        self.actualizar_l()

    def actualizar_materia(self):
        actual = self.logica.dar_paciente_actual()
        self.txt_nombre.setText(actual["Nombre"])
        self.txt_apellido.setText(actual["Apellido"])
        self.txt_sintoma.setText(actual["Sintoma"])
        self.txt_tiempo.setText(str(actual["Tiempo"]))

    def avanzar_paciente(self):
        paciente_aleatorio = seleccionar_paciente_azar("PacientesRandom")
        #Agregar el paciente aleatorio a la lista de pacientes
        self.logica.agregarpaciente(paciente_aleatorio, listapacientes)

        # Actualizar la vista
        self.actualizar_paciente()


    def inicializar_GUI(self):
        # inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Creamos el distribuidor gráfico principal
        self.distr_vertical = QVBoxLayout()

        # Creamos la caja de pacientes
        self.caja_pacientes = QGroupBox("Pacientes")
        distr_caja_pacientes = QGridLayout()
        self.caja_pacientes.setLayout(distr_caja_pacientes)

        # Creamos las etiquetas y campos de texto
        self.etiqueta_nombre = QLabel('Nombre')
        self.txt_nombre = QLineEdit()

        self.etiqueta_apellido = QLabel('Apellido')
        self.txt_apellido = QLineEdit()

        self.etiqueta_sintoma = QLabel('Sintoma')
        self.txt_sintoma = QLineEdit()

        self.etiqueta_tiempo = QLabel('Tiempo')
        self.txt_tiempo = QLineEdit()

        # Agregamos a la caja de materias las etiquetas
        distr_caja_pacientes.addWidget(self.etiqueta_nombre, 0, 0)
        distr_caja_pacientes.addWidget(self.etiqueta_apellido, 1, 0)
        distr_caja_pacientes.addWidget(self.etiqueta_sintoma, 2, 0)
        distr_caja_pacientes.addWidget(self.etiqueta_tiempo, 3, 0)

        # Agregamos a la caja de materias los campos de texto
        distr_caja_pacientes.addWidget(self.txt_nombre, 0, 1)
        distr_caja_pacientes.addWidget(self.txt_apellido, 1, 1)
        distr_caja_pacientes.addWidget(self.txt_sintoma, 2, 1)
        distr_caja_pacientes.addWidget(self.txt_tiempo, 3, 1)

        # Creamos la caja de botones
        self.caja_botones = QGroupBox()
        distr_caja_botones = QHBoxLayout()
        self.caja_botones.setFixedHeight(50)
        self.caja_botones.setLayout(distr_caja_botones)

        # Creamos los botones para la caja de botones
        self.boton_retroceder = QPushButton("<<")
        self.boton_retroceder.clicked.connect(self.retroceder_paciente)
        self.boton_avanzar = QPushButton(">>")
        self.boton_avanzar.clicked.connect(self.avanzar_paciente)

        # Agregamos los botones a la caja de botones
        distr_caja_botones.addWidget(self.boton_retroceder)
        distr_caja_botones.addWidget(self.boton_avanzar)

        # Agregamos las cajas a nuestra aplicación
        self.distr_vertical.addWidget(self.caja_pacientes)
        self.distr_vertical.addWidget(self.caja_botones)

        # Definimos el distribuidor principal de la ventana
        self.setLayout(self.distr_vertical)

        # Hacemos la ventana visible
        self.show()

