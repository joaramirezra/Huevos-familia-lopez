import sys
sys.path.append(".")

from .archivos import escribir_cuentas, obtener_cuentas_productos
from .archivos import obtener_cuentas,reiniciar_cuentas_producto
from .archivos import escribir_inventario,cantidad_producto, obtener_inventario
from .archivos import obtener_inventario_productos,reiniciar_inventario_producto

inventario_pollos = ['pollos','alimento_pollos']
cuentas_pollos = ['pollos']
deudas_pollos = ['Agropaisa_pollos','San_Alejo_pollos']


def contabilidad_pollos():
    df = obtener_cuentas_productos(cuentas_pollos)
    ingresos = df[df['transaccion']=='ingreso']['cantidad'].sum()
    egresos =  df[df['transaccion']=='egreso']['cantidad'].sum()
    return ingresos,egresos,ingresos+egresos

def compra_pollos(cantidad,precio):
    #Cuentas
    valor = cantidad*precio
    motivo = f'compra de {cantidad} pollos V/U {precio} pesos , total {valor} pesos'
    escribir_cuentas('pollos','egreso',-valor,motivo)
    # Inventario 
    escribir_inventario('pollos','ingreso',cantidad,motivo)

def matar_pollos(cantidad):
    motivo = f'muerte de {cantidad} pollos'
    escribir_inventario('pollos','egreso',-cantidad,motivo)

def apoyo_caja_pollo(cantidad):
    motivo = f'Apoyo a la caja por valor de {cantidad} PESOS'    
    escribir_cuentas('pollos','ingreso',cantidad,motivo)

def enviar_banco_pollos(cantidad):
    motivo = f'Se enviarion {cantidad} pesos al banco'
    escribir_cuentas('pollos','egreso',-cantidad,motivo)

def venta_produccion_pollos(cantidad,precio):
    valor = cantidad*precio
    motivo = f' Venta de {cantidad} kilos de pollo a {precio} pesos, total {valor} pesos'
    escribir_cuentas('pollos','ingreso',valor,motivo)

def cantidad_pollos_vivos():
    return cantidad_producto('pollos')

def cantidad_totales():
    df = obtener_inventario_productos(['pollos'])
    cantidad = df[df['transaccion']=='ingreso']['cantidad'].sum()
    return cantidad

def reiniciar_pollos():
    reiniciar_inventario_producto('pollos')
    reiniciar_cuentas_producto('pollos')

def calcular_mortalidad():
    if (cantidad_totales() == 0):
        return 0
    else:
        return cantidad_pollos_vivos()/cantidad_totales()

def transaccion_pollos():
    columnas = ['fecha','cantidad','motivo']
    return obtener_cuentas_productos(['pollos'])[columnas].tail(9)

def cantidad_efectivo_pollos():
    _,_,saldo = contabilidad_pollos()
    return saldo