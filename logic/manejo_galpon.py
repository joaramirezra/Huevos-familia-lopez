import pandas as pd
from manejo_lineas import crear_linea_con_fecha
from manejo_huevos import *

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
	df = pd.read_csv("./files/manejo_galpon.csv",sep=';',index_col=False)
	suma = df[['cantidad_pollitas','cantidad_gallinas']].sum()
	return suma.values

def calcular_cantidad_huevos(unidades,cubetas,sobrantes):
	return unidades*10*30+cubetas*30+sobrantes

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

print(obtener_rendimiento_diario())

