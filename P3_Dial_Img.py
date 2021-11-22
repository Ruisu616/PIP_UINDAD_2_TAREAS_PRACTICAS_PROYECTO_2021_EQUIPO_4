import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P3_Dial_lmg.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.dial.setMinimum(0)
        self.dial.setMaximum(5)
        self.dial.setSingleStep(1)

        self.dial.setValue(0)
        #self.txt_valor.setText("0")

        self.dial.valueChanged.connect(self.valorCambio)

        self.diccionario = {}
        self.diccionario[0] = ["Jorge", "ISC", ":/images/Imagenes/1237433-middle.png"]
        self.diccionario[1] = ["Chris", "IC", ":/images/Imagenes/d.jpg"]
        self.diccionario[2] = ["Jeremias", "ISC", ":/images/Imagenes/descarga.jfif"]
        self.diccionario[3] = ["Karla", "II", ":/images/Imagenes/dg.png"]
        self.diccionario[4] = ["Granda", "IM", ":/images/Imagenes/spdr.png"]
        self.diccionario[5] = ["Villalobos", "IC", ":/images/Imagenes/images.jfif"]

        alumno = self.diccionario[0]
        self.txt_valor.setText(alumno[0])

        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

    #area de slots

    def valorCambio(self):
        valor = self.dial.value()
        print(valor)

        #valor = str(valor)
        #self.txt_valor.setText(valor)

        alumno = self.diccionario[valor]

        self.txt_valor.setText(alumno[0])
        print(alumno[1])

        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())