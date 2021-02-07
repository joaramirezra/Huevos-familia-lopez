

#-------------------------------------------------------------------------------
        self.agregar_produccion.clicked.connect(self.agregar_produccon_button)
        self.eliminar_produccion.clicked.connect(self.borrar_produccon_button)
#-------------------------------------------------------------------------------
        
    def agregar_produccon_button(self):
        unidades = self.unidade_produccion.text()
        cubetas = self.cubetas_produccion.text()
        SOBRANTES = self.sobrantes_produccion.text()
        galpon = self.galpon_produccion.currentText()
        huevo  = self.tipo_produccion.currentText()
        galpon=  1 if(galpon == 'GALLINAS') else 0
        tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO VENTA','DESTRUIDOS']
        huevo = tipos_huevo.index(huevo)

        agregar_huevos(galpon,huevo,str(unidades),str(cubetas),str(SOBRANTES))
        self.actualizar_produccion_diaria()
        
#-------------------------------------------------------------------------------
    def borrar_produccon_button(self):
        unidades = '-'+self.unidade_produccion.text()
        cubetas = '-' +self.cubetas_produccion.text()
        SOBRANTES = '-'+ self.sobrantes_produccion.text()
        galpon = self.galpon_produccion.currentText()
        huevo  = self.tipo_produccion.currentText()

        galpon=  1 if(galpon == 'GALLINAS') else 0
        tipos_huevo = ['PIPO','B','A','AA','AAA','JUMBO','BLANCO','VENCIDO VENTA','DESTRUIDOS']
        huevo = tipos_huevo.index(huevo)
        agregar_huevos(galpon,huevo,str(unidades),str(cubetas),str(SOBRANTES))
        self.actualizar_produccion_diaria()

        self.graphicsView_2.setBackground('#3c3f58')
        self.graphicsView_2.showGrid(x=True, y=True,alpha=0.2)
        

#-------------------------------------------------------------------------------

    def actualizar_produccion_diaria(self):
        # move a row elements   
        self.tabWidget.produccion_diaria.item(5,5).setText('hola')
        # produccion_diaria.item(5,5)
        # elemento.setText("g")
        # print(produccion_hoy)



        self.graphicsView_2.setBackground('#3c3f58')
        self.graphicsView_3.setBackground('#3c3f58')
        self.graphicsView_4.setBackground('#3c3f58')
        self.graphicsView_5.setBackground('#3c3f58')
        