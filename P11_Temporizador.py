import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P11_Temporizador.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)

        self.seg = 0
        self.min = 0
        self.hr = 0

    #area de slots
    def accion(self):
        t = self.btn_accion.text()
        if t == "INICIAR":
            velTempo = int(self.txt_velocidad.text())
            self.btn_accion.setText("PAUSAR")
            self.segundos.setText(str(00))
            self.segundoPlano.start(velTempo)
        else: #PAUSAR
            self.btn_accion.setText("INICIAR")
            self.segundoPlano.stop()
            self.segundos.setText(str(self.seg))


    def temporizador(self):
        self.seg += 1
        self.segundos.setText(str(self.seg))
        self.minutos.setText(str(self.min))
        self.horas.setText(str(self.hr))
        if self.hr == 23 and self.min==59 and self.seg==59:
            self.seg=0
            self.min=0
            self.hr=0
        if self.min==59 and self.seg==59:
            self.seg = 0
            self.min = 0
            self.hr += 1
        if self.seg == 59:
            self.seg = 0
            self.min += 1

    #Práctica :  Simular un Reloj con Horas, Minutos y Segudos empleando un Timer
    # De preferencia, de 24hrs
    #Tarea: Buscar como reproducir efectos de sonido en python

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())