import sys
sys.path.append(".")
import pandas as pd

from .manejo_lineas import crear_linea_con_fecha

def registro_caja(motivo,cantidad):
	file = open("./files/caja_mayor.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(motivo,cantidad)
	file.write(linea+'\n')
	file.close()

def abono_agropaisa(cantidad):
	registro_caja('abono a agropaisa',cantidad)

def retiro_caja(cantidad):
	registro_caja('retiro de caja menor a caja mayor',cantidad)

def ingreso_caja(cantidad):
	registro_caja('ingreso a caja menor de caja mayor',cantidad)

def Cantidad_efectivo():
	df = pd.read_csv("./files/caja_mayor.csv",sep=';',index_col=False,error_bad_lines=False)
	return df['cantidad_dinero'].sum()

def obtener_registro_caja_mayor():
	df = pd.read_csv("./files/caja_mayor.csv",sep=';',index_col=False,error_bad_lines=False)
	return df.tail(3)

	