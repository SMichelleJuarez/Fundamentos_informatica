#Importaciones de funciones
from carga_datos import cargar_datos
from menu import menu
from modulo_busqueda import mayor_monto, menor_monto, busca_cliente_nombre, busca_cliente_DNI
from operaciones_mat import porcentaje, promedio
from formatear_datos_clientes import imprimeDatos
from exportar_a_excel import excelLecturaExportacion

#Invocaciones
datos = cargar_datos()
menu()
opcion = int(input("Ingrese una opción: "))
while opcion != 8:
    if opcion == 1:
        print("El mayor monto corresponde a: ")
        mayor_monto = mayor_monto(datos)
        imprimeDatos(mayor_monto)
    elif opcion == 2:
        print("El monto menor corresponde a: ")
        menor_monto = menor_monto(datos)
        imprimeDatos(menor_monto)
    elif opcion == 3:
        print("-" * 79)
        print("El promedio es: ", promedio(datos))
        print("-" * 79)
    elif opcion == 4:
        print("-" * 79)
        print(porcentaje(datos))
        print("-" * 79)
    elif opcion == 5:
       datos_conNombre  = busca_cliente_nombre(datos)
       imprimeDatos(datos_conNombre)
    elif opcion == 6: 
        datos_conDNI = busca_cliente_DNI(datos)
        imprimeDatos(datos_conDNI)
    elif opcion == 7:
        n_a = input("Nombre del archivo excel: ") + ".xlsx"
        h = input("Nombre de la hoja del libro excel: ")
        excelLecturaExportacion(n_a, h, datos)
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
    menu()
    opcion = int(input("Ingrese una opción: "))
print("El programa finalizo")
