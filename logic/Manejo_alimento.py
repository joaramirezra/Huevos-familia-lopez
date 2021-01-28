from manejo_lineas import crear_linea_con_fecha

#-------------------------------------------------------------------------------
def iniciarlizar_cantidad_alimento():
	file = open('./files/inventario_alimento_y_costales.csv','a')
	file.writelines( crear_linea_con_fecha('0','0')+'\n')
	file.close()

def Cantidad_bultos():
	file = open('./files/inventario_alimento_y_costales.csv','r')
	lineas = file.readlines()
	_,bultos,costales = lineas[len(lineas)-1].split(';')
	return bultos,costales

def aumentar_bultos(cantidad):
	bultos,costales  = Cantidad_bultos()
	bultos = int(bultos)+cantidad
	file = open('./files/inventario_alimento_y_costales.csv','a')
	file.write( crear_linea_con_fecha(str(bultos),str(costales)))
	file.close()

def disminuir_bultos(cantidad):
	bultos,costales  = Cantidad_bultos()
	bultos = int(bultos)-cantidad
	costales = int(costales)+ cantidad
	file = open('./files/inventario_alimento_y_costales.csv','a')
	file.write( crear_linea_con_fecha(str(bultos),str(costales))+'\n')
	file.close()

def disminuir_costales(cantidad):
	bultos,costales  = Cantidad_bultos()
	costales = int(costales) - cantidad
	file = open('./files/inventario_alimento_y_costales.csv','a')
	file.write( crear_linea_con_fecha(str(bultos),str(costales))+'\n')
	file.close()

