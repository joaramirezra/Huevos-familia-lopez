from datetime import datetime

def crear_linea_con_fecha(*parametros):
	hoy = str(datetime.today().strftime('%d/%m/%Y'))
	linea = ";".join([hoy,*parametros])
	return linea