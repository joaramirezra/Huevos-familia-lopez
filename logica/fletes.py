import sys
sys.path.append(".")
from .archivos import escribir_cuentas, obtener_cuentas_productos
from .archivos import obtener_cuentas,reiniciar_cuentas_producto

def venta_fletes(cantidad,precio,motivo):
    valor = cantidad*precio
    motivo = f' Realizacion de {cantidad} fletes por {valor} PESOS, observacion : {motivo}'
    escribir_cuentas('fletes','ingreso',valor,motivo)
    
def gastos_fletes(valor, motivo):
    motivo = f'Gasto de  {valor} PESOS , concepto : {motivo}'    
    escribir_cuentas('fletes','egreso',valor,motivo)

def contabilidad_fletes():
    df = obtener_cuentas_productos(['fletes'])
    ingresos = df[df['transaccion'] == 'ingreso']['cantidad'].sum()
    egresos = df[df['transaccion'] == 'egreso']['cantidad'].sum()
    return ingresos,egresos,ingresos-egresos        
    
def reiniciar_fletes():
    reiniciar_cuentas_producto('fletes')

def transacciones_fletes():
    columnas = ['fecha','cantidad','motivo']
    return obtener_cuentas_productos(['fletes'])[columnas].tail(8)
