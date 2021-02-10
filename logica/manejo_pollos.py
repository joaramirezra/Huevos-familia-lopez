import sys
sys.path.append(".")

import pandas as pd
from .manejo_lineas import crear_linea_con_fecha
from .manejo_huevos import *

def Crear_pollos():
	file = open("./files/manejo_pollos.csv",'w+')
	file.write('fecha;motivo;cantidad;precio')
	file.close()

def agregar_venta_pollos(*valores):
	file = open("./files/manejo_pollos.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(*valores)
	file.write(linea+'\n')
	file.close()

def registro_pollos():
	df = pd.read_csv("./files/manejo_pollos.csv",sep=';',index_col=False,error_bad_lines=False)
	return df


