from manejo_lineas import crear_linea_con_fecha

def ingresar_compra(motivo,cantidad):
	file = open("./files/compras.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(motivo,cantidad)
	file.write(linea+'\n')
	file.close()