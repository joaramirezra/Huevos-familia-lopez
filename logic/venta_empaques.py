from manejo_lineas import crear_linea_con_fecha

def venta_empaques(*valores):
	file = open("./files/venta_empaque.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(*valores)
	file.write(linea+'\n')
	file.close()