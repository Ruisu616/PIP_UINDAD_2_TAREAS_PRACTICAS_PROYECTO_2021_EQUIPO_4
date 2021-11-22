import sys
from playsound import playsound

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P12_BarraProgreso.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)


        self.btn_iniciar.clicked.connect(self.iniciar)

        self.progressBar.setValue(0)
        self.cont = 0

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.progreso)

    #area de slots
    def iniciar(self):
        self.cont = 0
        self.segundoPlano.start(1) #1000 = 1seg

        #import time as t
        #for i in range(self.cont, 101,1):
        #    #print(i)
        #    self.progressBar.setValue(i)
        #    t.sleep(0.25)

    def progreso(self):
        self.progressBar.setValue(self.cont)
        self.cont += 0.25
        if  self.cont == 101:
            print("Se lleno la barra de progreso")
            playsound('windows.wav')
            self.segundoPlano.stop()

    #programa: Dada una barra de progreso, cada n porcentaje que se llene la barra
    #ejecutar un sonido que notique al usuario que se llego a este valor.

    #ejemplo: cada 10% reproducir un sonido, y reproducir un sonido diferente cuando se llegue al 100%



    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())