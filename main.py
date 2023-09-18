import datetime
from persona import Persona
from autor import Autor
from libro import Libro
from categoria import Categoria

# Función para cargar los libros desde el archivo "libros.txt"
def cargar_libros_desde_archivo():
    libros = []
    try:
        with open("libros.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 6:  # Ahora hay 6 partes, incluida la categoría
                    cod_libro, titulo, año, tomo, autor_info, categoria = parts
                    # Dividir la información del autor en partes
                    autor_parts = autor_info.split(": Autor: ")
                    if len(autor_parts) == 2:
                        autor_nombre = autor_parts[1]
                        libros.append(Libro(cod_libro, titulo, año, tomo, Autor(cod_autor=cod_libro, nombre=autor_nombre), categoria))
    except FileNotFoundError:
        pass  # El archivo no existe, se creará cuando se guarden libros
    return libros

# Función para generar un informe de libros
def generar_reporte_libros():
    try:
        with open("libros.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No hay libros en el archivo para generar un informe.")
        else:
            # Obtener la fecha y hora actual
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")  # Cambiar ':' por '_'

            # Crear el nombre de archivo para el informe
            nombre_archivo = "reporte.txt"

            # Generar el informe en un archivo separado
            with open(nombre_archivo, "a") as reporte_file:
                reporte_file.write(f"Informe de Libros - Fecha y Hora: {fecha_actual}\n\n")
                for line in lines:
                    reporte_file.write(line)

            print(f"Informe de libros generado en el archivo '{nombre_archivo}'")
    except FileNotFoundError:
        print("El archivo 'libros.txt' no existe o no se puede abrir.")

# Función para guardar libros en el archivo "libros.txt"
def guardar_libros(libros):
    with open("libros.txt", "a") as file:
        for libro in libros:
            file.write(f"{libro.cod_libro}, {libro.titulo}, {libro.año}, {libro.tomo}, Autor: {libro.autor.nombre}, {libro.categoria}\n")
            
# Función para eliminar un libro por su código
def eliminar_libro(libros, cod_libro):
    libro_encontrado = None
    for libro in libros:
        if libro.cod_libro == cod_libro:
            libro_encontrado = libro
            libros.remove(libro)
            break 
    
    return libro_encontrado

# Función principal que muestra el menú
def menu():
    libros = []  # Lista para almacenar los libros en memoria
    
    while True:
        print("\nMenú de Opciones:")
        print("1. Ingresar Libros")
        print("2. Guardar Libros")
        print("3. Eliminar Libros")
        print("4. Generar Informe de Libros")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Código para ingresar los datos de un libro
            cod_libro = input("Ingrese el código del libro: ")
            titulo = input("Ingrese el título del libro: ")
            año = input("Ingrese el año del libro: ")
            tomo = input("Ingrese el tomo del libro: ")

            autor_cod = input("Ingrese el código del autor: ")
            autor_nombre = input("Ingrese el nombre del autor: ")

            categoria = input("Ingrese la categoría del libro: ")

            # Crear un nuevo objeto Autor
            autor = Autor(cod_autor=autor_cod, nombre=autor_nombre, pais=None, editorial=None)
            libro = Libro(cod_libro=cod_libro, titulo=titulo, año=año, tomo=tomo, autor=autor, categoria=categoria)
            libros.append(libro)
            print("Libro ingresado exitosamente.")
            
        elif opcion == "2":
            # Código para guardar los libros
            if not libros:
                print("No hay libros ingresados para guardar.")
            else:
                guardar_libros(libros)
                print("Libros guardados en 'libros.txt'")
            
        elif opcion == "3":
            # Código para eliminar un libro por código
            cod_libro = input("Ingrese el código del libro que desea eliminar: ")
            libro_eliminado = eliminar_libro(libros, cod_libro)
            if libro_eliminado:
                print(f"Libro '{libro_eliminado.titulo}' eliminado exitosamente.")
            else:
                print(f"No se encontró un libro con el código '{cod_libro}'.")
            
        elif opcion == "4":
            # Generar el informe de libros
            generar_reporte_libros()
            
        elif opcion == "5":
            break

if __name__ == "__main__":
    menu()
