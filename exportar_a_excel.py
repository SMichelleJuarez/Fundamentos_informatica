# Zona de importaciones
import openpyxl
import os

# Funcionalidad extra: cargar los datos en un excel
def excelLecturaExportacion(nombre_archivo, nombre_de_hoja, datos_bancarios):
    if os.path.exists(nombre_archivo):
        lib_ex = openpyxl.load_workbook(nombre_archivo)
        h = lib_ex[nombre_de_hoja] # Hoja actual.
    else:
        lib_ex = openpyxl.Workbook()
        h = lib_ex.active
        h.title = nombre_de_hoja
        # Agregar encabezados
        titulo_columnas = ['Usuario', 'Nro. cuenta', 'Monto', 'DNI', 'Género']
        h.append(titulo_columnas)
    for f in datos_bancarios:
        h.append(f)
    
    lib_ex.save(nombre_archivo)
    lib_ex.close()
    print('Los datos bancarios se guardaron con éxito.')