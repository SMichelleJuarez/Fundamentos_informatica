#Funcion calcula el monto mayor existente en la cuenta
def mayor_monto(lista):
    monto_maximo = lista[0]
    for cliente in lista:
        if cliente[2] > monto_maximo[2]:
            monto_maximo = cliente
    return  monto_maximo

#Funcion calcula el monto menor existente en la cuenta
def menor_monto(lista):
    monto_menor = lista[0]
    for cliente in lista:
        if cliente[2] < monto_menor[2]:
            monto_menor = cliente
    return monto_menor

#Función busca e imprime los datos de un cliente por medio del nombre
def busca_cliente_nombre(lista):
    nombre = input("Ingrese el nombre del cliente que desea buscar: ")
    for cliente in lista:
        if cliente[0].lower() == nombre.lower():
            return cliente

#Función busca e imprime los datos de un cliente por medio del DNI

def busca_cliente_DNI(lista):
    num_dni = input("Ingrese el número de DNI del cliente que desea buscar: ")
    for cliente in lista:
        if cliente[0] == num_dni:
            return cliente

