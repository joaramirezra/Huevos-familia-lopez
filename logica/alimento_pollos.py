import sys
sys.path.append(".")

from .archivos import escribir_inventario, cantidad_producto
from .caja_pollos import obtener_cuentas_productos
from .archivos import escribir_cuentas
from .archivos import reiniciar_cuentas_producto
from .archivos import reiniciar_inventario_producto

def cantidad_bultos_pollos():
    return cantidad_producto('alimento_pollos')

def cantidad_deuda_pollos(entidad):
    return obtener_cuentas_productos([entidad])['cantidad'].sum()

def gastos_general_pollos(cantidad,motivo):
    motivo = f'gasto de {cantidad} pesos con motivo de : {motivo} '
    escribir_cuentas('pollos','egreso',-cantidad,motivo)

def gastar_alimento_pollos(cantidad):
    motivo = f'Gasto de {cantidad} bultos de alimento'
    escribir_inventario('alimento_pollos','egreso',-cantidad,motivo)
    escribir_inventario('empaques','ingreso' ,cantidad ,motivo )
    

def devolver_alimento_pollos(cantidad):
    motivo = f'devolucion de {cantidad} bultos de alimento'
    escribir_inventario('alimento_pollos','ingreso',cantidad,motivo)
    escribir_inventario('empaques','egreso' ,-cantidad ,motivo )
    
def comprar_alimento_pollos(cantidad,precio):
    #cuentas
    valor = cantidad*precio
    motivo = f'compra de {cantidad} bultos a {precio} pesos, valor total {valor} pesos'
    escribir_cuentas('pollos','egreso',-valor,motivo)
    #inventario 
    motivo = f'compra de {cantidad} de bultos '
    escribir_inventario('alimento_pollos','ingreso',cantidad ,motivo)

def fiar_alimento_pollos(cantidad, precio, entidad):
    valor = cantidad*precio 
    motivo = f'credito de {cantidad} bultos a {precio} pesos, valor total {valor} pesos'
    escribir_cuentas(entidad,'ingreso',valor,motivo)
    #inventario 
    motivo = f'credito de {cantidad} de bultos '
    escribir_inventario('alimento_pollos','ingreso',cantidad ,motivo)
    
def abonar_deuda_pollos(cantidad,entidad):
    motivo = f'abono de {cantidad} pesos a {entidad}'
    escribir_cuentas('pollos','egreso',-cantidad,motivo)
    escribir_cuentas(entidad,'egreso',-cantidad,motivo)

def desabonar_deuda_pollos(cantidad,entidad):
    motivo = f'Correccion abono de {cantidad} pesos a {entidad}'
    escribir_cuentas('pollos','ingreso',cantidad,motivo)
    escribir_cuentas(entidad,'ingreso',cantidad,motivo)

def valor_deudad_pollos(entidad):
    df = obtener_cuentas_productos([entidad])
    if(df.shape[0]==0):
        return 0
    else:
        return df['cantidad'].sum()

def reiniciar_pollos():
    reiniciar_cuentas_producto('pollos')
    reiniciar_cuentas_producto('Agropaisa_pollos')
    reiniciar_cuentas_producto('San alejo_pollos')
    reiniciar_inventario_producto('alimento_pollos')         
    reiniciar_inventario_producto('pollos')
    