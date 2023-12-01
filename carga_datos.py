def cargar_datos():
    datos = [ ]
    usuario = input("Ingrese el nombre del cliente: ")
    while usuario.upper() != "ZZZ":
        numero_cuenta = input("Ingrese el número de cuenta: ")
        dni = input("Ingrese el dni: ")
        monto_actual = int(input("Ingrese el monto existente en la cuenta: "))
        genero = input("Ingrese el género; [F] femenimo, [M] masculino, [X] no binario: ")
        datos.append([usuario, numero_cuenta, monto_actual, dni, genero])
        usuario = input("Ingrese el nombre de usuario, para terminar la carga ingrese zzz: ")
    return datos

