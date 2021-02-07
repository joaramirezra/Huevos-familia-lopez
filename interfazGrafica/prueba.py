from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import Ui_MainWindow
import sys

class Hello_world(Ui_MainWindow):
    def __init__( self ):
        super().__init__()
        
    def setupUi( self, MW ):
        super().setupUi( MW )
        self.boton_agregar_produccion.clicked.connect(self.Eliminar)
        self.boton_eliminar_produccion.clicked.connect(self.Agregar)

    
    def Eliminar(self):
        self.label.setText('HOLA')
    def Agregar(self):
        self.label.setText('TIPO')

 
def main():
 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Hello_world()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()


