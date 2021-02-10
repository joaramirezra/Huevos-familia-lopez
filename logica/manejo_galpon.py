import sys
sys.path.append(".")

import pandas as pd
from .manejo_lineas import crear_linea_con_fecha
from .manejo_huevos import *

tipo_de_gallina = ['POLLITA','GALLINA']
tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO_VENTA','DESTRUIDOS']
presentacion_huevos = ['unidad','cubeta','sobrante']

def agregar_animales(*valores):
	file = open("./files/manejo_galpon.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(*valores)
	file.write(linea+'\n')
	file.close()

def obtener_animales():
	df = pd.read_csv("./files/manejo_galpon.csv",sep=';',index_col=False,error_bad_lines=False)
	suma = df[['cantidad_pollitas','cantidad_gallinas']].sum()
	return suma.values

def obtener_historico_animales():
	df = pd.read_csv("./files/manejo_galpon.csv",sep=';',index_col=False,error_bad_lines=False)
	df = df.groupby('fecha').sum().reset_index()
	df['fecha'] = pd.to_datetime(df['fecha'])
	df.sort_values(by='fecha',ascending=True,inplace=True)
	df['acumulado_pollitas'] = df['cantidad_pollitas'].cumsum()
	df['acumulado_gallinas'] = df['cantidad_gallinas'].cumsum()
	df.drop(columns = ['cantidad_pollitas','cantidad_gallinas'],inplace = True)
	return df

def calcular_cantidad_huevos(unidades,cubetas,sobrantes):
	return unidades+sobrantes

def calcular_rendimiento(huevos,animales):
	return round(huevos/animales,3)
	
def obtener_rendimiento_diario():
	produccion = obtener_produccion_diaria().groupby('galpon').sum()
	huevos_pollitas = calcular_cantidad_huevos(*produccion.iloc[1].values)
	huevos_gallina = calcular_cantidad_huevos(*produccion.iloc[0].values)
	
	pollitas,gallinas = obtener_animales()

	rendimiento_pollitas = calcular_rendimiento(huevos_pollitas,pollitas)
	rendimiento_gallinas = calcular_rendimiento(huevos_gallina,gallinas)
	
	return rendimiento_gallinas,rendimiento_pollitas

def Rendimiento_acumulado():
	historico_de_animales = obtener_historico_animales()
	prod_historica = obtener_produccion_historia()
	prod_historica_gallinas  = prod_historica[prod_historica['galpon']=='GALLINA']
	prod_historica_pollitas  = prod_historica[prod_historica['galpon']=='POLLITA']

	rend_hist_polli = pd.merge(historico_de_animales,prod_historica_pollitas,)
	rend_hist_galli = pd.merge(historico_de_animales,prod_historica_gallinas)
	his_polli =  rend_hist_polli['total_huevos']/rend_hist_polli['acumulado_pollitas']
	his_galli =  rend_hist_galli['total_huevos']/rend_hist_galli['acumulado_gallinas']
	return  his_polli,his_galli

