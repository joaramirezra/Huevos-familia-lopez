import sys
import pandas as pd
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from logica.logic import *
from logica.manejo_huevos import *
from logica.manejo_ventas import *
from logica.manejo_inventario import *
from logica.manejo_galpon import *
from logica.manejo_compras import *
from logica.manejo_credito import *
from interfaz_grafica.Interfaz_de_usuario import Ui_MainWindow
from logica.gasto_alimento import *
from logica.venta_empaques import *
from logica.manejo_limones import * 
from logica.manejo_cacao import *
from logica.manejo_fletes import *
from logica.manejo_pollos import *
from logica.manejo_ganancias import *
class Hello_world(Ui_MainWindow):
    def __init__( self ):
        super().__init__()
        
    def setupUi( self, MW ):
        super().setupUi( MW )
        self.actualizar_interfaz()
        
        self.boton_agregar_produccion.clicked.connect(self.agregar_produccion_gui)
        self.boton_eliminar_produccion.clicked.connect(self.eliminar_produccion_gui)
        
        self.boton_venta.clicked.connect(self.agregar_venta_gui)
        self.boton_devolucion.clicked.connect(self.devolver_venta_gui)
        
        self.boton_agregar_animales.clicked.connect(self.agregar_animales_gui)
        self.boton_dar_baja_animales.clicked.connect(self.eliminar_animales_gui)
        
        self.boton_comprar_caja_menor.clicked.connect(self.compra_caja_menor_gui)
        self.boton_fiar_caja_menor.clicked.connect(self.credito_caja_menor_gui)
        self.boton_comprar_alimento.clicked.connect(self.comprar_alimento_gui)
        self.boton_fiar_costales.clicked.connect(self.fiar_alimento_gui)
        self.boton_invertir_caja_menor.clicked.connect(self.apoyo_caja_menor_gui )
        self.boton_abonar.clicked.connect(self.abono_gui)
        self.boton_vender_empaques.clicked.connect(self.venta_empaques_gui)       

        self.boton_gastar_alimento.clicked.connect(self.gastar_alimento_gui)
        self.boton_devolver_alimento.clicked.connect(self.devolver_alimento_gui)

        self.boton_venta_limon.clicked.connect(self.agregar_limon)
        self.boton_gasto_limon.clicked.connect(self.sacar_limon)

        self.boton_venta_cacao.clicked.connect(self.agregar_cacao)
        self.boton_gasto_cacao.clicked.connect(self.sacar_cacao)
        
        self.boton_venta_flete.clicked.connect(self.agregar_fletes)
        self.boton_gasto_flete.clicked.connect(self.sacar_fletes)
        
        self.boton_agregar__pollos.clicked.connect(self.agregar_pollos)
        self.boton_dar_baja__pollos.clicked.connect(self.eliminar_pollos)
        self.boton_vender_pollos.clicked.connect(self.vender_pollos)
        self.boton_gastar_pollos.clicked.connect(self.gastos_pollos)
        self.boton_comprar_alimento_4.clicked.connect(self.comprar_alimento_pollos)
        self.boton_gastar_alimento_3.clicked.connect(self.gastar_alimento_pollos_gui)
        self.boton_vender_pollos_2.clicked.connect(self.vender_empaques_pollos)
        self.boton_gastar_pollos_2.clicked.connect(self.reiniciar)
#-------------------------------------------------------------------------------
#------------------------------funciones internas-------------------------------

    def inicizalizar_graficas(self):
        self.graphicsView_2.setBackground('#3c3f58')
        self.graphicsView_3.setBackground('#3c3f58')
        self.graphicsView_4.setBackground('#3c3f58')
        self.graphicsView_5.setBackground('#3c3f58')
        self.graphicsView_6.setBackground('#3c3f58')
        self.graphicsView_7.setBackground('#3c3f58')
        self.compra_alimento_pollos.setBackground('#3c3f58')
        self.gasto_alimento_pollos.setBackground('#3c3f58')
        
        self.graphicsView_2.showGrid(x=True, y=True,alpha=0.2)
        self.graphicsView_3.showGrid(x=True, y=True,alpha=0.2)
        self.graphicsView_4.showGrid(x=True, y=True,alpha=0.2)
        self.graphicsView_5.showGrid(x=True, y=True,alpha=0.2)
        self.graphicsView_6.showGrid(x=True, y=True,alpha=0.2)
        self.graphicsView_7.showGrid(x=True, y=True,alpha=0.2)
        self.compra_alimento_pollos.showGrid(x=True, y=True,alpha=0.2)
        self.gasto_alimento_pollos.showGrid(x=True, y=True,alpha=0.2)
        
        self.graphicsView_2.setLabels(title='Rendimiento historico pollitas', left='PORCENTAJE')
        self.graphicsView_3.setLabels(title='Rendimiento historico gallinas', left='PORCENTAJE')
        self.graphicsView_4.setLabels(title='Alimentacion historica porllitas', left='BULTOS')
        self.graphicsView_5.setLabels(title='Alimentacion historica gallinas', left='BULTOS')
        self.graphicsView_6.setLabels(title='GANANCIAS ACUMULADAS POR SEMANAS', left='MILLONES')
        self.graphicsView_7.setLabels(title='GANANCIAS ACUMULADAS POR MES ', left='MILLONES')
        self.compra_alimento_pollos.setLabels(title='Compra de alimento', left='BULTOS')
        self.gasto_alimento_pollos.setLabels(title='Consumo de alimento', left='BULTOS')
        
#-------------------------------------------------------------------------------
    def limpiar_graficas_rendimiento(self):
        self.graphicsView_2.clear()
        self.graphicsView_3.clear()
        self.graphicsView_4.clear()
        self.graphicsView_5.clear()
        self.graphicsView_6.clear()
        self.graphicsView_7.clear()
        self.compra_alimento_pollos.clear()
        self.gasto_alimento_pollos.clear()

#-------------------------------------------------------------------------------

    def actualizar_interfaz(self):

        self.actualizar_produccion()
        self.inicizalizar_graficas()
        self.actualizar_inventario()
        self.actualizar_numero_animales()
        self.actualizar_rendimiento_diario()
        self.graficar_rendimiento_historico()
        self.actualizar_tabla_caja_menor()
        self.actualizar_saldos()
        self.actualizar_alimento()
        self.graficar_alimentacion()
        self.actualizar_tabla_limon()
        self.actualizar_tabla_caco()
        self.actualizar_tabla_flete()
        self.actualizar_dinero_pollos()
        self.actualizar_tabla_pollo()
        self.actualizar_alimento_mortalidad()
        self.actulizar_alimento_pollos()
        self.actualizar_empaques_pollos()
        self.actualizar_graficas_pollos()
        self.actualizar_ganacias()
    
#-------------------------------------------------------------------------------
#---------------------------------produccion-----------------------------------

    def agregar_produccion_gui(self):
        tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO',
                        'VENCIDO VENTA','DESTRUIDOS']
        
        cubetas = self.cubetas_produccion.text()
        sobrantes = self.sobrantes_produccion.text()
        
        galpon = self.galpon_produccion.currentText()
        galpon =  1 if(galpon == 'GALLINAS') else 0
        
        huevo  = self.tipo_produccion.currentText()
        huevo = tipos_huevo.index(huevo)
       
        if (validar_numeros(cubetas,sobrantes)):
            self.cubetas_produccion.clear()
            self.sobrantes_produccion.clear()
            cubetas , sobrantes = numero_de_cubetas(cubetas,sobrantes)
            unidades = str(numero_de_unidades(cubetas))

            agregar_huevos(galpon,huevo,unidades,str(cubetas),str(sobrantes))
        self.actualizar_interfaz()

    def eliminar_produccion_gui(self):
        tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO',
                        'VENCIDO VENTA','DESTRUIDOS']
        
        cubetas = self.cubetas_produccion.text()
        sobrantes = self.sobrantes_produccion.text()
        
        galpon = self.galpon_produccion.currentText()
        galpon =  1 if(galpon == 'GALLINAS') else 0
        
        huevo  = self.tipo_produccion.currentText()
        huevo = tipos_huevo.index(huevo)
       
        if (validar_numeros(cubetas,sobrantes)):
            self.cubetas_produccion.clear()
            self.sobrantes_produccion.clear()
            cubetas , sobrantes = numero_de_cubetas(cubetas,sobrantes)
            unidades = str(numero_de_unidades(cubetas))
            unidades = '-' + unidades
            cubetas = '-' + str(cubetas )
            sobrantes = '-' +str(sobrantes)
            agregar_huevos(galpon,huevo,unidades,cubetas,sobrantes)
        self.actualizar_interfaz()

    def actualizar_produccion(self):
        data_produccion = obtener_produccion_diaria()

        tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO_VENTA','DESTRUIDOS']
        presentacion = ['cubeta','unidades','sobrantes']
                
        produccion_gallinas = data_produccion[data_produccion['galpon'] == 'POLLITA']

        for j,huevo in enumerate(tipos_huevo):
            produccion_tipo = produccion_gallinas[produccion_gallinas['tipo']==huevo]
            
            elementos = [str(int(produccion_tipo[pres])) for pres in presentacion ]
            for i in range(0,3):
                tiem = self.tabla_produccion_diaria.item(j,i)
                tiem.setText(str(elementos[i]))
        
        suma_vertical = produccion_gallinas[['cubeta','unidades','sobrantes']].sum()
        
        for i in range(0,3):
            tiem = self.tabla_produccion_diaria.item(9,i)
            tiem.setText(str(suma_vertical[i]))
            
        produccion_gallinas = data_produccion[data_produccion['galpon'] == 'GALLINA']
        for j,huevo in enumerate(tipos_huevo):
                produccion_tipo = produccion_gallinas[produccion_gallinas['tipo']==huevo]
                
                elementos = [str(int(produccion_tipo[pres])) for pres in presentacion ]
                for i in range(4,7):
                    tiem = self.tabla_produccion_diaria.item(j,i)
                    tiem.setText(str(elementos[i-4]))
                
        suma_vertical = produccion_gallinas[['cubeta','unidades','sobrantes']].sum()
        
        for i in range(0,3):
            tiem = self.tabla_produccion_diaria.item(9,i+4)
            tiem.setText(str(suma_vertical[i]))
                
        
        data_produccion['total'] = data_produccion['unidades']+data_produccion['sobrantes']
        data_produccion = data_produccion.groupby('tipo').sum().reset_index()
        total_huevos_dia = data_produccion['total'].sum()

        for j,huevo in enumerate(tipos_huevo):
            total_fila = data_produccion[data_produccion['tipo']==huevo]
            tiem = self.tabla_produccion_diaria.item(j,7)
            tiem.setText(str(int(total_fila['total'])))

        tiem = self.tabla_produccion_diaria.item(9,7)
        tiem.setText(str(total_huevos_dia))

# #-------------------------------------------------------------------------------
# #---------------------------------Ventas----------------------------------------

    def agregar_venta_gui(self):
        cantidad = self.cantidad_venta.text()
        precio = self.precio_venta.text()
        observaciones = self.comentario_venta.toPlainText()
        presentacion = self.presentacion_venta.currentText()
        tipo = self.tipo_venta.currentText()

        presentaciones = ['CUBETAS','SOBRANTES']

        tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO',
                        'VENCIDO VENTA','DESTRUIDOS']
        
        presentacion = presentaciones.index(presentacion)
        huevo = tipos_huevo.index(tipo)

        if(validar_numeros(cantidad,precio)):
            total = str(int(precio)*int(cantidad))
            self.cantidad_venta.clear()
            self.precio_venta.clear()
            self.comentario_venta.clear()
             
            if(presentacion == 0):
                unidades = str(int(cantidad)*30)
                agregar_venta(huevo,unidades,cantidad,'0',total,observaciones)
            elif(presentacion == 1):
                agregar_venta(huevo,'0','0',cantidad,total,observaciones)
            # Comentada para cuando venda
            elif(presentacion == 2):
                agregar_venta(huevo,'0','0',cantidad,total,observaciones)
            else :
                pass

            entrada_contabilidad(str(cantidad),str(total))
            registro_caja('venta de huevos : ',str(total))
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def devolver_venta_gui(self):
        cantidad = self.cantidad_venta.text()
        precio = self.precio_venta.text()
        observaciones = self.comentario_venta.toPlainText()
        presentacion = self.presentacion_venta.currentText()
        tipo = self.tipo_venta.currentText()

        presentaciones = ['CUBETAS','SOBRANTES']

        tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO',
                        'VENCIDO VENTA','DESTRUIDOS']
        
        presentacion = presentaciones.index(presentacion)
        huevo = tipos_huevo.index(tipo)

        if(validar_numeros(cantidad,precio)):
            total = str(int(precio)*int(cantidad))
            self.cantidad_venta.clear()
            self.precio_venta.clear()
            self.comentario_venta.clear()
             
            if(presentacion == 0):
                    unidades = str(int(cantidad)*30)
                    agregar_venta(huevo,'-'+unidades,'-'+cantidad,'0','-'+total,observaciones)
            elif(presentacion == 1):
                    agregar_venta(huevo,'0','0', '-'+cantidad,'-'+total,observaciones)
            # Comentada para cuando venda
            elif(presentacion == 2):
                    agregar_venta(huevo,'0','0',cantidad,total,observaciones)

            registro_caja('Devolucion venta','-'+str(total))
            entrada_contabilidad(str(cantidad),'-'+str(total))
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def actualizar_inventario(self):
        produccion_gallinas = inventario()
        ventas = venta_acumulada_dia()
        venta_acumulada_total = venta_acumulada()

        for j,huevo in enumerate(tipos_huevo):
            produccion_tipo = produccion_gallinas[produccion_gallinas['tipo']==huevo]
            venta = ventas[ventas['tipo'] == huevo]
            acumulada = venta_acumulada_total[venta_acumulada_total['tipo'] == huevo]
            cubeta= str(int(produccion_tipo['cubeta']))
            unidades=str(int(produccion_tipo['unidades']))
            sobrantes=str(int(produccion_tipo['sobrantes']))
            venta=str(int(venta['precio']))
            acum = str(int(acumulada['precio']))

            item_unidades = QTableWidgetItem()
            item_unidades.setText(unidades)
            self.tabla_inventario.setItem(j,1,item_unidades)
            
            item_cubeta = QTableWidgetItem()
            item_cubeta.setText(cubeta)
            self.tabla_inventario.setItem(j,0,item_cubeta)
            
            item_sobrantes = QTableWidgetItem()
            item_sobrantes.setText(sobrantes)
            self.tabla_inventario.setItem(j,2,item_sobrantes)
            
            item_venta = QTableWidgetItem()
            item_venta.setText(venta)
            self.tabla_inventario.setItem(j,3,item_venta)
    
            item_acum = QTableWidgetItem()
            item_acum.setText(acum)
            self.tabla_acumulada.setItem(j,0,item_acum)

        cubeta_total,unidades_total,sobrantes_total = produccion_gallinas[['unidades','cubeta','sobrantes']].sum()
        venta_total =str(venta_acumulada_total['precio'].sum()) 
        venta_dia_total = str(ventas['precio'].sum())

        item_venta_acum = QTableWidgetItem()
        item_venta_acum.setText(venta_total)
        self.tabla_acumulada.setItem(9,0,item_venta_acum)
        
        item_cubeta_total = QTableWidgetItem()
        item_cubeta_total.setText(str(cubeta_total))
        self.tabla_inventario.setItem(9,1,item_cubeta_total)

        item_unidades_totales = QTableWidgetItem()
        item_unidades_totales.setText(str(unidades_total))
        self.tabla_inventario.setItem(9,0,item_unidades_totales)

        item_sobrante_sotal = QTableWidgetItem()
        item_sobrante_sotal.setText(str(sobrantes_total))
        self.tabla_inventario.setItem(9,2,item_sobrante_sotal)

        item_venta_dia_total = QTableWidgetItem()
        item_venta_dia_total.setText(str(venta_dia_total))
        self.tabla_inventario.setItem(9,3,item_venta_dia_total)
 
#-------------------------------------------------------------------------------
#---------------------------------Rendimiento-----------------------------------

    def agregar_animales_gui(self):
        galpon = self.galpon_administrar_animales.currentText()
        cantidad = self.cantidad_animales_editar.text()
        if(validar_numeros(cantidad)):
            self.cantidad_animales_editar.clear()
            if(galpon == 'POLLITA'):
                    agregar_animales(str(cantidad),'0')
            elif(galpon == 'GALLINA'):
                    agregar_animales('0',str(cantidad))
        self.actualizar_interfaz()

    def actualizar_numero_animales(self):
        pollitas,gallinas = obtener_animales()
        self.cantidad_pollitas.setText(str(pollitas))
        self.cantidad_gallinas.setText(str(gallinas))
        

#-------------------------------------------------------------------------------
    def eliminar_animales_gui(self):
        galpon = self.galpon_administrar_animales.currentText()
        cantidad = self.cantidad_animales_editar.text()
        if(validar_numeros(cantidad)):
            self.cantidad_animales_editar.clear()
            if(galpon == 'POLLITA'):
                    agregar_animales('-'+str(cantidad),'0')
            elif(galpon == 'GALLINA'):
                    agregar_animales('0','-'+str(cantidad))
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def actualizar_rendimiento_diario(self):
        ren_pollitas,ren_gallinas = obtener_rendimiento_diario()

        ren_gallinas = int(ren_gallinas*100)
        ren_pollitas = int(ren_pollitas*100)

        self.rendimiento_pollitas.setValue(ren_gallinas)
        self.rendimiento_gallinas.setValue(ren_pollitas)

#-------------------------------------------------------------------------------
    def graficar_rendimiento_historico(self): 
        rendimiento_pollitas,rendimiento_gallinas = Rendimiento_acumulado()
        rendimiento_pollitas = rendimiento_pollitas
        self.limpiar_graficas_rendimiento()
        self.graphicsView_2.plot(rendimiento_pollitas,fillLevel=0,brush=("#9fccb8"))
        self.graphicsView_3.plot(rendimiento_gallinas,fillLevel=0,brush=("#9fccb8"))
        
#-------------------------------------------------------------------------------
#---------------------------------CAJA MENOR------------------------------------

    def convertir_a_pesos(self,valor):
        return str(valor)+ ' PESOS'
#-------------------------------------------------------------------------------
    def compra_caja_menor_gui(self):
        cantidad = self.cantidad_dinero_caja.text()
        motivo = self.motivo_gasto.toPlainText().replace('\n','')
        if(validar_numeros(cantidad)):
                self.cantidad_dinero_caja.clear()
                self.motivo_gasto.clear()
                registro_caja('Compra de :'+motivo,'-'+str(cantidad))
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def comprar_alimento_gui(self):
        cantidad = self.cantidad_bultos_adquirir.text()
        precio = self.precio_adquisicion_costal.text()
        if(validar_numeros(cantidad,precio)):
            self.cantidad_bultos_adquirir.clear()
            self.precio_adquisicion_costal.clear()
            ingresar_compra_alimento(cantidad,precio)
            motivo = 'Compra de '+cantidad +' bultos de alimento a :'+ precio + 'pesos'
            total = -1*int(cantidad)*int(precio)
            registro_caja( motivo,str(total))
            entrada_contabilidad(str(cantidad),str(total))

        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def fiar_alimento_gui(self):
        cantidad = self.cantidad_bultos_adquirir.text()
        precio = self.precio_adquisicion_costal.text()
        if(validar_numeros(cantidad,precio)):
            self.cantidad_bultos_adquirir.clear()
            self.precio_adquisicion_costal.clear()
            motivo = 'Credito de '+cantidad +' bultos de alimento a :'+ precio + 'pesos'
            total = int(cantidad)*int(precio)
            
            ingresar_fiado(motivo,str(total),'1',str(cantidad))
            entrada_contabilidad(str(cantidad),'-'+str(total))
        self.actualizar_interfaz()

#------------------------------------------------------------------------------- 
    def apoyo_caja_menor_gui(self):
        cantidad = self.ingresar_dinero.text()
        if(validar_numeros(cantidad)):
            self.ingresar_dinero.clear()
            motivo = 'Ingreso desde la caja mayor '+cantidad + 'pesos'
            registro_caja( motivo,cantidad)
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def abono_gui(self):
        cantidad = self.abonar_dinero.text()
        if(validar_numeros(cantidad)):
            self.abonar_dinero.clear()
            motivo = 'Abono a agropaisa : '+cantidad + 'pesos'
            registro_caja( motivo,'-'+cantidad)
            ingresar_fiado('abono','-'+str(cantidad),'0','0')
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def credito_caja_menor_gui(self):
        cantidad = self.cantidad_dinero_caja.text()
        motivo = self.motivo_gasto.toPlainText().replace('\n','')
        if(validar_numeros(cantidad)):
                self.cantidad_dinero_caja.clear()
                self.motivo_gasto.clear()
                motivo = 'Credito' + motivo
                ingresar_fiado(motivo,str(cantidad),'0','0')
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def actualizar_tabla_caja_menor(self):
        registros_credito = obtener_registro_credito()
        registros_credito = registros_credito[['fecha','motivo','precio']].tail(4)
        
        registro_compra = obtener_registro_compras()
        registro_compra = registro_compra[['fecha','motivo','precio']].tail(4)
        
        registro_caja = obtener_registro_caja_mayor()
        registro_caja.rename(columns = {'cantidad_dinero':'precio'},inplace=True)
        
        registros= pd.concat([registros_credito,registro_caja,registro_compra])
        registros['fecha'] = pd.to_datetime(registros['fecha'])
        registros = registros.tail(10)

        for i,registro in enumerate(registros['fecha']):
            item_venta_acum = QTableWidgetItem()
            item_venta_acum.setText("".join(str(registro).split(' ')[0]))
            self.tabla_caja_menor.setItem(i,0,item_venta_acum)
            
        for i,registro in enumerate(registros['motivo']):
            item_venta_acum = QTableWidgetItem()
            item_venta_acum.setText(str(registro))
            self.tabla_caja_menor.setItem(i,1,item_venta_acum)
            
        for i,registro in enumerate(registros['precio']):
            item_venta_acum = QTableWidgetItem()
            item_venta_acum.setText(str(registro))
            self.tabla_caja_menor.setItem(i,2,item_venta_acum)
            
#-------------------------------------------------------------------------------
    def actualizar_saldos(self):
        efectivo = self.convertir_a_pesos(int(Cantidad_efectivo()))
        deuda = self.convertir_a_pesos(int(obtener_total_credito()))
        saldo = self.convertir_a_pesos(15000000 - int(obtener_total_credito()))

        self.cantidad_efectivo.setText(efectivo)
        self.cantidad_deuda.setText(deuda)
        self.cantidad_cupo.setText(saldo)

    def venta_empaques_gui(self):
        cantidad = self.cantidad_empaques_venta.text()  
        precio = self.precio_empaque_venta.text()
        if(validar_numeros(cantidad,precio)):
            self.cantidad_empaques_venta.clear()
            self.precio_empaque_venta.clear()
            motivo = 'venta empaques'
            total = int(cantidad)*int(precio)
            registro_caja(motivo,str(total))
            venta_empaques(str(cantidad),str(total))
        self.actualizar_interfaz()

# #-------------------------------------------------------------------------------
# #--------------------------------------alimento---------------------------------
    def gastar_alimento_gui(self):
        galpon = self.galpon_alimentado.currentText()  
        cantidad = self.cantidad_alimento_dado.text()
        if(validar_numeros(cantidad)):
            self.cantidad_alimento_dado.clear()
            consumo_de_alimento(galpon,cantidad)
        self.actualizar_interfaz()

    def devolver_alimento_gui(self):
        galpon = self.galpon_alimentado.currentText()  
        cantidad = self.cantidad_alimento_dado.text()
        if(validar_numeros(cantidad)):
            self.cantidad_alimento_dado.clear()
            consumo_de_alimento(galpon,'-'+cantidad)
        self.actualizar_interfaz()


    def actualizar_alimento(self):
        bultos = obtener_cantidad_bultos()
        costales = cantidad_de_empaques()
        self.Empaques_gallinas_dis.setText(str(costales))
        self.bultos_gallinas_dis.setText(str(bultos))

    def graficar_alimentacion(self):
        historico_alimentacion = obtener_cantidad_bultos_gastados_historico()
        
        historico_gallinas = historico_alimentacion[historico_alimentacion['galpon'] == 'GALLINA']
        historico_pollitas = historico_alimentacion[historico_alimentacion['galpon'] == 'POLLITA']
        
        ren_gallinas = historico_gallinas['cantidad']
        ren_polliras = historico_pollitas['cantidad']
        
        self.limpiar_graficas_rendimiento()
        self.graphicsView_4.plot(list(ren_polliras),fillLevel=0,brush=("#9fccb8"))
        self.graphicsView_5.plot(list(ren_gallinas),fillLevel=0,brush=("#9fccb8")) 
        
    
#-------------------------------------------------------------------------------
#------------------------------------Limones -----------------------------------

    def agregar_limon(self):
        cantidad = self.cantidad_limones_venta.text()
        precio =self.valor_venta_limon.text()
        motivo = self.observacion_limon.toPlainText()
        
        if(validar_numeros(cantidad,precio)):
            self.cantidad_limones_venta.clear()
            self.valor_venta_limon.clear()
            self.observacion_limon.clear()
            motivo = 'venta de : '+str(cantidad) +' Canastillas'
            total = int(cantidad)*int(precio)
            agregar_venta_limon(motivo,str(cantidad),str(total))
        self.actualizar_interfaz()


    def sacar_limon(self):
        cantidad = self.cantidad_gasto_limon.text()
        motivo = self.concepto_gasto_limon.text()
        if(validar_numeros(cantidad)):
            self.cantidad_gasto_limon.clear()
            self.concepto_gasto_limon.clear()
            motivo =  motivo
            total = -1*int(cantidad)
            agregar_venta_limon(motivo,str(cantidad),str(total))
        
        self.actualizar_interfaz()

    
    def actualizar_tabla_limon(self):
        df = registro_limones()
        df['precio'] = pd.to_numeric(df['precio'] )
        
        ingresos = df[df['precio']>0]
        ingresos = int(ingresos['precio'].sum())
        
        egresos = df[df['precio']<0]
        egresos = int(egresos['precio'].sum())
        
        saldo = ingresos + egresos
        
        self.valor_ingreso_limon.setText(str(ingresos)+ ' PESOS')
        self.valor_egreso_limon.setText(str(egresos)+ ' PESOS')
        self.valor_saldo_limon.setText(str(saldo)+ ' PESOS')
        
        if(df.shape[0]>14):
            df = df.tail(14).reset_index()
      
        for i,row in df.iterrows():
            celda = self.tabla_caja_menor_2.item(i,0)
            celda.setText(str(row['fecha']))
            
            celda = self.tabla_caja_menor_2.item(i,1)
            celda.setText(str(row['motivo']))
            
            celda = self.tabla_caja_menor_2.item(i,2)
            celda.setText(str(row['precio']))

# #-------------------------------------------------------------------------------
# #------------------------------------Cacao -----------------------------------
    def agregar_cacao(self):
        cantidad = self.cantidad_cacao_venta.text()
        precio =self.valor_venta_cacao.text()
        motivo = self.observacion_cacao.toPlainText()

        if(validar_numeros(cantidad,precio)):
            self.cantidad_cacao_venta.clear()
            self.valor_venta_cacao.clear()
            self.observacion_cacao.clear()
            motivo = 'venta de : ' +str(cantidad) +' kilos'
            total = int(cantidad)*int(precio)
            agregar_venta_cacao(motivo,str(cantidad),str(total))
        self.actualizar_interfaz()


    def sacar_cacao(self):
        cantidad = self.cantidad_gasto_cacao.text()
        motivo = self.concepto_gasto_cacao.text()
        if(validar_numeros(cantidad)):
            self.cantidad_gasto_cacao.clear()
            self.concepto_gasto_cacao.clear()
            motivo =  motivo
            total = -1*int(cantidad)
            agregar_venta_cacao(motivo,str(cantidad),str(total))
        
        self.actualizar_interfaz()

    
    def actualizar_tabla_caco(self):
        df = registro_cacao()
        df['precio'] = pd.to_numeric(df['precio'] )
        
        ingresos = df[df['precio']>0]
        ingresos = int(ingresos['precio'].sum())

        egresos = df[df['precio']<0]
        egresos = int(egresos['precio'].sum())
        
        saldo = ingresos + egresos

        self.valor_ingreso_cacao.setText(str(ingresos)+ ' PESOS')
        self.valor_egreso_cacao.setText(str(egresos)+ ' PESOS')
        self.valor_saldo_cacao.setText(str(saldo)+ ' PESOS')

        if(df.shape[0]>14):
            df = df.tail(14).reset_index()
      
        for i,row in df.iterrows():
            celda = self.tabla_caja_menor_3.item(i,0)
            celda.setText(str(row['fecha']))
            
            celda = self.tabla_caja_menor_3.item(i,1)
            celda.setText(str(row['motivo']))
            
            celda = self.tabla_caja_menor_3.item(i,2)
            celda.setText(str(row['precio']))

    

# #-------------------------------------------------------------------------------
# #--------------------------------------fletes-----------------------------------
    def agregar_fletes(self):
        cantidad = self.cantidad_flete_venta_5.text()
        precio =self.valor_venta_flete.text()
        motivo = self.observacion_flete.toPlainText()
        
        if(validar_numeros(cantidad,precio)):
            self.cantidad_flete_venta_5.clear()
            self.valor_venta_flete.clear()
            self.observacion_flete.clear()
            motivo = 'se realizaron  : ' +str(cantidad) +' fletes'
            total = int(cantidad)*int(precio)
            agregar_venta_fletes(motivo,str(cantidad),str(total))
        
        self.actualizar_interfaz()


    def sacar_fletes(self):
        
        cantidad = self.cantidad_gasto_flete.text()
        motivo = self.concepto_gasto_flete.text()
        if(validar_numeros(cantidad)):
            self.cantidad_gasto_flete.clear()
            self.concepto_gasto_flete.clear()
            motivo =  motivo
            total = -1*int(cantidad)
            agregar_venta_fletes(motivo,str(cantidad),str(total))
        
        self.actualizar_interfaz()

    
    def actualizar_tabla_flete(self):
        df = registro_fletes()
        df['precio'] = pd.to_numeric(df['precio'] )
        
        ingresos = df[df['precio']>0]
        ingresos = int(ingresos['precio'].sum())
        
        egresos = df[df['precio']<0]
        egresos = int(egresos['precio'].sum())
        
        saldo = ingresos + egresos
        
        self.valor_ingreso_flete.setText(str(ingresos)+ ' PESOS')
        self.valor_egreso_flete.setText(str(egresos)+ ' PESOS')
        self.valor_saldo_flete.setText(str(saldo)+ ' PESOS')

        if(df.shape[0]>14):
            df = df.tail(14).reset_index()
      
        for i,row in df.iterrows():
            celda = self.tabla_caja_menor_4.item(i,0)
            celda.setText(str(row['fecha']))
            
            celda = self.tabla_caja_menor_4.item(i,1)
            celda.setText(str(row['motivo']))
            
            celda = self.tabla_caja_menor_4.item(i,2)
            celda.setText(str(row['precio']))

# #-------------------------------------------------------------------------------
# #-----------------------------------pollos-------------------------------------

    def agregar_pollos(self):
        cantidad = self.cantidad__pollos.text()
        precio =self.precio_pollos.text()
        
        if(validar_numeros(cantidad,precio)):
            self.cantidad__pollos.clear()
            self.precio_pollos.clear()
            motivo = 'Compra pollitos' 
            total = -1*int(precio)*int(cantidad)
            agregar_venta_pollos(motivo,str(cantidad),str(total),'0')
        
        self.actualizar_interfaz()

    def eliminar_pollos(self):
        cantidad = self.cantidad__pollos_2.text()
        if(validar_numeros(cantidad)):
            self.cantidad__pollos_2.clear()
            self.precio_pollos.clear()
            motivo = 'Dar de baja pollitos' 
            agregar_venta_pollos(motivo,'-'+str(cantidad),'0','0')
        self.actualizar_interfaz()

    def vender_pollos(self):
        cantidad = self.cantidad_kilos__pollos.text()
        precio = self.precio_kilo_pollos.text()

        if(validar_numeros(cantidad,precio)):
            self.cantidad_kilos__pollos.clear()
            self.precio_kilo_pollos.clear()
            
            motivo = 'venta de : '+ str(cantidad) +' Kilos de pollo' 
            total = int(precio)*int(cantidad)
            agregar_venta_pollos(motivo,str(cantidad),str(total),'1')
    
        self.actualizar_interfaz()


    def gastos_pollos(self):
    
        cantidad = self.cantidad_gastado_pollos.text()
        motivo = self.concepto_compra_pollos.text()

        if(validar_numeros(cantidad)):
            self.cantidad_gastado_pollos.clear()
            self.concepto_compra_pollos.clear()
            
            motivo = 'gasto pollo : '+ motivo 
            total = -1*int(cantidad)
            agregar_venta_pollos(motivo,str(0),str(total),'1')
        self.actualizar_interfaz()
    
    def actualizar_dinero_pollos (self):
        ingresos,egresos,saldo = valores_pollos()

        self.valor_ingreso_pollos.setText(str(ingresos)+ ' PESOS')
        self.valor_egreso__pollos.setText(str(egresos)+ ' PESOS')
        self.valor_saldo__pollos.setText(str(saldo)+ ' PESOS')
   
    def actualizar_alimento_mortalidad(self):
        df = registro_pollos()
        df = df[df['tipo']== 0]
        
        if(df.shape[0]<1):
            cantidad_pollos_comprados = 0
            cantidad_pollos_muertos = 0
            cantidad_pollos_vivos = 0
            mortalidad = 0
        else :
            cantidad_pollos_comprados = df[df['cantidad']>0] 
            cantidad_pollos_comprados = int(cantidad_pollos_comprados['cantidad'].sum())
        
            cantidad_pollos_muertos = df[df['cantidad']<0]
            cantidad_pollos_muertos = int(cantidad_pollos_muertos['cantidad'].sum())

            cantidad_pollos_vivos = cantidad_pollos_comprados+cantidad_pollos_muertos
            
            if(cantidad_pollos_comprados == 0):
                mortalidad = 0
            
            else :
                mortalidad = -cantidad_pollos_muertos/cantidad_pollos_comprados

            mortalidad = round(mortalidad*100,3)
        
        self.cantidad_pollos_galpon.setText(str(cantidad_pollos_vivos))
        self.indice_mortalidad_pollos.setText(str(mortalidad)+' % ')
        
    def actualizar_tabla_pollo(self):
        df = registro_pollos()

        for i in range(0,7):
            celda = self.tabla_pollos.item(i,0)
            celda.setText(' ')
            celda = self.tabla_pollos.item(i,1)
            celda.setText(' ')
            celda = self.tabla_pollos.item(i,2)
            celda.setText(' ')

        if(df.shape[0]>7):
            df = df.tail(7).reset_index()

        for i,row in df.iterrows():
            celda = self.tabla_pollos.item(i,0)
            celda.setText(str(row['fecha']))
            
            celda = self.tabla_pollos.item(i,1)
            celda.setText(str(row['motivo']))
            
            celda = self.tabla_pollos.item(i,2)
            celda.setText(str(row['precio']))

#-------------------------------------------------------------------------------
#--------------------------CONSUMO ALIMENTO POLLOS------------------------------

    def comprar_alimento_pollos(self):
        cantidad = self.cantidad_bultos_adquirir_4.text()
        precio = self.precio_adquisicion_costal_4.text()

        if(validar_numeros(cantidad,precio)):
            self.cantidad_bultos_adquirir_4.clear()
            self.precio_adquisicion_costal_4.clear()
            
            motivo = 'Compra de : '+ str(cantidad) +' bultos de alimento' 
            total = -1*int(precio)*int(cantidad)
            agregar_venta_pollos(motivo,str(cantidad),str(total),'2')
    
        self.actualizar_interfaz()

    def gastar_alimento_pollos_gui(self):
        cantidad = self.cantidad_alimento_dado_3.text()
        
        if(validar_numeros(cantidad)):
            self.cantidad_alimento_dado_3.clear()
            
            motivo = 'gasto de : '+ str(cantidad) +' bultos de alimento' 
            total = 0
            agregar_venta_pollos(motivo,'-'+str(cantidad),str(total),'2')
    
        self.actualizar_interfaz()

    def actulizar_alimento_pollos(self):
        df = registro_pollos()
        df = df[df['tipo']== 2]
       
        ingresos = df[df['cantidad']>0]
        ingresos = int(ingresos['cantidad'].sum())
        
        egresos = df[df['cantidad']<0]
        egresos = int(egresos['cantidad'].sum())

        total = ingresos +egresos
        self.cantidad_cupo_30.setText(str(total))        

    def  vender_empaques_pollos(self):
        cantidad = self.cantidad_kilos__pollos_2.text()
        precio = self.precio_kilo_pollos_2.text()
       
        if(validar_numeros(cantidad,precio)):
            self.cantidad_kilos__pollos_2.clear()
            self.precio_kilo_pollos_2.clear()
            
            motivo = 'venta de : '+ str(cantidad) +' empaques' 
            total = int(precio)*int(cantidad)
            agregar_venta_pollos(motivo,str(cantidad),str(total),'3')

        self.actualizar_interfaz()

    def actualizar_empaques_pollos(self):
        df = registro_pollos()
        df = df[df['tipo']== 2]
       
        egresos = df[df['cantidad']<0]
        egresos = int(egresos['cantidad'].sum())

        vendidos = registro_pollos().copy()
        vendidos = vendidos[vendidos['tipo']== 3]

        ventas = vendidos[vendidos['cantidad']>0]
        ventas = int(ventas['cantidad'].sum())
        
        total = -1*(egresos + ventas)

        self.cantidad_cupo_24.setText(str(total))        


    def actualizar_graficas_pollos(self):
        df = registro_pollos()
        df = df[df['tipo']== 2]
       
        egresos = df[df['cantidad']<0]
        egresos = egresos.groupby('fecha').sum().reset_index()
        egresos = -1*egresos['cantidad']

        ingresos = df[df['cantidad']>0]
        ingresos = ingresos.groupby('fecha').sum().reset_index()
        ingresos = ingresos['cantidad']

        self.limpiar_graficas_rendimiento()
        self.compra_alimento_pollos.plot(ingresos,fillLevel=0,brush=("#9fccb8"))
        self.gasto_alimento_pollos.plot(egresos,fillLevel=0,brush=("#9fccb8"))
        
    def actualizar_ganacias(self):
        self.limpiar_graficas_rendimiento()
        df = calular_ganancia_semanal()
        
        ultimos = df['precio']
        ultimo = df.tail(1)

        self.cantidad_cupo_15.setText(str(int(ultimo['precio']))+'\nPESOS')
        self.graphicsView_6.plot(ultimos,fillLevel=0,brush=("#9fccb8"))
        
        df = calular_ganancia_mensual()
        ultimos = df['precio']
        ultimo = df.tail(1)
        self.cantidad_cupo_16.setText(str(int(ultimo['precio']))+'\nPESOS')
        self.graphicsView_7.plot(ultimos,fillLevel=0,brush=("#9fccb8"))
    
    def reiniciar(self ):
        reiniciar_produccion()
        self.actualizar_interfaz()

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Hello_world()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

main()


