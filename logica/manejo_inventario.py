import sys
sys.path.append(".")
import pandas as pd

import pandas as pd 

from .manejo_huevos import obtener_produccion
from .manejo_ventas import obtener_venta_huevos

def inventario():
    produccion_total = obtener_produccion()
    produccion_total_vendida = obtener_venta_huevos()

    inventario = pd.merge(produccion_total,produccion_total_vendida,how='outer', on = 'tipo')

    inventario['unidades'] = inventario['unidades_x']-inventario['unidades_y']
    inventario['cubeta'] = inventario['cubeta_x']-inventario['cubeta_y']
    inventario['sobrantes'] = inventario['sobrantes_x']-inventario['sobrantes_y']
    
    inventario['cubeta'] += inventario['sobrantes']//30
    inventario['unidades'] = inventario['cubeta']*30
    inventario['sobrantes'] = inventario['sobrantes']%30 
    inventario = inventario[['tipo','unidades','cubeta','sobrantes']]
    return inventario