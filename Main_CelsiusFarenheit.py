import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "CelsiusFarenheit.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)



        # Área de los Signals
        self.SliderC.valueChanged['int'].connect(self.slider_c)
        self.SliderF.valueChanged['int'].connect(self.slider_f)


    # Área de los Slots
    def slider_c(self):
        self.txt_C.setText(str(self.SliderC.value()))
        f = self.SliderC.value() * (9 / 5) + 32
        self.SliderF.setValue(round(f))

    def slider_f(self):
        self.txt_F.setText(str(self.SliderF.value()))
        c = (5 / 9) * (self.SliderF.value() - 32)
        self.SliderC.setValue(round(c))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())