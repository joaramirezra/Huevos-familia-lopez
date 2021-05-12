import sys
sys.path.append(".")
from .archivos import escribir_cuentas, obtener_cuentas_productos
from .archivos import obtener_cuentas,reiniciar_cuentas_producto

def venta_limon(cantidad,precio,motivo):
    valor = cantidad*precio
    motivo = f'Venta de {cantidad} canastillas de limon por {valor} PESOS, observacio : {motivo}'    

    escribir_cuentas('limon','ingreso',valor,motivo)
    
def gastos_limon(valor, motivo):
    motivo = f'Gasto de  {valor} PESOS , concepto : {motivo}'    
    escribir_cuentas('limon','egreso',valor,motivo)

def contabilidad_limon():
    df = obtener_cuentas_productos(['limon'])
    ingresos = df[df['transaccion'] == 'ingreso']['cantidad'].sum()
    egresos = df[df['transaccion'] == 'egreso']['cantidad'].sum()
    return ingresos,egresos,ingresos-egresos        
    
def reiniciar_limon():
    reiniciar_cuentas_producto('limon')
    pass

def transacciones_limon():
    columnas = ['fecha','cantidad','motivo']
    return obtener_cuentas_productos(['limon'])[columnas].tail(13)
