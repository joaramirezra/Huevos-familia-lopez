from pyqtgraph import PlotWidget
from datetime import datetime
import pandas as pd

from manejo_archivos import crear_archivos
from manejo_huevos import *
from manejo_ventas import *
from manejo_inventario  import inventario
from manejo_galpon import *
from venta_empaques import *
from gasto_alimento import *
from manejo_compras import *
from manejo_credito import *
from manejo_caja_mayor import *

# crear_archivos()
# venta_empaques('5','600')
# consumo_de_alimento(1,'8')
# ingresar_compra('prueba','450000')
# ingresar_fiado('prueba','450000')
# registro_caja('prueba','450000')

# agregar_huevos(0,0,'3','130','9')
# agregar_venta(0,'0','2','0','510000','venta a don predo')
# consumo_de_alimento(0,'5')
# venta_empaques('5','684')
# ingresar_compra_alimento('9','8000')
# ingresar_compra_caja_menor('gasolina','5000')
# agregar_animales('1500','1000')

# print(obtener_produccion_diaria())
# print(obtener_produccion())
# print(inventario())
# print(venta_acumulada_dias().groupby('tipo').sum().reset_index())
# print(obtener_animales())
# print(obtener_consumo_alimento())
# print(cantidad_de_empaques())
# print(obtener_total_compras())
# print(obtener_cantidad_bultos_comprados())
# print(obtener_cantidad_bultos())
# print(venta_total())

def validar_numeros(*numeros):
    valido = 0
    for numero in numeros:
        numero = str(numero)
        valido +=  (numero.isnumeric()) 
    
    return True if (valido == len(numeros)) else False


    