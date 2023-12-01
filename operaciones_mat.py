#Funcion calcula el promedio de montos
def promedio(lista):
    suma = 0 
    contador = 0 
    for sueldo in lista:
        suma = suma + sueldo[2]
        contador += 1
    if contador != 0:
        prom = suma / contador
        return prom
    else: 
        return 0

#Función que calcula el porcentaje de distrubución por sexo

def porcentaje(lista):
    cuentas_femenino = 0
    cuentas_masculino = 0
    cuentas_binario = 0
    cuentas_otro = 0
    
    for genero in lista:
        if genero[4].upper() == "M":
            cuentas_masculino += 1
        elif genero[4].upper() == "F":
            cuentas_femenino += 1
        elif genero[4].upper() == "X":
           cuentas_binario += 1
        else: 
            cuentas_otro += 1
          
  # Calcular el total de cuentas
    total_cuentas = len(lista)

    # Calcular los porcentajes
    porcentaje_masculino = (cuentas_masculino*100) / total_cuentas
    porcentaje_femenino = (cuentas_femenino * 100 ) / total_cuentas
    porcentaje_binario = (cuentas_binario * 100 ) / total_cuentas
    porcentaje_otro = (cuentas_otro * 100 ) / total_cuentas

    # Devolver los resultados
    tupla = (["Procentaje de hombres", porcentaje_masculino], ["Porsentaje de mujeres", porcentaje_femenino], ["Porcentaje no binario", porcentaje_binario], ["Porcentaje dato mal ingresado", porcentaje_otro])
    return tupla

