from manejo_lineas import crear_linea_con_fecha
import pandas as pd
from manejo_credito import obtener_cantidad_bultos_fiados

def ingresar_compra(motivo,precio,es_alimento,cantidad):
	file = open("./files/compras.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(motivo,precio,es_alimento,cantidad)
	file.write(linea+'\n')
	file.close()

def ingresar_compra_alimento(cantidad,precio):
	motivo = 'Compra de '+ str(cantidad)+ ' bultos de alimento'
	ingresar_compra(motivo,precio,'1',cantidad)

def ingresar_compra_caja_menor(motivo,precio):
	ingresar_compra(motivo,precio,'0','0')

def obtener_cantidad_bultos_comprados():
	df = pd.read_csv("./files/compras.csv",sep=';')
	df = df[df['es_alimento']==True]
	bultos = df['cantidad'].sum()+obtener_cantidad_bultos_fiados()
	return bultos

def obtener_total_compras():
	df = pd.read_csv("./files/compras.csv",sep=';')
	return  df['precio'].sum()
	 
