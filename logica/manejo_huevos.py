import sys
sys.path.append(".")
from .manejo_lineas import crear_linea_con_fecha
import pandas as pd 
from datetime import datetime


tipo_de_gallina = ['POLLITA','GALLINA']
tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO_VENTA','DESTRUIDOS']
presentacion_huevos = ['unidad','cubeta','sobrante']

#------------------------------------------------------------------------------
# Asociados al manejo de huevos
def llenar_inicio_dia_inventario():
	f = open("./files/ingreso_huevos.csv", "a")	
	for tipo in tipo_de_gallina:
		for huevo in tipos_huevo:
				f.write(crear_linea_con_fecha(tipo,huevo,'0','0','0')+'\n')

def agregar_huevos(galpon,tipo,*valores):
	file = open("./files/ingreso_huevos.csv",'a')
	tipo_gallina = tipo_de_gallina[galpon]
	tipo_huevo = tipos_huevo[tipo]
	linea = crear_linea_con_fecha(tipo_gallina,tipo_huevo,*valores)
	file.write(linea+'\n')
	file.close()
	df = obtener_produccion()
	if (len(df['tipo'].unique())<9):
		llenar_inicio_dia_inventario()

def obtener_produccion():
	df = pd.read_csv("./files/ingreso_huevos.csv",sep=';',index_col=False,error_bad_lines=False)
	df = df.groupby('tipo').sum().reset_index()
	return df

def obtener_produccion_historia():
	df = pd.read_csv("./files/ingreso_huevos.csv",sep=';',index_col=False,error_bad_lines=False)
	df['fecha'] = pd.to_datetime(df['fecha'])
	df.sort_values(by='fecha',ascending = True,inplace = True)
	df = df.groupby(['fecha','galpon']).sum().reset_index()
	df['total_huevos'] = df['unidades']+df['sobrantes']
	return df[['fecha','galpon','total_huevos']]


def obtener_produccion_diaria():
	df = pd.read_csv("./files/ingreso_huevos.csv",sep=';',index_col=False,error_bad_lines=False)
	hoy = str(datetime.today().strftime('%d/%m/%Y'))
	df = df[df['fecha'] == hoy]
	
	if (df['tipo'].shape[0] < 18 ):
		llenar_inicio_dia_inventario()
	
	df = pd.read_csv("./files/ingreso_huevos.csv",sep=';',index_col=False,error_bad_lines=False)
	hoy = str(datetime.today().strftime('%d/%m/%Y'))
	df = df[df['fecha'] == hoy]
	df = df.groupby(['galpon','tipo']).sum().reset_index()
	df['cubeta'] += df['sobrantes']//30
	df['sobrantes'] = df['sobrantes']%30
	df.to_csv('./files/produccion_diaria.csv',sep=';',index= False)
	
	return df