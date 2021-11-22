import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer

qtCreatorFile = "T3_Semaforo automatizado con Colores.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.encender.clicked.connect(self.iniciar)
        self.apagar.clicked.connect(self.detener)
        self.timer_rojo = QTimer()
        #self.timer_rojo.setInterval(1000)
        self.timer_rojo.timeout.connect(self.Rojo)
        self.timer_amarillo = QTimer()
        #self.timer_amarillo.setInterval(350)
        self.timer_amarillo.timeout.connect(self.Amarillo)
        self.timer_verde = QTimer()
        #self.timer_verde.setInterval(1000)
        self.timer_verde.timeout.connect(self.Verde)
        self.timer_reinicia = QTimer()
        #self.timer_reinicia.setInterval(200)
        self.timer_reinicia.timeout.connect(self.Reiniciar)



    # Área de los Slots
    def iniciar(self):
        self.apagar.setEnabled(True)
        self.encender.setEnabled(False)
        self.timer_rojo.start(100)
        self.timer_amarillo.start(4000)
        self.timer_verde.start(5000)
        self.timer_reinicia.start(9000)
        #QTimer.singleShot(1, self.Rojo)
        #QTimer.singleShot(2000, self.Amarillo)
        #QTimer.singleShot(2500, self.Verde)
        #QTimer.singleShot(3000, self.Reiniciar)


    def detener(self):
        self.timer_rojo.stop()
        self.timer_amarillo.stop()
        self.timer_verde.stop()
        self.timer_reinicia.stop()
        self.apagar.setEnabled(False)
        self.encender.setEnabled(True)
        self.color_rojo.setStyleSheet("background-color: rgb(150, 150, 150);" + "border-radius: 50;")
        self.color_amarillo.setStyleSheet("background-color: rgb(150, 150, 150);" + "border-radius: 50;")
        self.color_verde.setStyleSheet("background-color: rgb(150, 150, 150);" + "border-radius: 50;")



    def Rojo(self):
        QTimer.singleShot(10, self.VerdeApagado)
        self.color_rojo.setStyleSheet("background-color: rgb(255, 0, 0);" + "border-radius: 50;")
        self.timer_rojo.stop()

    def Amarillo(self):
        QTimer.singleShot(10, self.RojoApagado)
        self.color_amarillo.setStyleSheet("background-color: rgb(255,255,0);" + "border-radius: 50;")
        self.timer_amarillo.stop()


    def Verde(self):
        QTimer.singleShot(10, self.AmarilloApagado)
        self.color_verde.setStyleSheet("background-color: rgb(0,255,0);" + "border-radius: 50;")
        self.timer_verde.stop()

    def RojoApagado(self):
        self.color_rojo.setStyleSheet("background-color: rgb(150, 150, 150);" + "border-radius: 50;")

    def AmarilloApagado(self):
        self.color_amarillo.setStyleSheet("background-color: rgb(150, 150, 150);" + "border-radius: 50;")

    def VerdeApagado(self):
        self.color_verde.setStyleSheet("background-color: rgb(150, 150, 150);" + "border-radius: 50;")

    def Reiniciar(self):
        self.timer_rojo.start()
        self.timer_amarillo.start()
        self.timer_verde.start()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
