import sys
sys.path.append(".")
import pandas as pd
from .manejo_lineas import crear_linea_con_fecha
from .manejo_compras import obtener_cantidad_bultos_comprados
from datetime import datetime

tipo_de_gallina = ['POLLITA','GALLINA']
tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO_VENTA','DESTRUIDOS']
presentacion_huevos = ['unidad','cubeta','sobrante']

def consumo_de_alimento(galpon,bultos):
	file = open("./files/gasto_alimento.csv",'a')
	# tipo_galpon = tipo_de_gallina[galpon]
	# agregar segun posicion 
	linea = crear_linea_con_fecha(galpon,bultos)
	file.write(linea+'\n')
	file.close()

def llenar_alimento_inicial():
	file = open("./files/gasto_alimento.csv",'a')
	linea = crear_linea_con_fecha('POLLITA','0')
	file.write(linea+'\n')
	linea = crear_linea_con_fecha('GALLINA','0')
	file.write(linea+'\n')
	file.close()


def obtener_consumo_alimento():
	df =pd.read_csv("./files/gasto_alimento.csv",sep=';',index_col=False)
	if(df.shape[0]< 1 ):
		llenar_alimento_inicial()
		return obtener_consumo_alimento()

	df = df.groupby(['fecha','galpon']).sum().reset_index()
	# tener fecha de hoy y pasarla a formato fecha
	hoy = datetime.today().strftime('%d/%m/%Y')
	hoy = pd.to_datetime(hoy,format = '%d/%m/%Y')

	df['fecha'] = pd.to_datetime(df['fecha'],format = '%d/%m/%Y')
	mascara =  (hoy -df['fecha']).dt.days <= 6 
	df = df[mascara]
	return df

def obtener_cantidad_bultos_gastados():
	consumo = obtener_consumo_alimento()
	return consumo['cantidad'].sum()

def obtener_cantidad_bultos_gastados_historico():
	df =pd.read_csv("./files/gasto_alimento.csv",sep=';',index_col=False)
	return df.groupby(['fecha','galpon']).sum().reset_index()


def obtener_cantidad_bultos():
	comprados = obtener_cantidad_bultos_comprados()
	gastados  =  obtener_cantidad_bultos_gastados()
	
	return comprados - gastados


