archivos = {
	'compras'       : 'fecha;motivo;precio;es_alimento;cantidad',
	'credito'       : 'fecha;motivo;precio;es_alimento;cantidad',
	'venta_empaque' : 'fecha;cantidad;precio',
	'gasto_alimento': 'fecha;galpon;cantidad',
	'caja_mayor'    : 'fecha;motivo;cantidad_dinero',
	'manejo_galpon' : 'fecha;cantidad_pollitas;cantidad_gallinas',
	'ingreso_huevos': 'fecha;galpon;tipo;unidades;cubeta;sobrantes',
	'venta_huevos'  : 'fecha;tipo;unidades;cubeta;sobrantes;precio;observacion',
	'manejo_cacao'  : 'fecha;motivo;cantidad;precio',
	'manejo_fletes' : 'fecha;motivo;cantidad;precio',
	'manejo_limon'  : 'fecha;motivo;cantidad;precio',
	'manejo_pollos' : 'fecha;motivo;cantidad;precio;tipo', # 0 pollo , 1 venta , 2 alimento
	'produccion_diaria':'galpon;tipo;unidades;cubeta;sobrantes',
	'manejo_ganancias' :'fecha;cantidad;precio'
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

crear_archivos()
