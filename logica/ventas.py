import sys
sys.path.append(".")

from .archivos import escribir_inventario,escribir_cuentas
from .archivos import obtener_inventario_productos,obtener_cuentas_productos
from .archivos import obtener_fecha_hoy
from .produccion import obtener_inventario_huevos_diario
from .produccion import tipos_huevo,conversion
import pandas as pd

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def agregar_venta(presentacion,tipo,cantidad,precio,observacion):
    # Cuentas
    valor = cantidad*precio
    motivo = f'venta de {cantidad} {presentacion} con valor total de {valor}'    
    cantidad = cantidad*30 if presentacion == 'CUBETAS' else cantidad
    escribir_cuentas(tipo,'ingreso',valor,motivo)
    # inventario 
    motivo = f'venta de {cantidad} huevos, como {presentacion}'    
    escribir_inventario(tipo ,'egreso' ,-cantidad ,motivo )

def devolucion_venta(presentacion,tipo,cantidad,precio,observacion):
    # Cuentas
    valor = cantidad*precio
    motivo = f'devolucion de {cantidad} {presentacion} con valor  de {valor}'    
    cantidad = cantidad*30 if presentacion == 'CUBETAS' else cantidad
    escribir_cuentas(tipo,'egreso',-valor,motivo)
    # inventario 
    motivo = f'devolucion de {cantidad} huevos, debido a '+observacion    
    escribir_inventario(tipo ,'egreso' ,cantidad ,motivo )

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def obtener_inventario_total():
    df = obtener_inventario_productos(tipos_huevo)

    if(len(df['producto'].unique()) < len(tipos_huevo) ):
        huevos = pd.DataFrame()
        huevos['producto'] = tipos_huevo
        df = pd.merge(df,huevos,on  = 'producto',how='outer') 
        df.fillna('0',inplace = True)
    
    df = df.groupby(['producto'])['cantidad'].sum().reset_index()
    df['cubetas'],df['unidades'],df['sobrantes'] = zip(*df['cantidad'].apply(conversion))
    
    ventas = obtener_cuentas_productos(tipos_huevo)
    if(len(ventas['producto'].unique()) < len(tipos_huevo) ):
        huevos = pd.DataFrame()
        huevos['producto'] = tipos_huevo
        ventas = pd.merge(ventas,huevos,on  = 'producto',how='outer') 
        ventas.fillna('0',inplace = True)
    
    ventas = ventas.groupby(['producto','fecha'])['cantidad'].sum().reset_index()

    ventas = ventas[ventas['fecha'] == obtener_fecha_hoy()]

    if(len(ventas['producto'].unique()) < len(tipos_huevo) ):
        huevos = pd.DataFrame()
        huevos['producto'] = tipos_huevo
        ventas = pd.merge(ventas,huevos,on  = 'producto',how='outer') 
        ventas.fillna('0',inplace = True)
        
    ventas.rename(columns = {'cantidad':'ventas_del_dia'},inplace =True)
    
    df = pd.merge(df,ventas,on  = 'producto',how='outer') 
    
    return df.drop(columns='fecha')

def cantidad_huevos_inventario(tipo):
    df = obtener_inventario_total()
    return df[df['producto']==tipo]['cantidad'].sum()

def inventario_total_huevos():
    df = obtener_inventario_total()
    cantidad = df['cantidad'].astype(int).sum()
    cubeta,unidades,sobrantes = conversion(cantidad)

    ventas = obtener_cuentas_productos(tipos_huevo)
    cantidad = ventas[ventas['fecha'] == obtener_fecha_hoy()]['cantidad'].sum()
    return cubeta,unidades,sobrantes,cantidad

