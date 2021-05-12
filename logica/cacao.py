import sys
sys.path.append(".")
from .archivos import escribir_cuentas, obtener_cuentas_productos
from .archivos import obtener_cuentas,reiniciar_cuentas_producto

def venta_cacao(cantidad,precio,motivo):
    valor = cantidad*precio
    motivo = f'Venta de {cantidad} kilos de cacao por {valor} PESOS, observacion : {motivo}'    

    escribir_cuentas('cacao','ingreso',valor,motivo)
    
def gastos_cacao(valor, motivo):
    motivo = f'Gasto de  {valor} PESOS , concepto : {motivo}'    
    escribir_cuentas('cacao','egreso',valor,motivo)

def contabilidad_cacao():
    df = obtener_cuentas_productos(['cacao'])
    ingresos = df[df['transaccion'] == 'ingreso']['cantidad'].sum()
    egresos = df[df['transaccion'] == 'egreso']['cantidad'].sum()
    return ingresos,egresos,ingresos-egresos        
    
def reiniciar_cacao():
    reiniciar_cuentas_producto('cacao')

def transacciones_cacao():
    columnas = ['fecha','cantidad','motivo']
    return obtener_cuentas_productos(['cacao'])[columnas].tail(8)
