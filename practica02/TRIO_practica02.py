import os
import shutil


directorio_actual = os.getcwd()
print("Directorio actual:", directorio_actual)


print("\nArchivos y directorios en el directorio actual:")
contenido_directorio = os.listdir(directorio_actual)
for elemento in contenido_directorio:
    print(elemento)


nuevo_directorio = os.path.join(directorio_actual, "modules")
try:
    if "modules" in contenido_directorio:
        print("Directorio 'modules' ya existe")
    else:
        os.mkdir(nuevo_directorio)
        print("Directorio 'modules' creado")

except OSError as error:
    print("\nError al crear el directorio 'modules':", error)


with open(os.path.join(nuevo_directorio, "README.txt"), "w") as escritura:
    escritura.write("Este es un archivo README")

print("Archivo README.txt creado en el directorio 'modules'")


ruta_archivo_readme = os.path.join(nuevo_directorio, "README.txt")
if os.path.exists(ruta_archivo_readme):
    informacion_archivo = os.stat(ruta_archivo_readme)
    print("\nInformación detallada sobre el archivo 'README.txt':")
    print(f"Tamaño: {informacion_archivo.st_size} bytes")
    print(f"Fecha de modificación: {informacion_archivo.st_mtime}")


carpetas_a_copiar = ["c1", "c2"]
for carpeta in carpetas_a_copiar:
    origen = os.path.join(directorio_actual, carpeta)
    destino = os.path.join(nuevo_directorio, carpeta + "_copia")
    try:
        shutil.copytree(origen, destino)
        print(f"Se copiaron los archivos de '{carpeta}' a '{carpeta}_copia'")
    except Exception as error:
        print(f"Error al copiar archivos desde '{carpeta}': {error}")


for carpeta in carpetas_a_copiar:
    carpeta_path = os.path.join(directorio_actual, carpeta)
    if os.path.exists(carpeta_path) and os.path.isdir(carpeta_path):
        archivos_en_carpeta = os.listdir(carpeta_path)
        for archivo in archivos_en_carpeta:
            archivo_path = os.path.join(carpeta_path, archivo)
            try:
                if os.path.isfile(archivo_path):
                    os.remove(archivo_path)
                    print(f"Se eliminó el archivo '{archivo}' en '{carpeta}'")
            except Exception as error:
                print(f"Error al eliminar el archivo '{archivo}' en '{carpeta}': {error}")

print("\nTodas las tareas se han completado correctamente.")
