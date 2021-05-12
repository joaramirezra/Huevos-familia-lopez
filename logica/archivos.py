from datetime import datetime
import pandas as pd

archivos = {'inventario'  : 'fecha;producto;transaccion;cantidad;motivo',
	        'cuentas'     : 'fecha;producto;transaccion;cantidad;motivo'
	        }

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def crear_archivo(nombre:str,header:str):
	f = open("./files/"+nombre+".csv", "w+")
	f.write(header)
	f.write('\n')
	f.close()
	return True

def crear_archivos():
	[crear_archivo(key,archivos[key]) for key in archivos]
	return True

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def obtener_fecha_hoy():
    return  datetime.today().strftime('%d/%m/%Y')

def cantidad_producto(producto):
    df = obtener_inventario_productos([producto])
    return  df['cantidad'].sum()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def escribir_inventario(producto ,transaccion ,cantidad ,motivo ):
    producto,transaccion = str(producto),str(transaccion)
    cantidad ,motivo = str(cantidad) ,str(motivo)
    
    hoy = obtener_fecha_hoy()
    cadena = ";".join([hoy,producto,transaccion,cantidad,motivo+'\n'])
    
    with open("./files/inventario.csv", "a+") as file :
        file.write(cadena)
    
def escribir_cuentas(producto ,transaccion ,cantidad ,motivo ):
    producto,transaccion = str(producto),str(transaccion)
    cantidad ,motivo = str(cantidad) ,str(motivo)
    
    hoy = obtener_fecha_hoy()
    cadena = ";".join([hoy,producto,transaccion,cantidad,motivo+'\n'])
    
    with open("./files/cuentas.csv", "a+") as file :
        file.write(cadena)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def obtener_inventario():
    return pd.read_csv("./files/inventario.csv",sep=';')

def obtener_cuentas():
    return pd.read_csv("./files/cuentas.csv",sep=';')

def obtener_inventario_productos(productos):
    df = obtener_inventario()
    return df[df['producto'].isin(productos)]

def obtener_cuentas_productos(productos):
    df = obtener_cuentas()
    return df[df['producto'].isin(productos)]

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def reiniciar_inventario():
    crear_archivo('inventario',archivos['inventario'])

def reiniciar_cuentas():
    crear_archivo('cuentas',archivos['cuentas'])

#-------------------------------------------------------------------------------
def reiniciar_cuentas_producto(producto):
    df =obtener_cuentas()
    df = df[df['producto'] != producto]
    df.to_csv('./files/cuentas.csv',sep = ';', index = False)

def reiniciar_inventario_producto(producto):
    df =obtener_inventario()
    df = df[df['producto'] != producto]
    df.to_csv('./files/inventario.csv',sep = ';', index = False)

# reiniciar_inventario()
# reiniciar_cuentas()
