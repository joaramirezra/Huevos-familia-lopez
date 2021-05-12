import sys
sys.path.append(".")

import pandas as pd
from .manejo_lineas import crear_linea_con_fecha
from .manejo_huevos import *

tipo_de_gallina = ['POLLITA','GALLINA']
tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO_VENTA','DESTRUIDOS']
presentacion_huevos = ['unidad','cubeta','sobrante']

# def Crear_limon():
# 	file = open("./files/manejo_limon.csv",'w+')
# 	file.write('fecha;motivo;precio')
# 	file.close()

def agregar_venta_limon(*valores):
	file = open("./files/manejo_limon.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(*valores)
	file.write(linea+'\n')
	file.close()

def registro_limones():
	df = pd.read_csv("./files/manejo_limon.csv",sep=';',index_col=False,error_bad_lines=False)
	return df


