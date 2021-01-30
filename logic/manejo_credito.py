from manejo_lineas import crear_linea_con_fecha

def ingresar_fiado(motivo,cantidad):
	file = open("./files/credito.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(motivo,cantidad)
	file.write(linea+'\n')
	file.close()