import sys
sys.path.append(".")

import pandas as pd
from .manejo_lineas import crear_linea_con_fecha

def Crear_pollos():
	file = open("./files/manejo_pollos.csv",'w+')
	file.write('fecha;motivo;cantidad;precio;tipo'+'\n')
	file.close()

def agregar_venta_pollos(*valores):
	file = open("./files/manejo_pollos.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(*valores)
	file.write(linea+'\n')
	file.close()

def registro_pollos():
	df = pd.read_csv("./files/manejo_pollos.csv",sep=';',index_col=False,error_bad_lines=False)
	return df

def valores_pollos():
	df = registro_pollos()
	
	df['precio'] = pd.to_numeric(df['precio'] )

	ingresos = df[df['precio']>0]
	ingresos = int(ingresos['precio'].sum())
	
	egresos = df[df['precio']<0]
	egresos = int(egresos['precio'].sum())
	
	saldo = ingresos + egresos
	return ingresos,egresos,saldo

def reiniciar_produccion():
	saldo = valores_pollos()[2]
	Crear_pollos()
	motivo = 'saldo produccion anterior '
	agregar_venta_pollos(motivo,'0',str(saldo),'1')

