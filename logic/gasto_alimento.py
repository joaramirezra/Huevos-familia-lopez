from manejo_lineas import crear_linea_con_fecha


tipo_de_gallina = ['POLLITA','GALLINA']
tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO_VENTA','DESTRUIDOS']
presentacion_huevos = ['unidad','cubeta','sobrante']

def consumo_de_alimento(galpon,bultos):
	file = open("./files/gasto_alimento.csv",'a')
	tipo_galpon = tipo_de_gallina[galpon]
	# agregar segun posicion 
	linea = crear_linea_con_fecha(tipo_galpon,bultos)
	file.write(linea+'\n')
	file.close()
	