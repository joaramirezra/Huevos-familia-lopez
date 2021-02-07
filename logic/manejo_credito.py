from manejo_lineas import crear_linea_con_fecha
import pandas as pd
def ingresar_fiado(motivo,precio,es_alimento,cantidad):
	file = open("./files/credito.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(motivo,precio,es_alimento,cantidad)
	file.write(linea+'\n')
	file.close()

def ingresar_fiado_alimento(cantidad,precio):
	motivo = 'fiado de '+ str(cantidad)+ ' bultos de alimento'
	ingresar_fiado(motivo,precio,'1',cantidad)

def ingresar_fiado_caja_menor(motivo,precio):
	ingresar_fiado(motivo,precio,'0','0')

def obtener_cantidad_bultos_fiados():
	df = pd.read_csv("./files/credito.csv",sep=';')
	df = df[df['es_alimento']==True]
	bultos = df['cantidad'].sum()
	return bultos

def obtener_total_credito():
	df = pd.read_csv("./files/credito.csv",sep=';')
	return  df['precio'].sum()
	 