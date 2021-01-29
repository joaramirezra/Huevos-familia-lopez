from manejo_lineas import crear_linea_con_fecha
import pandas as pd 

tipo_de_gallina = ['POLLITA','GALLINA']
tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO_VENTA','DESTRUIDOS']
presentacion_huevos = ['unidad','cubeta','sobrante']
#------------------------------------------------------------------------------
# Asociados al manejo de huevos
#
def llenar_inicio_dia_inventario():
	f = open("./files/invetario_diario.csv", "a")	
	for tipo in tipo_de_gallina:
		for huevo in tipos_huevo:
				f.write(crear_linea_con_fecha(tipo,huevo,'0','0','0')+'\n')

def inicializar_inventario():
	f = open("./files/inventario_huevos.csv", "a")	
	for tipo in tipo_de_gallina:
		for huevo in tipos_huevo:
				f.write(crear_linea_con_fecha(tipo,huevo,'0','0','0')+'\n')

def agregar_al_registro(galpon,tipo,*valores):
    tipo_gallina = tipo_de_gallina[galpon]
    tipo_huevo = tipos_huevo[tipo]
    linea = crear_linea_con_fecha(tipo_gallina,tipo_huevo,*valores).split(';')
	df = pd.read_csv("./files/inventario_huevos.csv",sep=';')
	df.append()
	df.to_csv("./files/inventario_huevos.csv",sep=';')

def obtener_inventario():
	df = pd.read_csv("./files/inventario_huevos.csv",sep=';')
	print(df.head()) 

