def contar_lineas_codigo(archivo):
    try:
        with open(archivo, "r") as file:
            lineas = file.readlines()
            contador = 0
            for linea in lineas:
                linea = linea.strip()  # Eliminar espacios en blanco al inicio y al final
                if linea != "" and not linea.startswith("#"):
                    contador += 1
            return contador
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    return 0

if __name__ == "__main__":
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    if ruta_archivo.endswith(".py"):
        lineas_codigo = contar_lineas_codigo(ruta_archivo)
        print(f"El archivo {ruta_archivo} tiene {lineas_codigo} líneas de código.")
    else:
        print("El archivo ingresado no es un archivo Python (.py)")
