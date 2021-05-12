import sys
sys.path.append(".")

from .archivos import escribir_inventario,obtener_inventario_productos
from .archivos import obtener_fecha_hoy
import pandas as pd
tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO VENTA',
			   'DESTRUIDOS']

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def conversion(cantidad) :
    cantidad = int(cantidad)
    return cantidad//30,(cantidad//30)*30,cantidad%30

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def agregar_huevos(producto,cubetas,sobrantes):
    cantidad = cubetas*30+sobrantes
    motivo = f'Produccion de {cantidad} huevos tipo {producto}'    
    escribir_inventario(producto ,'ingreso' ,cantidad ,motivo )

def eliminar_huevos(producto,cubetas,sobrantes):
    cantidad = cubetas*30+sobrantes
    motivo = f'produccion de {cantidad} huevos tipo {producto}'    
    escribir_inventario(producto ,'ingreso' ,-cantidad ,motivo )

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def obtener_inventario_huevos_diario():
    hoy = obtener_fecha_hoy()

    df = obtener_inventario_productos(tipos_huevo)
    
    if(df.shape[0] == 0):
        agregar_huevos('A',0,0) 
        df = obtener_inventario_productos(tipos_huevo)
        
    df = df[df['fecha'] == hoy]

    if(df.shape[0] == 0):
        agregar_huevos('A',0,0) 
        df = obtener_inventario_productos(tipos_huevo)
    
    df = df[df['transaccion'].isin(['ingreso'])]
    
    df = df.groupby(['producto'])['cantidad'].sum().reset_index()
    df['cubetas'],df['unidades'],df['sobrantes'] = zip(*df['cantidad'].apply(conversion))
    
    if(len(df['producto'].unique()) < len(tipos_huevo) ):
        huevos = pd.DataFrame()
        huevos['producto'] = tipos_huevo
        df = pd.merge(df,huevos,on  = 'producto',how='outer') 
        df.fillna('0',inplace = True)

    return df[['producto','cubetas','unidades','sobrantes','cantidad']]

def cantidad_huevos_tipo(tipo):
    df = obtener_inventario_huevos_diario()
    df = df[df['producto'] == tipo]
    if(df.shape[0] == 0 ):
        return 0
    else :
        return df[df['producto'] == tipo]['cantidad'].sum()

def cantidad_total_huevos():
    df = obtener_inventario_huevos_diario()
    cantidad = df['cantidad'].astype(int).sum()
    cubeta,unidades,sobrantes = conversion(cantidad)
    return cubeta,unidades,sobrantes,cantidad

