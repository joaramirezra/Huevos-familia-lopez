import sys
sys.path.append(".")
from .archivos import escribir_inventario,escribir_cuentas
from .archivos import obtener_inventario_productos,cantidad_producto
from .archivos import obtener_cuentas_productos
from .produccion import obtener_inventario_huevos_diario,tipos_huevo

transacciones = ['ingreso','egreso']
productos = ['alimento_gallinas','empaques','otros','banco',
             'gallinas','agropaisa_gallinas','san_alejo_gallinas']

             
val_efectivo = ['alimento_gallinas','empaques','otros','banco',
                'gallinas']+tipos_huevo
productos += tipos_huevo


# print(productos)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def comprar_alimento(bultos, precio):
    # Cuentas
    valor = bultos*precio
    motivo = f'compra de {bultos} bultos con valor total de {valor}'    
    escribir_cuentas('gallinas','egreso',-valor,motivo)
    
    # inventario 
    motivo = f'compra de {bultos} bultos de comida para gallinas'
    escribir_inventario('alimento_gallinas','ingreso' ,bultos ,motivo )

def credito_alimento(bultos, valor_unitario,entidad):
    # Cuentas
    valor = bultos*valor_unitario
    motivo = f'credito de {bultos} bultos con valor total de {valor}'    
    escribir_cuentas(entidad,'ingreso',valor,motivo)
    
    # inventario 
    motivo = f'credito de {bultos} bultos de comida para gallinas'
    escribir_inventario('alimento_gallinas','ingreso' ,bultos ,motivo )

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def alimentar_gallinas(cantidad):
    motivo = f'gasto de {cantidad} bultos de alimentos para gallinas '
    escribir_inventario('alimento_gallinas','egreso' ,-cantidad ,motivo )
    escribir_inventario('empaques','ingreso' ,cantidad ,motivo )
    

def devolver_alimento(cantidad):
    motivo = f'devolucion de {cantidad} bultos de alimentos para gallinas '
    escribir_inventario('alimento_gallinas','ingreso' ,cantidad ,motivo )
    escribir_inventario('empaques','egreso' ,-cantidad ,motivo )
    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def agregar_gallinas(cantidad):
    motivo = f'adquisicion de {cantidad} gallinas '
    escribir_inventario('gallinas','ingreso' ,cantidad ,motivo )
    
def matar_gallinas(cantidad):
    motivo = f'muerte de {cantidad} gallinas '
    escribir_inventario('gallinas','egreso' ,-cantidad ,motivo )

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def rendimiento_gallinas():
    df = obtener_inventario_huevos_diario()
    gallinas = cantidad_producto('gallinas')
    huevos_dia = df['cantidad'].astype(int).sum()
    rendimiento =  huevos_dia/gallinas if (gallinas != 0) else 0   
    return rendimiento

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def compra_aux_gallinas(valor,motivo):
    motivo = f'compra de {motivo} por valor de {valor} pesos'
    escribir_cuentas('gallinas','egreso' ,-valor , motivo)
    
def credito_aux_gallinas(valor,motivo):
    motivo = f'endeudamiento de {motivo} con valor de {valor} pesos'
    escribir_cuentas('Agropaisa_gallinas','ingreso' ,valor ,motivo )

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def apoyo_caja_menor_gallinas(valor):
    motivo = f'Apoyo de {valor} pesos a caja menor'
    escribir_cuentas('gallinas','ingreso' ,valor ,motivo )

def salida_caja_menor(valor):
    motivo = f'Consignacion de {valor} desde la caja menor'
    escribir_cuentas('gallinas','egreso' ,-valor ,motivo )

def abono_credito_gallinas(valor,entidad):
    motivo = f'Abono  de {valor} pesos a {entidad}'
    escribir_cuentas('gallinas','egreso' ,-valor ,motivo )
    escribir_cuentas(entidad,'egreso' ,-valor ,motivo )
    
#-------------------------------------------------------------------------------
def venta_empaques(cantidad ,precio):
    valor = cantidad*precio
    motivo = f'venta de {cantidad} empaques por valor de {valor}'
    escribir_cuentas('gallinas','ingreso',valor,motivo)
    escribir_inventario('empaques','egreso',-cantidad,motivo)

#-------------------------------------------------------------------------------
def ultimas_transacciones():
    df = obtener_cuentas_productos(productos)
    return df.tail(8)

#-------------------------------------------------------------------------------
def cantidad_efectivo_gallinas():
    df = obtener_cuentas_productos(['gallinas']+tipos_huevo)
    efectivo = df['cantidad'].astype(int).sum()
    return efectivo

def cantidad_deuda(entidad):
    df = obtener_cuentas_productos([entidad])
    if (df.shape[0] == 0):
        return 0
    # sacar credito 
    return df[df['producto'] == entidad ]['cantidad'].astype(int).sum()

def cantidad_gallinas():
    df = obtener_inventario_productos(['gallinas'])['cantidad'].sum()
    return int(df)

def cantidad_bultos():
    df = obtener_inventario_productos(['alimento_gallinas'])['cantidad'].sum()
    return int(df)

def cantidad_costales():
    return obtener_inventario_productos(['empaques'])['cantidad'].sum()

def valor_deuda_gallinas(entidad):
    df = obtener_cuentas_productos([entidad])
    if(df.shape[0]==0):
        return 0
    else:
        return df['cantidad'].sum()

def transaccion_gallinas():
    columnas = ['fecha','cantidad','motivo']
    return obtener_cuentas_productos(['gallinas'])[columnas].tail(7)
