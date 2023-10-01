from alumno import Alumno
from docente import Docente
from cursos import Curso

##LISTA DE CURSOS
lista_cursos = []
lista_alumnos = []#lista para almacenar alumnos
lista_docente = []#lista para almacenar docentes
# Crear instancias de cursos

docente1=Docente('nombre1', 'paterno', 'materno', 'dni', '123', 'FIIS')
lista_docente.append(docente1)
alumno1=Alumno('nombre1', 'paterno', 'materno', 'fabu', '123', 'FIIS', 2021)
lista_alumnos.append(alumno1)
curso_algebra = Curso('C001', 'Algebra')
curso_matematica = Curso('C002', 'Matematica')
curso_filosofia = Curso('C003', 'Filosofia')

lista_cursos.append(curso_algebra)
lista_cursos.append(curso_matematica)
lista_cursos.append(curso_filosofia)


def asignar_curso_docente():
    print("Asignación de curso a docente")
    
    # Mostrar la lista de cursos disponibles
    print("Cursos disponibles:")
    for curso in lista_cursos:
        print(f"{curso.get_codigo()}: {curso.get_nombre()}")

    # Pedir al usuario que seleccione un curso
    codigo_curso = input("Ingrese el código del curso que desea asignar: ")

    # Buscar el curso seleccionado en la lista de cursos
    curso_seleccionado = None
    for curso in lista_cursos:
        if curso.get_codigo() == codigo_curso:
            curso_seleccionado = curso
            break
    
    if curso_seleccionado is None:
        print("Curso no encontrado.")
        return
    
    # Mostrar la lista de docentes disponibles
    print("Docentes disponibles:")
    for docente in lista_docente:
        print(f"{docente.get_dni()}: {docente.get_nombre()} {docente.get_ap_paterno()}")

    # Pedir al usuario que seleccione un docente
    dni_docente = input("Ingrese el DNI del docente al que desea asignar el curso: ")

    # Buscar el docente seleccionado en la lista de docentes
    docente_seleccionado = None
    for docente in lista_docente:
        if docente.get_dni() == dni_docente:
            docente_seleccionado = docente
            break
    
    if docente_seleccionado is None:
        print("Docente no encontrado.")
        return
    
    # Asignar el curso al docente
    curso_seleccionado.asignar_docente(docente_seleccionado)
    print(f"Curso {curso_seleccionado.get_nombre()} asignado al docente {docente_seleccionado.get_nombre()} {docente_seleccionado.get_ap_paterno()}.")
def actualizar_docente_curso():
    print("Actualización de docente en curso")

    # Mostrar la lista de cursos disponibles
    print("Cursos disponibles:")
    for curso in lista_cursos:
        print(f"{curso.get_codigo()}: {curso.get_nombre()}")

    # Pedir al usuario que seleccione un curso
    codigo_curso = input("Ingrese el código del curso que desea actualizar: ")

    # Buscar el curso seleccionado en la lista de cursos
    curso_seleccionado = None
    for curso in lista_cursos:
        if curso.get_codigo() == codigo_curso:
            curso_seleccionado = curso
            break

    if curso_seleccionado is None:
        print("Curso no encontrado.")
        return

    # Mostrar la lista de docentes disponibles
    print("Docentes disponibles:")
    for docente in lista_docente:
        print(f"{docente.get_dni()}: {docente.get_nombre()} {docente.get_ap_paterno()}")

    # Pedir al usuario que seleccione un docente
    dni_docente = input("Ingrese el DNI del nuevo docente para el curso: ")

    # Buscar el docente seleccionado en la lista de docentes
    docente_nuevo = None
    for docente in lista_docente:
        if docente.get_dni() == dni_docente:
            docente_nuevo = docente
            break

    if docente_nuevo is None:
        print("Docente no encontrado.")
        return

    # Actualizar el docente del curso
    curso_seleccionado.actualizar_docente(docente_nuevo)
    print(f"Docente del curso {curso_seleccionado.get_nombre()} actualizado a {docente_nuevo.get_nombre()} {docente_nuevo.get_ap_paterno()}.")
def registrar_nota():
    print("Registro de nota del alumno")
    for alumno in lista_alumnos:
        print(str(alumno) + "\n")

    # Mostrar la lista de alumnos
    print("Alumnos disponibles:")
    for alumno in lista_alumnos:
        print(f"{alumno.get_dni()}: {alumno.get_nombre()} {alumno.get_ap_paterno()}")

    # Pedir al usuario que seleccione un alumno
    dni_alumno = input("Ingrese el DNI del alumno para registrar la nota: ")

    # Buscar el alumno seleccionado en la lista de umnos
    alumno_seleccionado = None
    for alumno in lista_alumnos:
        if alumno.get_dni() == dni_alumno:
            alumno_seleccionado = alumno
            break

    if alumno_seleccionado is None:
        print("Alumno no encontrado.")
        return

    # Mostrar la lista de cursos en los que el alumno está inscrito
    cursos_inscritos = alumno_seleccionado.mostrar_cursos_inscritos()
    print(f"Cursos inscritos por el alumno {alumno_seleccionado.get_nombre()} {alumno_seleccionado.get_ap_paterno()}:")
    for curso in cursos_inscritos:
        print(curso)

    # Pedir al usuario que seleccione un curso
    codigo_curso = input("Ingrese el código del curso en el que desea registrar la nota: ")

    # Buscar el curso seleccionado en la lista de cursos
    curso_seleccionado = None
    for curso in lista_cursos:
        if curso.get_codigo() == codigo_curso:
            curso_seleccionado = curso
            break

    if curso_seleccionado is None:
        print("Curso no encontrado.")
        return

    # Pedir al usuario que ingrese la nota del alumno
    nota = float(input("Ingrese la nota del alumno: "))

    # Registrar la nota del alumno en el curso
    curso_seleccionado.registrar_nota(alumno_seleccionado, nota)
    print(f"Nota {nota} registrada para el alumno {alumno_seleccionado.get_nombre()} {alumno_seleccionado.get_ap_paterno()} en el curso {curso_seleccionado.get_nombre()}.")

def registrar_curso():
    print("lista de cursos:")
    for curso in lista_cursos:
        print(str(curso) + "\n")
    
    codigo = input("Ingrese el código del curso: ")
    nombre = input("Ingrese el nombre del curso: ")

    curso = (codigo, nombre)
    lista_cursos.append(curso)  # Agregar el curso a la lista global
    print("Curso registrado exitosamente:", curso)
    print("nueva lista de cursos:")
    for curso in lista_cursos:
        print(str(curso) + "\n")
    return curso

##DICCIONARIOS
opciones={
    '1':Alumno.registrar_alumno,
    '2':Docente.registrar_docente,
    '3':registrar_curso,
    '4':asignar_curso_docente,
    '5':actualizar_docente_curso,
    '6':registrar_nota,
    '9':exit
}

while True:
    print("Bienvenido al sistema de registro de alumnos")
    print("1. Registrar alumno")
    print("2. Registrar docente")
    print("3. Registrar curso")
    print("4. Asignar curso a docente")
    print("5. Actualizar docente a curso")
    print("6. Registrar nota del alumno")
    print("7. Mostrar reporte de alumnos")
    print("8. Mostrar reporte de docentes")
    print("9. Salir")

    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        break
print("Este programa funciona corectamente")
"""
    # Incluir los 5 registros por integrante
    for i in range(3):
        

        # Inscribir alumnos en los cursos correspondientes
        for curso in lista_cursos:
            inscripcion = input(f"¿Inscribir al alumno en el curso {curso.get_nombre()}? (s/n): ")
            if inscripcion.lower() == 's':
                alumno1.agregar_curso(curso)

        # Mostrar los cursos inscritos por el alumno
        cursos_inscritos = alumno1.mostrar_cursos_inscritos()
        print(f"Cursos inscritos por el alumno {alumno1.get_nombre()} {alumno1.get_ap_paterno()}:")
        for curso in cursos_inscritos:
            print(curso)

    lista_docente = []
    docente1 = Docente('nombre1', 'paterno', 'materno', 'dni', 'codigo', 'FIIS')
    docente2 = Docente('nombre2', 'paterno', 'materno', 'dni', 'codigo', 'FIIS')

    lista_docente.append(docente1)
    lista_docente.append(docente2)
    
    """


