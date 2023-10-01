from alumno import Alumno
from docente import Docente
from cursos import Curso

##LISTA DE CURSOS
lista_cursos = []
# Crear instancias de cursos
curso_algebra = Curso('C001', 'Algebra')
curso_matematica = Curso('C002', 'Matematica')
curso_filosofia = Curso('C003', 'Filosofia')

lista_cursos.append(curso_algebra)
lista_cursos.append(curso_matematica)
lista_cursos.append(curso_filosofia)

lista_alumnos = []
# Incluir los 5 registros por integrante
for i in range(3):
    alumno1 = Alumno('nombre', 'apellido 1', 'apellido 2', 'dni','codigo', 'Informatica y Sistemas', 2023)
    lista_alumnos.append(alumno1)

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

print("Este programa funciona correctamente")
input("Presiona Enter para salir...")
