import sys
import pandas as pd
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from logica.produccion import * 
from logica.ventas import *
from logica.caja_gallinas import * 
from logica.limones import *
from logica.cacao import *
from logica.fletes import *
from logica.caja_pollos import * 
from logica.alimento_pollos import *
from interfaz_grafica.interfaz_de_usuario import Ui_MainWindow

convertir_pesos = lambda x : f'{int(x):,.0f} PESOS'

class Hello_world(Ui_MainWindow):
    def __init__( self ):
        super().__init__()
        
    def setupUi( self, MW ):
        super().setupUi( MW )
        self.actualizar_interfaz()
        self.actualizar_produccion()
        
        MW.setFixedSize(962, 612)   
        self.boton_agregar_produccion.clicked.connect(self.agregar_produccion_gui)
        self.boton_eliminar_produccion.clicked.connect(self.eliminar_produccion_gui)
        
        self.boton_venta.clicked.connect(self.agregar_venta_gui)
        self.boton_devolucion.clicked.connect(self.devolver_venta_gui)
        
        self.boton_agregar_animales.clicked.connect(self.agregar_animales_gui)
        self.boton_dar_baja_animales.clicked.connect(self.eliminar_animales_gui)
        
        self.boton_comprar_alimento_2.clicked.connect(self.comprar_alimento_gui)
        self.boton_fiar_costales_2.clicked.connect(self.credito_caja_menor_gui)
        self.boton_ingresar_limon.clicked.connect(self.venta_limon_gui)
        self.boton_gastar_alimento.clicked.connect(self.alimentar_gallinas_gui)

        self.boton_egrasar_limon.clicked.connect(self.egreso_limon_gui)
        self.boton_reiniciar_limon.clicked.connect(self.reiniciar_limon_gui)

        self.boton_ingresar_cacao.clicked.connect(self.venta_cacao_gui)
        self.boton_egresar_cacao.clicked.connect(self.egreso_cacao_gui)
        self.boton_reinicio_cacao.clicked.connect(self.reiniciar_cacao_gui)


        self.boton_ingresar_fletes.clicked.connect(self.venta_fletes_gui)
        self.boton_egresar_flete.clicked.connect(self.egreso_fletes_gui)
        self.boton_reiniciar_fletes.clicked.connect(self.reiniciar_fletes_gui)
        self.boton_agregar__pollos.clicked.connect(self.comprar_pollos_gui)
        self.boton_dar_baja__pollos.clicked.connect(self.dar_baja_pollos)
        self.boton_invertir_caja_menor_4.clicked.connect(self.apoyo_caja_menor_pollos)
        self.boton_invertir_caja_menor_5.clicked.connect(self.enviar_banco_pollos)
        self.boton_vender_pollos.clicked.connect(self.vender_produccion_pollos)
        self.boton_fiar_costales_4.clicked.connect(self.fiar_comida_pollos)
        
        self.tipo_produccion_14.currentIndexChanged.connect(self.actualizar_deuda_pollos)
        self.tipo_produccion_4.currentIndexChanged.connect(self.actualizar_deuda_gallinas)
        
        self.boton_comprar_alimento_4.clicked.connect(self.comprar_alimento_pollos)
        self.boton_vender_empaques_3.clicked.connect(self.abonar_san_alejo_pollos)
        self.boton_vender_empaques_8.clicked.connect(self.abonar_agropaisa_pollos)
        self.boton_gastar_pollos_5.clicked.connect(self.gastos_generales_pollos)
        self.boton_gastar_alimento_4.clicked.connect(self.gasto_alimento_pollos)
        self.boton_devolver_alimento_3.clicked.connect(self.devolver_bultos_pollos)
        self.boton_gastar_pollos_2.clicked.connect(self.reiniciar_gui_pollos)
        self.boton_comprar_caja_menor.clicked.connect(self.gastos_generales_gallinas)
        self.boton_fiar_caja_menor.clicked.connect(self.credito_general_gallinas)
        self.boton_invertir_caja_menor.clicked.connect(self.apoyo_caja_menor_gallinas)
        self.boton_abonar.clicked.connect(self.abonar_deuda_gallinas)
        self.boton_vender_empaques.clicked.connect(self.venta_empaque_gallinas)
        self.boton_vender_empaques_2.clicked.connect(self.enviar_banco_gallinas)
        self.boton_devolver_alimento.clicked.connect(self.devolver_alimento_gallinas)
        self.boton_abonar_4.clicked.connect(self.desabonar_agropaisa_pollos)
        self.boton_abonar_3.clicked.connect(self.desabonar_san_alejo_pollos)
        self.boton_abonar_2.clicked.connect(self.desabonar_deuda_gallinas)
        self.boton_reiniciar_limon_2.clicked.connect(self.reiniciar_gallinas)


#-------------------------------------------------------------------------------

    def actualizar_interfaz(self):
        self.actualizar_gui_gallinas()
        self.actualizar_gui_limon()
        self.actualizar_gui_cacao()
        self.actualizar_gui_fletes()
        self.actualizar_gui_pollos()
#-------------------------------------------------------------------------------
# #---------------------------------produccion-----------------------------------
    def validar_numeros(self,*numeros):
        for numero in numeros:
            numero = str(numero)
            if (not numero.isnumeric()):
                return False
            if (int(numero)<0):
                return False 
        return True
#-------------------------------------------------------------------------------
    def valor_campo(self,campo):
        valor = campo.text()
        campo.clear()
        return valor

#-------------------------------------------------------------------------------
    def agregar_produccion_gui(self):
        validacion = self.validar_numeros(self.cubetas_produccion.text(),
                                       self.sobrantes_produccion.text())
        
        if(validacion):
            cubeta = self.valor_campo(self.cubetas_produccion)
            sobrantes = self.valor_campo(self.sobrantes_produccion)
            huevo  = self.tipo_produccion.currentText()
            agregar_huevos(huevo,int(cubeta),int(sobrantes))

        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def eliminar_produccion_gui(self):
        validacion = self.validar_numeros(self.cubetas_produccion.text(),
                                       self.sobrantes_produccion.text())
        
        if(validacion):
            huevo  = self.tipo_produccion.currentText()
            cantidad = int(cantidad_huevos_tipo(huevo))
            cubeta = int(self.valor_campo(self.cubetas_produccion))
            sobrantes = int(self.valor_campo(self.sobrantes_produccion))
            
            if(cantidad>=(cubeta*30+sobrantes)):
                eliminar_huevos(huevo,int(cubeta),int(sobrantes))
            else:
                self.cubetas_produccion.setText(str(cubeta))
                self.sobrantes_produccion.setText(str(sobrantes))
        self.actualizar_interfaz()



#-------------------------------------------------------------------------------
    def actualizar_gui_gallinas(self):
        self.actualizar_contabilidad_gallinas() #1
        self.actualizar_produccion()#2
        self.actualizar_inventario()#3
        self.actualizar_numero_animales()#4
        self.actualizar_rendimiento_diario()#5
        self.actualizar_bultos_disponibles()#6
        self.actualizar_costales_gui()#7
        self.actualizar_deuda_gallinas()#8
        self.actualizar_tabla_galllinas()#9

#1-------------------------------------------------------------------------------
    def actualizar_contabilidad_gallinas(self):
        caja_menor = cantidad_efectivo_gallinas()
        cupo_endeudamiento = 15000000
        cupo_endeudamiento -= int(valor_deuda_gallinas('Agropaisa_gallinas'))
        self.cantidad_efectivo.setText(convertir_pesos(caja_menor))
        self.cantidad_cupo.setText(convertir_pesos(cupo_endeudamiento))

#2------------------------------------------------------------------------------
    def actualizar_produccion(self):
        produccion_gallinas = obtener_inventario_huevos_diario()
        
        presentacion = ['cubetas','unidades','sobrantes','cantidad']
                
        for j,huevo in enumerate(tipos_huevo):
            
            mascara = produccion_gallinas['producto']==huevo
            produccion_tipo = produccion_gallinas[mascara]
            elementos = [str(int(produccion_tipo[pres])) for pres in presentacion ]
            for i in range(0,4):
                tiem = self.tabla_produccion_diaria.item(j,i)
                tiem.setText(str(elementos[i]))
        
        cubeta,unidades,sobrantes,cantidad = cantidad_total_huevos()

        for index,i in enumerate([cubeta,unidades,sobrantes,cantidad]):
            tiem = self.tabla_produccion_diaria.item(9,index)
            tiem.setText(str(i))



#3------------------------------------------------------------------------------
    def actualizar_inventario(self):
        produccion_gallinas =obtener_inventario_total()
        
        presentacion = ['cubetas','unidades','sobrantes','ventas_del_dia']
                
        for j,huevo in enumerate(tipos_huevo):
            mascara = produccion_gallinas['producto']==huevo
            produccion_tipo = produccion_gallinas[mascara]
            elementos = [str(int(produccion_tipo[pres])) for pres in presentacion ]
            for i in range(0,4):
                tiem = self.tabla_inventario.item(j,i)
                tiem.setText(str(elementos[i]))
        
        cubeta,unidades,sobrantes,cantidad = inventario_total_huevos()

        for index,i in enumerate([cubeta,unidades,sobrantes,cantidad]):
            tiem = self.tabla_inventario.item(9,index)
            tiem.setText(str(i))

#4------------------------------------------------------------------------------
    def actualizar_numero_animales(self):
        numero  = cantidad_gallinas()
        self.Empaques_gallinas_dis_2.setText(str(numero))

#5-------------------------------------------------------------------------------
    def actualizar_rendimiento_diario(self):
        rendimiento =float(rendimiento_gallinas())
        if (rendimiento<=1):
            self.rendimiento_gallinas.setValue(float(rendimiento)*100)
        else :
            self.rendimiento_gallinas.setValue(100)
#6------------------------------------------------------------------------------
    def actualizar_bultos_disponibles(self):
        cantidad = cantidad_bultos()
        self.bultos_gallinas_dis.setText(str(cantidad))

#7------------------------------------------------------------------------------
    def actualizar_costales_gui(self):
        cantidad_empaques = cantidad_costales() 
        self.Empaques_gallinas_dis.setText(str(cantidad_empaques))

#8------------------------------------------------------------------------------
    def actualizar_deuda_gallinas(self):
        entidad = self.tipo_produccion_4.currentText()
        valor = valor_deuda_gallinas(entidad+'_gallinas')
        self.cantidad_deuda_3.setText(convertir_pesos(valor))

#9------------------------------------------------------------------------------
    def actualizar_tabla_galllinas(self):
        df = transaccion_gallinas()
        
        for j in range(7) :
            for i in range(3) :
                    tiem = self.tabla_caja_menor.item(j,i)
                    tiem.setText(str((0)))
        
        
        for j,elementos in enumerate(df.itertuples()) :
            for i,elemento in enumerate(elementos[1:]) :
                    tiem = self.tabla_caja_menor.item(j,i)
                    tiem.setText(str((elemento)))


# # #-------------------------------------------------------------------------------
# # #---------------------------------Ventas----------------------------------------
    def agregar_venta_gui(self):
        validacion = self.validar_numeros(self.cantidad_venta.text(),
                                       self.precio_venta.text())
        
        if(validacion):
            huevo  = self.tipo_venta.currentText()
            presentacion = self.presentacion_venta.currentText()
            observacion = self.comentario_venta.toPlainText()
            precio = int(self.valor_campo(self.precio_venta))
            cantidad = int(self.valor_campo(self.cantidad_venta))

            total = cantidad*30 if (presentacion == 'CUBETAS') else cantidad
            
            disponibles = int(cantidad_huevos_inventario(huevo))
            
            if(int(disponibles)>=int(total)):
                agregar_venta(presentacion,huevo,cantidad,precio,observacion)
                self.comentario_venta.clear()
            else:
                self.cantidad_venta.setText(str(cantidad))
                self.precio_venta.setText(str(precio))

        self.actualizar_gui_gallinas()

# #-------------------------------------------------------------------------------
    def devolver_venta_gui(self):
        validacion = self.validar_numeros(self.cantidad_venta.text(),
                                       self.precio_venta.text())
        
        if(validacion):
            huevo  = self.tipo_venta.currentText()
            presentacion = self.presentacion_venta.currentText()
            observacion = self.comentario_venta.toPlainText()
            precio = int(self.valor_campo(self.precio_venta))
            cantidad = int(self.valor_campo(self.cantidad_venta))

            devolucion_venta(presentacion,huevo,cantidad,precio,observacion)
            
            self.actualizar_gui_gallinas()














#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
    def gastos_generales_gallinas(self):
        cantidad = self.cantidad_dinero_caja 
        observacion = self.motivo_gasto

        validacion = self.validar_numeros(cantidad.text())

        if(validacion):
            cantidad = int(self.valor_campo(cantidad))
            caja_menor = int(cantidad_efectivo_gallinas())
            
            if(caja_menor>=cantidad):
                motivo = observacion.toPlainText()
                observacion.clear()
                compra_aux_gallinas(int(cantidad),motivo)
            else :
                self.cantidad_dinero_caja.setText(str(cantidad))

        self.actualizar_gui_gallinas()
    
#-------------------------------------------------------------------------------
    def credito_general_gallinas(self):
        cantidad = self.cantidad_dinero_caja 
        observacion = self.motivo_gasto

        validacion = self.validar_numeros(cantidad.text())

        if(validacion):
            cantidad = self.valor_campo(cantidad)
            motivo = observacion.toPlainText()
            observacion.clear()
            
            credito_aux_gallinas(int(cantidad),motivo)

        self.actualizar_gui_gallinas()

#-------------------------------------------------------------------------------
    def apoyo_caja_menor_gallinas(self):
        cantidad = self.ingresar_dinero 
        validacion = self.validar_numeros(cantidad.text())

        if(validacion):
            cantidad = self.valor_campo(cantidad)
            
            apoyo_caja_menor_gallinas(int(cantidad))

        self.actualizar_gui_gallinas()

#-------------------------------------------------------------------------------
    def abonar_deuda_gallinas(self):
        cantidad = self.abonar_dinero 
        validacion = self.validar_numeros(cantidad.text())
        entidad = self.tipo_produccion_3.currentText()

        if(validacion):
            caja_menor = int(cantidad_efectivo_gallinas())
            cantidad = int(self.valor_campo(cantidad))
            deuda = int(valor_deudad_pollos(entidad+'_gallinas'))
            puede_pagar = (cantidad<= caja_menor)
            paga_de_mas = (cantidad<= deuda)

            if(puede_pagar and paga_de_mas):
                abono_credito_gallinas(int(cantidad),entidad+'_gallinas')
            else : 
                self.abonar_dinero.setText(str(cantidad))

        self.actualizar_gui_gallinas()

    def desabonar_deuda_gallinas(self):
        cantidad = self.abonar_dinero 
        validacion = self.validar_numeros(cantidad.text())
        entidad = self.tipo_produccion_3.currentText()

        if(validacion):
            cantidad = int(self.valor_campo(cantidad))
            deuda = int(valor_deudad_pollos(entidad+'_gallinas'))
            
            tiene_cupo = (cantidad+deuda <= 15000000)

            if(tiene_cupo):
                desabono_credito_gallinas(int(cantidad),entidad+'_gallinas')
            else : 
                self.abonar_dinero.setText(str(cantidad))

        self.actualizar_gui_gallinas()

    def reiniciar_gallinas(self):
        reiniciar_produccion_gallinas()
        self.actualizar_gui_gallinas()


        



            
            

#-------------------------------------------------------------------------------
    def venta_empaque_gallinas(self):
        cantidad = self.cantidad_empaques_venta 
        precio = self.precio_empaque_venta

        validacion = self.validar_numeros(cantidad.text(),precio.text())

        if(validacion):
            costales = int(cantidad_costales())
            cantidad = int(self.valor_campo(cantidad))

            if(cantidad<=costales):
                precio = int(self.valor_campo(precio))

                venta_empaques(int(cantidad),precio)
            else :
                self.cantidad_empaques_venta.setText(str(cantidad))

        self.actualizar_gui_gallinas()

#-------------------------------------------------------------------------------
    def enviar_banco_gallinas(self):
        cantidad = self.precio_empaque_venta_2 
        validacion = self.validar_numeros(cantidad.text())

        if(validacion):
            caja_menor = int(cantidad_efectivo_gallinas())
            cantidad = int(self.valor_campo(cantidad))
            
            if(caja_menor>=cantidad):
                salida_caja_menor(int(cantidad))
            else: 
                self.precio_empaque_venta_2.setText(str(cantidad))
        self.actualizar_gui_gallinas()

#-------------------------------------------------------------------------------
    def comprar_alimento_gui(self):
        cantidad = self.cantidad_bultos_adquirir_2
        precio = self.precio_adquisicion_costal_2
        condicion = self.validar_numeros(cantidad.text(),precio.text())
        
        if(condicion):
            caja_menor = int(cantidad_efectivo_gallinas())
            cantidad = int(self.valor_campo(cantidad))
            precio = int(self.valor_campo(precio))
            
            if(caja_menor >= cantidad*precio):
                comprar_alimento(cantidad,precio)
            else : 
                self.cantidad_bultos_adquirir_2.setText(str(cantidad))
                self.precio_adquisicion_costal_2.setText(str(precio))
                
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def credito_caja_menor_gui(self):
        cantidad_bultos = self.cantidad_bultos_adquirir_3
        costo = self.precio_adquisicion_costal_3
        banco = self.tipo_produccion_2
        
        condicion = self.validar_numeros(cantidad_bultos.text(),costo.text())
        
        if(condicion):
            cantidad = int(self.valor_campo(cantidad_bultos))
            precio = int(self.valor_campo(costo))
            entidad = banco.currentText()+'_gallinas'
            credito_alimento(cantidad,precio,entidad)

        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def alimentar_gallinas_gui(self):
        cantidad  = self.cantidad_alimento_dado

        condicion = self.validar_numeros(cantidad.text())
        
        if(condicion):
            bultos = int(cantidad_bultos())
            cantidad = int(self.valor_campo(cantidad))
            if(bultos>= cantidad):
               alimentar_gallinas(cantidad)
            else :
                self.cantidad_alimento_dado.setText(str(cantidad))
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def devolver_alimento_gallinas(self):
        cantidad  = self.cantidad_alimento_dado

        condicion = self.validar_numeros(cantidad.text())
        
        if(condicion):
            cantidad = int(self.valor_campo(cantidad))
            empaques = int(cantidad_costales())

            if(cantidad<=empaques):
                devolver_alimento(cantidad)
            else:
                self.cantidad_alimento_dado.setText(str(cantidad))

        self.actualizar_interfaz()


#---------------------------------Rendimiento-----------------------------------
    def agregar_animales_gui(self):
        numero = self.validar_numeros(self.cantidad_gallinas_gestion.text())
        if(numero):
            cantidad = self.valor_campo(self.cantidad_gallinas_gestion)
            agregar_gallinas(int(cantidad))
            
        self.actualizar_interfaz()

#-------------------------------------------------------------------------------
    def eliminar_animales_gui(self):
        numero = self.validar_numeros(self.cantidad_gallinas_gestion.text())
        if(numero):
            cantidad = self.valor_campo(self.cantidad_gallinas_gestion)
            if(cantidad_gallinas()>=int(cantidad)):
                matar_gallinas(int(cantidad))
            else :
                self.cantidad_gallinas_gestion.setText(str(cantidad))
        self.actualizar_interfaz()
        





















#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
    def actualizar_limon_gui(self):
        ingresos,egresos,saldo = contabilidad_limon()
        efectivo = convertir_pesos(ingresos)
        egreso = convertir_pesos(egresos)
        saldo = convertir_pesos(saldo)

        self.ingresos_limon.setText(efectivo)
        self.egresos_limon.setText(egreso)
        self.saldo_total_limones.setText(saldo)

#-------------------------------------------------------------------------------
    def venta_limon_gui(self):
        cantidad = self.cantidad_limones_venta_6 
        precio = self.valor_venta_limon_6
        observacion = self.observacion_limon_6

        validacion = self.validar_numeros(cantidad.text(),precio.text())
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            precio = self.valor_campo(precio)
            
            motivo = observacion.toPlainText()
            observacion.clear()
            
            venta_limon(int(cantidad),int(precio),motivo)

        self.actualizar_gui_limon()
    
#-------------------------------------------------------------------------------
    def egreso_limon_gui(self):
        _,_,disponible = contabilidad_limon()
        cantidad = self.cantidad_gasto_limon_6 
        observacion = self.concepto_gasto_limon_6
        validacion = self.validar_numeros(cantidad.text())

        if(validacion):
            cantidad = self.valor_campo(cantidad)
            if(int(cantidad) <= int(disponible)):            
                motivo = observacion.text()
                observacion.clear()
                gastos_limon(int(cantidad),motivo)
            else :
                self.cantidad_gasto_limon_6.setText(cantidad)
        
        self.actualizar_gui_limon()

#-------------------------------------------------------------------------------
    def actualizar_tabla_limon(self):
        df = transacciones_limon()
        
        for j in range(14) :
            for i in range(3) :
                    tiem = self.tabla_transacciones_limones.item(j,i)
                    tiem.setText(str((0)))
        
        for j,elementos in enumerate(df.itertuples()) :
            for i,elemento in enumerate(elementos[1:]) :
                    tiem = self.tabla_transacciones_limones.item(j,i)
                    tiem.setText(str((elemento)))
        
#-------------------------------------------------------------------------------
    def reiniciar_limon_gui(self):
        reiniciar_limon()
        self.actualizar_gui_limon()

    def actualizar_gui_limon(self):
        self.actualizar_limon_gui()
        self.actualizar_tabla_limon()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
    def actualizar_saldos_cacao_gui(self):
        ingresos,egresos,saldo = contabilidad_cacao()
        efectivo = convertir_pesos(ingresos)
        egreso = convertir_pesos(egresos)
        saldo = convertir_pesos(saldo)

        self.ingresos_cacao.setText(efectivo)
        self.egreso_cacao.setText(egreso)
        self.saldo_total_cacao.setText(saldo)

#-------------------------------------------------------------------------------
    def venta_cacao_gui(self):
        cantidad = self.cantidad_cacao_venta 
        precio = self.valor_venta_caco
        observacion = self.observacion_limon_4

        validacion = self.validar_numeros(cantidad.text(),precio.text())
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            precio = self.valor_campo(precio)
            
            motivo = observacion.toPlainText()
            observacion.clear()
            
            venta_cacao(int(cantidad),int(precio),motivo)

        self.actualizar_gui_cacao()
    
#-------------------------------------------------------------------------------
    def egreso_cacao_gui(self):
        _,_,disponible = contabilidad_cacao()
        cantidad = self.cantidad_egreso_cacao 
        observacion = self.concepto_egreso_cacao

        validacion = self.validar_numeros(cantidad.text())

        if(validacion):
            cantidad = self.valor_campo(cantidad)
            if(int(cantidad) <= int(disponible)):            
                motivo = observacion.text()
                observacion.clear()
                gastos_cacao(int(cantidad),motivo)
            else :
                self.cantidad_egreso_cacao.setText(cantidad)
        
        self.actualizar_gui_cacao()

#-------------------------------------------------------------------------------
    def actualizar_tabla_cacao(self):
        df = transacciones_cacao()
        
        for j in range(14) :
            for i in range(3) :
                    tiem = self.tabla_transacciones_cacao.item(j,i)
                    tiem.setText(str((0)))
        
        for j,elementos in enumerate(df.itertuples()) :
            for i,elemento in enumerate(elementos[1:]) :
                    tiem = self.tabla_transacciones_cacao.item(j,i)
                    tiem.setText(str((elemento)))
        
#-------------------------------------------------------------------------------
    def reiniciar_cacao_gui(self):
        reiniciar_cacao()
        self.actualizar_gui_cacao()

#-------------------------------------------------------------------------------
    def actualizar_gui_cacao(self):
        self.actualizar_saldos_cacao_gui()
        self.actualizar_tabla_cacao()
        
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
    def actualizar_saldos_fletes_gui(self):
        ingresos,egresos,saldo = contabilidad_fletes()
        efectivo = convertir_pesos(ingresos)
        egreso = convertir_pesos(egresos)
        saldo = convertir_pesos(saldo)

        self.ingresos_fletes.setText(efectivo)
        self.egresos_fletes.setText(egreso)
        self.saldo_total_fletes.setText(saldo)

#-------------------------------------------------------------------------------
    def venta_fletes_gui(self):
        cantidad = self.cantidad_fletes 
        precio = self.valor_flete
        observacion = self.observacion_flete

        validacion = self.validar_numeros(cantidad.text(),precio.text())
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            precio = self.valor_campo(precio)
            
            motivo = observacion.toPlainText()
            observacion.clear()
            
            venta_fletes(int(cantidad),int(precio),motivo)

        self.actualizar_gui_fletes()
    
#-------------------------------------------------------------------------------
    def egreso_fletes_gui(self):
        _,_,disponible = contabilidad_fletes()
        cantidad = self.cantidad_egreso_flete 
        observacion = self.concepto_gasto_limon_7

        validacion = self.validar_numeros(cantidad.text())

        if(validacion):
            cantidad = self.valor_campo(cantidad)
            if(int(cantidad) <= int(disponible)):            
                motivo = observacion.text()
                observacion.clear()
                gastos_fletes(int(cantidad),motivo)
            else :
                self.cantidad_egreso_flete.setText(cantidad)
        
        self.actualizar_gui_fletes()

#-------------------------------------------------------------------------------
    def actualizar_tabla_fletes(self):
        df = transacciones_fletes()
        
        for j in range(14) :
            for i in range(3) :
                    tiem = self.tabla_transacciones_fletes.item(j,i)
                    tiem.setText(str((0)))
        
        for j,elementos in enumerate(df.itertuples()) :
            for i,elemento in enumerate(elementos[1:]) :
                    tiem = self.tabla_transacciones_fletes.item(j,i)
                    tiem.setText(str((elemento)))
        
#-------------------------------------------------------------------------------
    def reiniciar_fletes_gui(self):
        reiniciar_fletes()
        self.actualizar_gui_fletes()

    def actualizar_gui_fletes(self):
        self.actualizar_saldos_fletes_gui()
        self.actualizar_tabla_fletes()

#-------------------------------------------------------------------------------
    def actualizar_gui_pollos(self):
        self.actualizar_caja_pollos()
        self.actualizar_rendimiento_pollos()
        self.actualizar_alimento_pollos()
        self.actualizar_deuda_pollos()
        self.actualizar_tabla_pollos()

#-------------------------------------------------------------------------------
    def actualizar_caja_pollos(self):
        ingresos,egresos,saldo = contabilidad_pollos()
        self.valor_ingreso_limon_8.setText(convertir_pesos(ingresos))
        self.valor_egreso_limon_8.setText(convertir_pesos(egresos))
        self.valor_saldo_limon_8.setText(convertir_pesos(saldo))
        self.valor_saldo_limon_9.setText(convertir_pesos(saldo))
        
#-------------------------------------------------------------------------------
    def actualizar_rendimiento_pollos(self):
        pollos_vivos = cantidad_pollos_vivos()
        mortalidad = calcular_mortalidad()
        self.cantidad_pollos_galpon.setText(str(pollos_vivos))
        self.indice_mortalidad_pollos.setText(str(round(1-mortalidad,2)*100))

#-------------------------------------------------------------------------------
    def actualizar_alimento_pollos(self):
        cantidad = cantidad_bultos_pollos()
        self.bultos_gallinas_dis_3.setText(str(cantidad))

#-------------------------------------------------------------------------------
    def actualizar_deuda_pollos(self):
        entidad = self.tipo_produccion_14.currentText()
        valor = valor_deudad_pollos(entidad+'_pollos')
        self.valor_egreso_limon_9.setText(convertir_pesos(valor))

#-------------------------------------------------------------------------------
    def comprar_pollos_gui(self):
        cantidad = self.cantidad__pollos 
        precio = self.precio_pollos
        
        validacion = self.validar_numeros(cantidad.text(),precio.text())
        
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            precio = self.valor_campo(precio)
        
            compra_pollos(int(cantidad),int(precio))

        self.actualizar_gui_pollos()
    
#-------------------------------------------------------------------------------
    def dar_baja_pollos(self):
        cantidad = self.cantidad__pollos_2 
        
        validacion = self.validar_numeros(cantidad.text())
        
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            if(int(cantidad)<=int(cantidad_pollos_vivos())):
                matar_pollos(int(cantidad))
            else:
                self.cantidad__pollos_2.setText(str(cantidad))
        
        self.actualizar_gui_pollos()
    
#-------------------------------------------------------------------------------
    def apoyo_caja_menor_pollos(self):
        cantidad = self.ingresar_dinero_4 
        
        validacion = self.validar_numeros(cantidad.text())
        
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            apoyo_caja_pollo(cantidad)
        
        self.actualizar_gui_pollos()
    
#-------------------------------------------------------------------------------
    def enviar_banco_pollos(self):
        cantidad = self.ingresar_dinero_5 
        
        validacion = self.validar_numeros(cantidad.text())
        
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            if(int(cantidad)<=int(cantidad_efectivo_pollos())):
                enviar_banco_pollos(int(cantidad))
            else:
                self.ingresar_dinero_5.setText(str(cantidad))
        
        self.actualizar_gui_pollos()
    
#-------------------------------------------------------------------------------
    def vender_produccion_pollos(self):
        cantidad = self.cantidad_kilos__pollos.text()
        precio = self.precio_kilo_pollos
        
        try:
            float(cantidad)
            validacion = self.validar_numeros(precio.text())
        except ValueError:
            validacion = False
        
        if(validacion):
            precio = self.valor_campo(precio)
            self.cantidad_kilos__pollos.clear()
            venta_produccion_pollos(float(cantidad),int(precio))

        self.actualizar_gui_pollos()

#-------------------------------------------------------------------------------
    def fiar_comida_pollos(self):
        cantidad = self.cantidad_bultos_adquirir_6 
        precio = self.precio_adquisicion_costal_6
        entidad = self.tipo_produccion_13.currentText()

        validacion = self.validar_numeros(cantidad.text(),precio.text())
        
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            precio = self.valor_campo(precio)
        
            fiar_alimento_pollos(int(cantidad),int(precio),entidad+'_pollos')

        self.actualizar_gui_pollos()

#-------------------------------------------------------------------------------
    def comprar_alimento_pollos(self):
        cantidad = self.cantidad_bultos_adquirir_7 
        precio = self.precio_adquisicion_costal_7
        
        validacion = self.validar_numeros(cantidad.text(),precio.text())
        
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            precio = self.valor_campo(precio)
        
            comprar_alimento_pollos(int(cantidad),int(precio))

        self.actualizar_gui_pollos()

#-------------------------------------------------------------------------------
    def abonar_san_alejo_pollos(self):
        cantidad = self.precio_empaque_venta_3 
        
        validacion = self.validar_numeros(cantidad.text())
        
        if(validacion):
            cantidad = int(self.valor_campo(cantidad))
            efectvo = int(cantidad_efectivo_pollos())
            deuda = int(valor_deudad_pollos('San alejo_pollos'))

            puede_pagar = (cantidad<= efectvo)
            paga_de_mas = (cantidad<= deuda)
            
            if(puede_pagar and paga_de_mas):
                abonar_deuda_pollos(int(cantidad),'San alejo_pollos')
            else:
                self.precio_empaque_venta_3.setText(str(cantidad))
        
        self.actualizar_gui_pollos()


#-------------------------------------------------------------------------------
    def abonar_agropaisa_pollos(self):
        cantidad = self.precio_empaque_venta_8        
        validacion = self.validar_numeros(cantidad.text())
        
        if(validacion):
            cantidad = int(self.valor_campo(cantidad))
            efectvo = int(cantidad_efectivo_pollos())
            deuda = int(valor_deudad_pollos('Agropaisa_pollos'))

            puede_pagar = (cantidad<= efectvo)
            paga_de_mas = (cantidad<= deuda)
            
            if(puede_pagar and paga_de_mas):
                abonar_deuda_pollos(int(cantidad),'Agropaisa_pollos')
            else:
                self.precio_empaque_venta_8.setText(str(cantidad))
        
        self.actualizar_gui_pollos()

#-------------------------------------------------------------------------------
# #-------------------------------------------------------------------------------
    def desabonar_san_alejo_pollos(self):
        cantidad = self.precio_empaque_venta_3 
        validacion = self.validar_numeros(cantidad.text())
        
        if(validacion):
            cantidad = int(self.valor_campo(cantidad))
            deuda = int(valor_deudad_pollos('San alejo_pollos'))

            se_puede_devolver = ((deuda+cantidad) <= 15000000 )
            
            if(se_puede_devolver):
                desabonar_deuda_pollos(int(cantidad),'San alejo_pollos')
            else:
                self.precio_empaque_venta_3.setText(str(cantidad))
        
        self.actualizar_gui_pollos()


#-------------------------------------------------------------------------------
    def desabonar_agropaisa_pollos(self):
        cantidad = self.precio_empaque_venta_8 
        validacion = self.validar_numeros(cantidad.text())

        if(validacion):
            cantidad = int(self.valor_campo(cantidad))
            deuda = int(valor_deudad_pollos('Agropaisa_pollos'))

            se_puede_devolver = ((deuda+cantidad) <= 15000000 )
            
            if(se_puede_devolver):
                desabonar_deuda_pollos(int(cantidad),'Agropaisa_pollos')
            else:
                self.precio_empaque_venta_8.setText(str(cantidad))
        
        self.actualizar_gui_pollos()

#-------------------------------------------------------------------------------
    def gastos_generales_pollos(self):
        cantidad = self.cantidad_gastado_pollos_3 
        concepto = self.concepto_compra_pollos_3

        validacion = self.validar_numeros(cantidad.text())
        
        if(validacion):
            cantidad = self.valor_campo(cantidad)
            gastos_general_pollos(int(cantidad),concepto.text())
            concepto.clear()
        self.actualizar_gui_pollos()

#-------------------------------------------------------------------------------
    def gasto_alimento_pollos(self):
        cantidad = self.cantidad_alimento_dado_4 

        validacion = self.validar_numeros(cantidad.text())
        
        if(validacion):
            cantidad = int(self.valor_campo(cantidad))
            if(cantidad<=int(cantidad_bultos_pollos())):
                gastar_alimento_pollos(int(cantidad))
            else :
                self.cantidad_alimento_dado_4.setText(str(cantidad))
        self.actualizar_costales_gui()
        self.actualizar_gui_pollos()

#-------------------------------------------------------------------------------
    def devolver_bultos_pollos(self):
        cantidad = self.cantidad_alimento_dado_4 

        validacion = self.validar_numeros(cantidad.text())
        
        if(validacion):
            empaques = int(cantidad_costales())
            cantidad = int(self.valor_campo(cantidad))

            if(cantidad<=empaques):
                devolver_alimento_pollos(int(cantidad))
            else :
                self.cantidad_alimento_dado_4.setText(str(cantidad))
        self.actualizar_costales_gui()         
        self.actualizar_gui_pollos()

    def reiniciar_gui_pollos(self):
        reiniciar_pollos()
        self.actualizar_gui_pollos()

#-------------------------------------------------------------------------------

    def actualizar_tabla_pollos(self):
        df = transaccion_pollos()
        
        for j in range(9) :
            for i in range(3) :
                    tiem = self.tabla_pollos.item(j,i)
                    tiem.setText(str((0)))
        
        
        for j,elementos in enumerate(df.itertuples()) :
            for i,elemento in enumerate(elementos[1:]) :
                    tiem = self.tabla_pollos.item(j,i)
                    tiem.setText(str((elemento)))

    
        self.tabs.setStyleSheet('QTabBar::tab:selected {'
                                'color: black;'
                                'background-color: #a2c07e;'
                                ' }')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Hello_world()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

main()


