archivos = {
	'compras'       : 'fecha;motivo;precio',
	'credito'       : 'fecha;motivo;precio',
	'venta_empaque' : 'fecha;cantidad;precio',
	'gasto_alimento': 'fecha;galpon;cantidad',
	'caja_mayor'    : 'fecha;motivo;cantidad_dinero',
	'manejo_galpon' : 'fecha;cantidad_pollitas;cantidad_gallinas',
	'ingreso_huevos': 'fecha;galpon;tipo;unidades;cubeta;sobrantes',
	'venta_huevos'  : 'fecha;tipo;unidades;cubeta;sobrantes;precio;observacion',
}

#------------------------------------------------------------------------------
# Asociados al manejo de archivos

def crear_archivo(nombre:str,header:str):
	f = open("./files/"+nombre+".csv", "w+")
	f.write(header)
	f.write('\n')
	f.close()
	return True

def crear_archivos():
	[crear_archivo(key,archivos[key]) for key in archivos]
	return True