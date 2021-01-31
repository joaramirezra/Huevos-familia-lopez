from manejo_lineas import crear_linea_con_fecha
from gasto_alimento import obtener_consumo_alimento
 
import pandas as pd

def venta_empaques(*valores):
	file = open("./files/venta_empaque.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(*valores)
	file.write(linea+'\n')
	file.close()

def obterner_numero_empaques_vendidos():
	df = pd.read_csv("./files/venta_empaque.csv",sep=';')
	return df['cantidad'].sum()

def cantidad_de_empaques():
	df = obtener_consumo_alimento()
	cantidad_empaques_total = df['cantidad'].sum()
	cantidad_empaques_vendidos = obterner_numero_empaques_vendidos()
	return cantidad_empaques_total-cantidad_empaques_vendidos

