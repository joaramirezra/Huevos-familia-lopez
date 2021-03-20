import sys
sys.path.append(".")

import pandas as pd
from .manejo_lineas import crear_linea_con_fecha
from .manejo_huevos import *

def Crear_fletes():
	file = open("./files/manejo_fletes.csv",'w+')
	file.write('fecha;motivo;precio')
	file.close()

def agregar_venta_fletes(*valores):
	file = open("./files/manejo_fletes.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(*valores)
	file.write(linea+'\n')
	file.close()

def registro_fletes():
	df = pd.read_csv("./files/manejo_fletes.csv",sep=';',index_col=False,error_bad_lines=False)
	return df


