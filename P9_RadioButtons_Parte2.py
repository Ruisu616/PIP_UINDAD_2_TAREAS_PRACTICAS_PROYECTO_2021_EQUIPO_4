import sys

from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P9_RadioButtons_Parte2.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.rb_hombre.setChecked(True)
        #self.rb_soltero.setChecked(True)
        #self.rb_isc.setChecked(True)

        self.rb_hombre.toggled.connect(self.cambioHombre)
        self.rb_mujer.toggled.connect(self.cambioMujer)
        self.rb_otro.toggled.connect(self.cambioOtro)

        self.rb_soltero.toggled.connect(self.cambioSoltero)
        self.rb_casado.toggled.connect(self.cambioCasado)
        self.rb_divorciado.toggled.connect(self.cambioDivorciado)
        self.rb_unionLibre.toggled.connect(self.cambioUnionLibre)

        self.rb_isc.toggled.connect(self.cambioISC)
        self.rb_ic.toggled.connect(self.cambioIC)
        self.rb_ii.toggled.connect(self.cambioII)
        self.rb_in.toggled.connect(self.cambioIN)
        self.rb_ig.toggled.connect(self.cambioIG)

        self.sexo = "NO DEFINIDO"
        self.estado_civil = "NO DEFINIDO"
        self.licenciatura = "NO DEFINIDO"

        self.btn_enviar.clicked.connect(self.enviar_formulario)

    #area de slots
    def enviar_formulario(self):
        print("Sexo: " + self.sexo)
        print("Estado Civil: " + self.estado_civil)
        print("Licenciatura: " + self.licenciatura)

    def cambioHombre(self):
        self.sexo = "HOMBRE"

    def cambioMujer(self):
        self.sexo = "MUJER"

    def cambioOtro(self):
        self.sexo = "OTRO"

    def cambioSoltero(self):
        self.estado_civil = "SOLLTERO"

    def cambioCasado(self):
        self.estado_civil = "CASADO"

    def cambioDivorciado(self):
        self.estado_civil = "DIVORCIADO"

    def cambioUnionLibre(self):
        self.estado_civil = "Unión Libre"

    def cambioISC(self):
        self.licenciatura = "ISC"

    def cambioIC(self):
        self.licenciatura = "IC"

    def cambioII(self):
        self.licenciatura = "II"

    def cambioIN(self):
        self.licenciatura = "IN"

    def cambioIG(self):
        self.licenciatura = "IG"

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

        #ejercicio: añadir la funcionalidad del programa 9 al resto de las categorias

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


