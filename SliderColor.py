import sys

from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "SliderColor.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.hs_B.setMinimum(159)
        self.hs_B.setMaximum(255)
        self.hs_B.setSingleStep(1)
        self.hs_B.setValue(0)
        self.txt_valor_B.setText("0")

        self.hs_B.valueChanged.connect(self.cambioB)

        self.B = 0


    # area de slots

    def cambioB(self):
        self.B = self.hs_B.value()
        self.txt_valor_B.setText(str(self.B))
        colorFondo = "background-color: rgb("+str(145)+","+str(157)+"," + str(self.B) + ");"
        self.btn_color.setStyleSheet(colorFondo)

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
