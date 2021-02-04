import pandas as pd 

from manejo_huevos import *
from manejo_ventas import *

def inventario():
    produccion_total = obtener_produccion()
    produccion_total_vendida = obtener_venta_huevos()

    inventario = pd.merge(produccion_total,produccion_total_vendida,how='outer', on = 'tipo')

    inventario['unidades'] = inventario['unidades_x']-inventario['unidades_y']
    inventario['cubeta'] = inventario['cubeta_x']-inventario['cubeta_y']
    inventario['sobrantes'] = inventario['sobrantes_x']-inventario['sobrantes_y']

    inventario = inventario[['tipo','unidades','cubeta','sobrantes']]
    return inventario