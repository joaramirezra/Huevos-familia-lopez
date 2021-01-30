import pandas as pd
from manejo_lineas import crear_linea_con_fecha

tipo_de_gallina = ['POLLITA','GALLINA']
tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO_VENTA','DESTRUIDOS']
presentacion_huevos = ['unidad','cubeta','sobrante']


def agregar_venta(tipo,*valores):
	file = open("./files/venta_huevos.csv",'a')
	tipo_huevo = tipos_huevo[tipo]
    # agregar segun posicion 
	linea = crear_linea_con_fecha(tipo_huevo,*valores)
	file.write(linea+'\n')
	file.close()

def llenar_inventario_venta():
	f = open("./files/venta_huevos.csv", "a")	
	for huevo in tipos_huevo:
			f.write(crear_linea_con_fecha(huevo,'0','0','0','0','0')+'\n')

def obtener_venta_huevos():
	df = pd.read_csv("./files/venta_huevos.csv",sep=';',index_col=False)
	df = df[['tipo','unidades','cubeta','sobrantes']]
	if (len(df['tipo'].unique())<9):
		llenar_inventario_venta()
	df = df.groupby('tipo').sum().reset_index()
	return df

def venta_acumulada_dias():
	df = pd.read_csv("./files/venta_huevos.csv",sep=';',index_col=False)
	df = df[['fecha','tipo','precio']].groupby(['fecha','tipo']).sum().reset_index()
	return df