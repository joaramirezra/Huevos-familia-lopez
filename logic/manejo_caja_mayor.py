from manejo_lineas import crear_linea_con_fecha

def registro_caja(motivo,cantidad):
	file = open("./files/caja_mayor.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(motivo,cantidad)
	file.write(linea+'\n')
	file.close()