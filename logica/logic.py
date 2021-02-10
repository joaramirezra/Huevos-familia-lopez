def validar_numeros(*numeros):
    for numero in numeros:
        numero = str(numero)
        if (not numero.isnumeric()):
            return False
        if (int(numero)<0):
            return False 
    return True

#-------------------------------------------------------------------------------
def numero_de_unidades(cubetas): 
    return int(cubetas)*30

#-------------------------------------------------------------------------------
def numero_de_cubetas(cubetas,sobrantes):
    cubetas = int(cubetas)
    sobrantes = int(sobrantes)
    return cubetas+sobrantes//30,sobrantes%30

#-------------------------------------------------------------------------------