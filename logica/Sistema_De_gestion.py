from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import pandas as pd
from pyqtgraph import PlotWidget

from GUI import Ui_MainWindow
from logic import *
import sys
from manejo_huevos import agregar_huevos

class Hello_world(Ui_MainWindow):
    def __init__( self ):
        super().__init__()
        
    def setupUi( self, MW ):
        super().setupUi( MW )
        self.boton_agregar_produccion.clicked.connect(self.agregar_produccion_gui)
    
    def Eliminar(self):
        self.label.setText('HOLA')

    def agregar_produccion_gui(self):
        tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO',
                        'VENCIDO VENTA','DESTRUIDOS']
        
        cubetas = self.cubetas_produccion.text()
        sobrantes = self.sobrantes_produccion.text()
        
        galpon = self.galpon_produccion.currentText()
        galpon =  1 if(galpon == 'GALLINAS') else 0
        
        huevo  = self.tipo_produccion.currentText()
        huevo = tipos_huevo.index(huevo)
       
        if (validar_numeros(cubetas,sobrantes)):
            self.cubetas_produccion.clear()
            self.sobrantes_produccion.clear()
            cubetas , sobrantes = numero_de_cubetas(cubetas,sobrantes)
            unidades = str(numero_de_unidades(cubetas))
            agregar_huevos(galpon,huevo,unidades,str(cubetas),str(sobrantes))
            
 
def main():
 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Hello_world()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()


