class Curso:
    def __init__(self, nombre, docente):
        self.nombre = nombre
        self.docente = docente
        self.datos = []

    def calcular_promedio(self):
        suma = sum(self.datos)
        return suma / len(self.datos) if len(self.datos) > 0 else 0

    def ingresar_nota(self, nota):
        self.datos.append(nota)

    def reporte(self):
        print(f"Curso: {self.nombre}")
        print(f"Docente: {self.docente}")
        print(f"Promedio: {self.calcular_promedio()}")

class Persona:
    def __init__(self, dni, apellidos, nombres, nacionalidad):
        self.dni = dni
        self.apellidos = apellidos
        self.nombres = nombres
        self.nacionalidad = nacionalidad

    def cambiarNombre(self, nuevo_nombre):
        self.nombres = nuevo_nombre

    def cambiarApellidos(self, nuevo_apellido):
        self.apellidos = nuevo_apellido

    def to_string(self):
        print(f"Dni: {self.dni}, Apellidos: {self.apellidos}, Nombres: {self.nombres}, Nacionalidad: {self.nacionalidad}")

class Alumno(Persona):
    def __init__(self, dni, apellidos, nombres, nacionalidad, edad, anoIngreso, anoestudio):
        super().__init__(dni, apellidos, nombres, nacionalidad)
        self.anoIngreso = anoIngreso
        self.anoestudio = anoestudio
        self.edad = edad

alumnos_array = []

for i in range(15):
    dni = f"Dni {i}"
    nombre = "Nombre " + str(i)
    alumno = Alumno(dni, "Apellido", nombre, "Nacionalidad", 20, 2021, 344)
    alumnos_array.append(alumno)

def imprimir_informacion_alumnos(alumnos):
    for alumno in alumnos:
        print("-" * 30)
        alumno.to_string()
        print(f"Edad: {alumno.edad}")
        print(f"Año de Ingreso: {alumno.anoIngreso}")
        print(f"Año de Estudio: {alumno.anoestudio}")
        print("-" * 30)

imprimir_informacion_alumnos(alumnos_array)
