import sys
sys.path.append(".")
import pandas as pd

from .manejo_lineas import crear_linea_con_fecha

def entrada_contabilidad(cantidad,total):
	file = open("./files/manejo_ganancias.csv",'a')
	linea = crear_linea_con_fecha(cantidad,total)
	file.write(linea+'\n')
	file.close()

def inicializar_contabilidad():
	entrada_contabilidad('0','0')

def obtener_contabilidad():
	return pd.read_csv("./files/manejo_ganancias.csv",sep=';',index_col=False)

def calular_ganancia_semanal():
	df = obtener_contabilidad()
	
	if(df.shape[0]<1):
		inicializar_contabilidad()
		return calular_ganancia_semanal()

	df['fecha'] = pd.to_datetime(df['fecha']) 
	df = df.groupby(pd.Grouper(key = 'fecha',freq = 'W-WED')).sum().reset_index()

	return df

def calular_ganancia_mensual():
	df = obtener_contabilidad()
	df['fecha'] = pd.to_datetime(df['fecha']) 
	df = df.groupby(pd.Grouper(key = 'fecha',freq = 'M')).sum().reset_index()
	return df