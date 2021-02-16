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
        self.boton_comprar_alimento.clicked.connect(self.comprar_alimento_gui)
        self.boton_invertir_caja_menor.clicked.connect(self.apoyo_caja_menor_gui )
        self.boton_abonar.clicked.connect(self.abono_gui)
        self.boton_fiar_caja_menor.clicked.connect(self.credito_caja_menor_gui)
        self.boton_fiar_costales.clicked.connect(self.fiar_alimento_gui)
        self.boton_gastar_alimento.clicked.connect(self.gastar_alimento_gui)
        self.boton_vender_empaques.clicked.connect(self.venta_empaques_gui)       
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

    def inicizalizar_graficas(self):
        self.graphicsView_2.setBackground('#3c3f58')
        self.graphicsView_3.setBackground('#3c3f58')
        self.graphicsView_4.setBackground('#3c3f58')
        self.graphicsView_5.setBackground('#3c3f58')

        self.graphicsView_2.showGrid(x=True, y=True,alpha=0.2)
        self.graphicsView_3.showGrid(x=True, y=True,alpha=0.2)
        self.graphicsView_4.showGrid(x=True, y=True,alpha=0.2)
        self.graphicsView_5.showGrid(x=True, y=True,alpha=0.2)
        
        self.graphicsView_2.setLabels(title='Rendimiento historico pollitas', left='PORCENTAJE')
        self.graphicsView_3.setLabels(title='Rendimiento historico gallinas', left='PORCENTAJE')
        self.graphicsView_4.setLabels(title='Alimentacion historica porllitas', left='BULTOS')
        self.graphicsView_5.setLabels(title='Alimentacion historica gallinas', left='BULTOS')

    def limpiar_graficas_rendimiento(self):
        self.graphicsView_2.clear()
        self.graphicsView_3.clear()
        self.graphicsView_4.clear()
        self.graphicsView_5.clear()

    def actualizar_interfaz(self):
        self.actualizar_produccion()
        self.actualizar_inventario()
        self.actualizar_rendimiento()
        self.inicizalizar_graficas()
        self.actualizar_saldos()
        self.actualizar_alimento()
        self.graficar_alimentacion()
        self.actualizar_tabla_limon()
        self.actualizar_tabla_caco()
        self.actualizar_tabla_flete()
        self.actualizar_dinero_pollos()
        self.actualizar_tabla_pollo()
    
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

        produccion_gallinas = data_produccion[data_produccion['galpon'] == 'POLLITA']
        for j,huevo in enumerate(tipos_huevo):
                produccion_tipo = produccion_gallinas[produccion_gallinas['tipo']==huevo]
                cubeta= str(int(produccion_tipo['cubeta']))
                unidades=str(int(produccion_tipo['unidades']))
                sobrantes=str(int(produccion_tipo['sobrantes']))
                item_cubeta = QTableWidgetItem()
                item_cubeta.setText(cubeta)
                self.tabla_produccion_diaria.setItem(j,0,item_cubeta)
                
                item_unidades = QTableWidgetItem()
                item_unidades.setText(unidades)
                self.tabla_produccion_diaria.setItem(j,1,item_unidades)
                
                item_sobrantes = QTableWidgetItem()
                item_sobrantes.setText(sobrantes)
                self.tabla_produccion_diaria.setItem(j,2,item_sobrantes)

        sum_unidades,sum_cubeta,sum_sobrantes = produccion_gallinas[['unidades','cubeta','sobrantes']].sum()
        
        total_sobrantes = QTableWidgetItem()
        total_sobrantes.setText(str(sum_sobrantes))
        self.tabla_produccion_diaria.setItem(9,2,total_sobrantes)
        
        total_cubeta = QTableWidgetItem()
        total_cubeta.setText(str(sum_cubeta))
        self.tabla_produccion_diaria.setItem(9,0,total_cubeta)
        
        total_unidades = QTableWidgetItem()
        total_unidades.setText(str(sum_unidades))
        self.tabla_produccion_diaria.setItem(9,1,total_unidades)

        produccion_gallinas = data_produccion[data_produccion['galpon'] == 'GALLINA']
        for j,huevo in enumerate(tipos_huevo):
                produccion_tipo = produccion_gallinas[produccion_gallinas['tipo']==huevo]
                cubeta= str(int(produccion_tipo['cubeta']))
                unidades=str(int(produccion_tipo['unidades']))
                sobrantes=str(int(produccion_tipo['sobrantes']))
                item_cubeta = QTableWidgetItem()
                item_cubeta.setText(cubeta)
                self.tabla_produccion_diaria.setItem(j,4,item_cubeta)
                
                item_unidades = QTableWidgetItem()
                item_unidades.setText(unidades)
                self.tabla_produccion_diaria.setItem(j,5,item_unidades)
                
                item_sobrantes = QTableWidgetItem()
                item_sobrantes.setText(sobrantes)
                self.tabla_produccion_diaria.setItem(j,6,item_sobrantes)
        
        sum_unidades,sum_cubeta,sum_sobrantes = produccion_gallinas[['unidades','cubeta','sobrantes']].sum()
        
        total_sobrantes = QTableWidgetItem()
        total_sobrantes.setText(str(sum_sobrantes))
        self.tabla_produccion_diaria.setItem(9,6,total_sobrantes)
        
        total_cubeta = QTableWidgetItem()
        total_cubeta.setText(str(sum_cubeta))
        self.tabla_produccion_diaria.setItem(9,4,total_cubeta)
        
        total_unidades = QTableWidgetItem()
        total_unidades.setText(str(sum_unidades))
        self.tabla_produccion_diaria.setItem(9,5,total_unidades)

        total_diario_huevos =  total_diario()
        total_diario_huevos['total'] = total_diario_huevos['unidades']+total_diario_huevos['sobrantes']
        print(total_diario_huevos)

    

#-------------------------------------------------------------------------------
#---------------------------------Ventas----------------------------------------

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
	        
            registro_caja('venta',str(total))
        self.actualizar_interfaz()

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
        self.actualizar_interfaz()

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

    
    def actualizar_rendimiento(self):
        pollitas,gallinas= obtener_animales()
        ren_pollitas,ren_gallinas = obtener_rendimiento_diario()
        self.cantidad_pollitas.setText(str(pollitas))
        self.cantidad_gallinas.setText(str(gallinas))
        ren_gallinas = int(ren_gallinas)*100
        ren_pollitas = int(ren_pollitas)*100
        self.rendimiento_pollitas.setValue(ren_gallinas)
        self.rendimiento_gallinas.setValue(ren_pollitas)
        self.graficar_rendimiento()
        
    def graficar_rendimiento(self): 
        rendimiento_pollitas,rendimiento_gallinas = Rendimiento_acumulado()
        self.limpiar_graficas_rendimiento()
        self.graphicsView_2.plot(rendimiento_pollitas,fillLevel=0,brush=("#9fccb8"))
        self.graphicsView_3.plot(rendimiento_gallinas,fillLevel=0,brush=("#9fccb8"))
        
#-------------------------------------------------------------------------------
#---------------------------------CAJA MENOR------------------------------------

    def convertir_a_pesos(self,valor):
        return str(valor)+ ' PESOS'

    def compra_caja_menor_gui(self):
        cantidad = self.cantidad_dinero_caja.text()
        motivo = self.motivo_gasto.toPlainText().replace('\n','')
        if(validar_numeros(cantidad)):
                self.cantidad_dinero_caja.clear()
                self.motivo_gasto.clear()
                registro_caja('Compra de :'+motivo,'-'+str(cantidad))
        self.actualizar_interfaz()


    def comprar_alimento_gui(self):
        cantidad = self.cantidad_bultos_adquirir.text()
        precio = self.precio_adquisicion_costal.text()
        if(validar_numeros(cantidad,precio)):
            self.cantidad_bultos_adquirir.clear()
            self.precio_adquisicion_costal.clear()
            ingresar_compra_alimento(cantidad,precio)
            motivo = 'Compra de '+cantidad +' bultos de alimento a :'+ precio + 'pesos'
            total = int(cantidad)*int(precio)
            registro_caja( motivo,'-'+str(total))
        self.actualizar_interfaz()

    def fiar_alimento_gui(self):
        cantidad = self.cantidad_bultos_adquirir.text()
        precio = self.precio_adquisicion_costal.text()
        if(validar_numeros(cantidad,precio)):
            self.cantidad_bultos_adquirir.clear()
            self.precio_adquisicion_costal.clear()
            motivo = 'Credito de '+cantidad +' bultos de alimento a :'+ precio + 'pesos'
            total = int(cantidad)*int(precio)
            ingresar_fiado(motivo,str(total),'1',str(cantidad))
            ( motivo,'-'+str(total))
        self.actualizar_interfaz()

    
    def apoyo_caja_menor_gui(self):
        cantidad = self.ingresar_dinero.text()
        if(validar_numeros(cantidad)):
            self.ingresar_dinero.clear()
            motivo = 'Ingreso desde la caja mayor '+cantidad + 'pesos'
            registro_caja( motivo,cantidad)
        self.actualizar_interfaz()

    def abono_gui(self):
        cantidad = self.abonar_dinero.text()
        if(validar_numeros(cantidad)):
            self.abonar_dinero.clear()
            motivo = 'Abono a agropaisa : '+cantidad + 'pesos'
            registro_caja( motivo,'-'+cantidad)
            ingresar_fiado('abono','-'+str(cantidad),'0','0')
        self.actualizar_interfaz()


    def credito_caja_menor_gui(self):
        cantidad = self.cantidad_dinero_caja.text()
        motivo = self.motivo_gasto.toPlainText().replace('\n','')
        if(validar_numeros(cantidad)):
                self.cantidad_dinero_caja.clear()
                self.motivo_gasto.clear()
                motivo = 'Credito' + motivo
                ingresar_fiado(motivo,str(cantidad),'0','0')
        self.actualizar_interfaz()

    def actualizar_tabla(self):
        registros_credito = obtener_registro_credito()
        registro_compra = obtener_registro_compras()
        registros_credito=registros_credito[['fecha','motivo','precio']].tail(4)
        registro_compra = registro_compra[['fecha','motivo','precio']].tail(4)
        registro_caja =obtener_registro_caja_mayor()
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
            

    def actualizar_saldos(self):
        efectivo = self.convertir_a_pesos(int(Cantidad_efectivo()))
        deuda = self.convertir_a_pesos(int(obtener_total_credito()))
        saldo = str(15000000 - int(obtener_total_credito()))
        self.cantidad_efectivo.setText(efectivo)
        self.cantidad_deuda.setText(deuda)
        self.cantidad_cupo.setText(saldo)
        self.actualizar_tabla()
        
#-------------------------------------------------------------------------------
#--------------------------------------alimento---------------------------------
    def actualizar_alimento(self):
        bultos = obtener_cantidad_bultos()
        costales = cantidad_de_empaques()
        
        item_bultos = QTableWidgetItem()
        item_bultos.setText(str(bultos))
        self.tabla_inventario_alimento.setItem(0,0,item_bultos)
        
        item_empaques = QTableWidgetItem()
        item_empaques.setText(str(costales))
        self.tabla_inventario_alimento.setItem(0,1,item_empaques)          

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

    def graficar_alimentacion(self):
        historico_alimentacion = obtener_cantidad_bultos_gastados_historico()
        historico_gallinas = historico_alimentacion[historico_alimentacion['galpon'] == 'GALLINA']
        historico_pollitas = historico_alimentacion[historico_alimentacion['galpon'] == 'POLLITA']
        ren_gallinas = historico_gallinas['cantidad']
        ren_polliras = historico_pollitas['cantidad']
        self.limpiar_graficas_rendimiento()
        self.graphicsView_5.plot(list(ren_gallinas),fillLevel=0,brush=("#9fccb8"))
        self.graphicsView_4.plot(list(ren_polliras),fillLevel=0,brush=("#9fccb8"))
       
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
            motivo = 'venta '+ motivo
            total = int(cantidad)*int(precio)
            agregar_venta_limon(motivo,str(total))
        
        self.actualizar_interfaz()


    def sacar_limon(self):
        cantidad = self.cantidad_gasto_limon.text()
        motivo = self.concepto_gasto_limon.text()
        if(validar_numeros(cantidad)):
            self.cantidad_gasto_limon.clear()
            self.concepto_gasto_limon.clear()
            motivo =  motivo
            total = -1*int(cantidad)
            agregar_venta_limon(motivo,str(total))
        
        self.actualizar_interfaz()

    
    def actualizar_tabla_limon(self):
        df = registro_limones()
        ingresos = df[df['precio']>0]
        ingresos = int(ingresos['precio'].sum())
        egresos = df[df['precio']<0]
        egresos = int(egresos['precio'].sum())
        
        saldo = ingresos + egresos
        self.valor_ingreso_limon.setText(str(ingresos))
        self.valor_egreso_limon.setText(str(egresos))
        self.valor_saldo_limon.setText(str(saldo))
    

#-------------------------------------------------------------------------------
#------------------------------------Limones -----------------------------------

    def agregar_cacao(self):
        cantidad = self.cantidad_cacao_venta.text()
        precio =self.valor_venta_cacao.text()
        motivo = self.observacion_cacao.toPlainText()
        if(validar_numeros(cantidad,precio)):
            self.cantidad_cacao_venta.clear()
            self.valor_venta_cacao.clear()
            self.observacion_cacao.clear()
            motivo = 'venta '+ motivo
            total = int(cantidad)*int(precio)
            agregar_venta_cacao(motivo,str(total))
        
        self.actualizar_interfaz()


    def sacar_cacao(self):
        
        cantidad = self.cantidad_gasto_cacao.text()
        motivo = self.concepto_gasto_cacao.text()
        if(validar_numeros(cantidad)):
            self.cantidad_gasto_cacao.clear()
            self.concepto_gasto_cacao.clear()
            motivo =  motivo
            total = -1*int(cantidad)
            agregar_venta_cacao(motivo,str(total))
        
        self.actualizar_interfaz()

    
    def actualizar_tabla_caco(self):
        df = registro_cacao()
        ingresos = df[df['precio']>0]
        ingresos = int(ingresos['precio'].sum())
        egresos = df[df['precio']<0]
        egresos = int(egresos['precio'].sum())
        
        saldo = ingresos + egresos
        self.valor_ingreso_cacao.setText(str(ingresos))
        self.valor_egreso_cacao.setText(str(egresos))
        self.valor_saldo_cacao.setText(str(saldo))
    

#-------------------------------------------------------------------------------
#--------------------------------------fletes-----------------------------------

    def agregar_fletes(self):
        cantidad = self.cantidad_flete_venta_5.text()
        precio =self.valor_venta_flete.text()
        motivo = self.observacion_flete.toPlainText()
        if(validar_numeros(cantidad,precio)):
            self.cantidad_flete_venta_5.clear()
            self.valor_venta_flete.clear()
            self.observacion_flete.clear()
            motivo = 'venta '+ motivo
            total = int(cantidad)*int(precio)
            agregar_venta_fletes(motivo,str(total))
        
        self.actualizar_interfaz()


    def sacar_fletes(self):
        
        cantidad = self.cantidad_gasto_flete.text()
        motivo = self.concepto_gasto_flete.text()
        if(validar_numeros(cantidad)):
            self.cantidad_gasto_flete.clear()
            self.concepto_gasto_flete.clear()
            motivo =  motivo
            total = -1*int(cantidad)
            agregar_venta_fletes(motivo,str(total))
        
        self.actualizar_interfaz()

    
    def actualizar_tabla_flete(self):
        df = registro_fletes()
        ingresos = df[df['precio']>0]
        ingresos = int(ingresos['precio'].sum())
        egresos = df[df['precio']<0]
        egresos = int(egresos['precio'].sum())
        
        saldo = ingresos + egresos
        self.valor_ingreso_flete.setText(str(ingresos))
        self.valor_egreso_flete.setText(str(egresos))
        self.valor_saldo_flete.setText(str(saldo))

#-------------------------------------------------------------------------------
#-----------------------------------pollos-------------------------------------

    def agregar_pollos(self):
        cantidad = self.cantidad__pollos.text()
        precio =self.precio_pollos.text()
        if(validar_numeros(cantidad,precio)):
            self.cantidad__pollos.clear()
            self.precio_pollos.clear()
            motivo = 'Compra pollitos' 
            total = -1*int(precio)*int(cantidad)
            agregar_venta_pollos(motivo,str(cantidad),str(total))
        self.actualizar_interfaz()

    def eliminar_pollos(self):
        cantidad = self.cantidad__pollos.text()
        if(validar_numeros(cantidad)):
            self.cantidad__pollos.clear()
            self.precio_pollos.clear()
            motivo = 'Compra pollitos' 
            agregar_venta_pollos(motivo,'-'+str(cantidad),'0')
        self.actualizar_interfaz()

    def vender_pollos(self):
        cantidad = self.cantidad_kilos__pollos.text()
        precio = self.precio_kilo_pollos.text()
        motivo = self.comentario_venta__pollos.toPlainText()

        if(validar_numeros(cantidad,precio)):
            self.cantidad_kilos__pollos.clear()
            self.precio_kilo_pollos.clear()
            self.comentario_venta__pollos.clear()
            
            motivo = 'venta pollo muerto' 
            total = int(precio)*int(cantidad)
            agregar_venta_pollos(motivo,str(0),str(total))
        self.actualizar_interfaz()


    def gastos_pollos(self):
        cantidad = self.cantidad_gastado_pollos.text()
        motivo = self.concepto_compra_pollos.text()

        if(validar_numeros(cantidad)):
            self.cantidad_gastado_pollos.clear()
            self.concepto_compra_pollos.clear()
            
            motivo = 'gasto pollo : '+ motivo 
            total = -1*int(cantidad)
            agregar_venta_pollos(motivo,str(0),str(total))
        self.actualizar_interfaz()
    
    def actualizar_dinero_pollos (self):
        df = registro_pollos()
        
        ingresos = df[df['precio']>0]
        ingresos = str(int(ingresos['precio'].sum()))
        egresos = df[df['precio']<0]
        egresos = str(int(egresos['precio'].sum()))
        cantidad_pollos = int(df['cantidad'].sum())
        saldo = str(int(ingresos) + int(egresos))
        cantidad_pollos_total = df[df['cantidad']>0]
        cantidad_pollos_total = int(cantidad_pollos_total['cantidad'].sum())
        mortalidad =100*(cantidad_pollos_total-cantidad_pollos)/cantidad_pollos_total
        self.valor_ingreso_pollos.setText(ingresos)
        self.valor_egreso__pollos.setText(egresos)
        self.valor_saldo__pollos.setText(saldo)
        self.cantidad_pollos_galpon.setText(str(cantidad_pollos))
        self.indice_mortalidad_pollos.setText(str(mortalidad))

    def actualizar_tabla_pollo(self):
        registros = registro_pollos()
        registros = registros.tail(10)
        for i,registro in enumerate(registros['fecha']):
            item_venta_acum = QTableWidgetItem()
            item_venta_acum.setText("".join(str(registro).split(' ')[0]))
            self.tabla_pollos.setItem(i,0,item_venta_acum)
            
        for i,registro in enumerate(registros['motivo']):
            item_venta_acum = QTableWidgetItem()
            item_venta_acum.setText(str(registro))
            self.tabla_pollos.setItem(i,1,item_venta_acum)
            
        for i,registro in enumerate(registros['precio']):
            item_venta_acum = QTableWidgetItem()
            item_venta_acum.setText(str(registro))
            self.tabla_pollos.setItem(i,2,item_venta_acum)
            

def main():
    # Crear_pollos()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Hello_world()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

main()


