archivos = {
	'caja_menor':'fecha;ffectivo;Deuda;Cupo',
	'ventas':'Fecha,unidades,cubetas,sobrantes,precio_total',
	'compras':'Fecha,unidades,cubetas,sobrantes,precio_total',
	'inventario_alimento_y_costales': 'fecha;cantidad_bultos;cantidad_costales',
	'inventario_huevos':'fecha;tipo_gallina;unidades;cubetas;sobrantes',
	'historico_invetario_diario': 'fecha;tipo_gallina;unidades;cubetas;sobrantes;total_nuevos',
	'invetario_diario': 'fecha;tipo_gallina;tipo;unidades;cubetas;sobrantes',
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