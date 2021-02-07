from manejo_lineas import crear_linea_con_fecha

def registro_caja(motivo,cantidad):
	file = open("./files/caja_mayor.csv",'a')
	# agregar segun posicion 
	linea = crear_linea_con_fecha(motivo,cantidad)
	file.write(linea+'\n')
	file.close()

def abono_agropaisa(cantidad):
	registro_caja('abono a agropaisa',cantidad)

def retiro_caja(cantidad):
	registro_caja('retiro de caja menor a caja mayor',cantidad)

def ingreso_caja(cantidad):
	registro_caja('ingreso a caja menor de caja mayor',cantidad)
