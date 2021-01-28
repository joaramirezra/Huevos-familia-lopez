from datetime import datetime
import pandas as pd

from manejo_lineas import crear_linea_con_fecha
from manejo_archivos import crear_archivos
from Manejo_alimento import *
from manejo_huevos import *


crear_archivos()
inicializar_inventario()
obtener_inventario()
agregar_al_registro(0,1,'3','2','5')
