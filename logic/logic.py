from datetime import datetime
import pandas as pd

from manejo_archivos import crear_archivos
from manejo_huevos import *
from manejo_ventas import *
from manejo_inventario  import inventario
from manejo_galpon import *
from venta_empaques import venta_empaques
from gasto_alimento import consumo_de_alimento
from manejo_compras import ingresar_compra
from manejo_credito import ingresar_fiado
from manejo_caja_mayor import registro_caja

# crear_archivos()
# venta_empaques('5','600')
# consumo_de_alimento(1,'8')
# ingresar_compra('prueba','450000')
# ingresar_fiado('prueba','450000')
# registro_caja('prueba','450000')

agregar_huevos(0,0,'3','130','9')
agregar_venta(4,'1','0','0','510000','venta a don predo')
agregar_animales('-1500','1000')


print(obtener_produccion_diaria())
print(obtener_produccion())
print(inventario())
print(venta_acumulada_dias().groupby('tipo').sum().reset_index())
print(obtener_animales())