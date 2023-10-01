class Persona:
    def _init_(self, DNI, Apellidos, Nombres, Nacionalidad):
        self.DNI = DNI
        self.Apellidos = Apellidos
        self.Nombres = Nombres
        self.Nacionalidad = Nacionalidad
    
    def cambiar_nombre(self, nuevo_nombre):
        self.Nombres = nuevo_nombre

    def cambiar_apellido(self, nuevo_apellido):
        self.Apellidos = nuevo_apellido
    
    def _to_string(self):
        return f'DNI: {self.DNI}\nApellidos: {self.Apellidos}\nNombres: {self.Nombres}\nNacionalidad: {self.Nacionalidad}'

class Alumno(Persona):
    def _init_(self, DNI, Apellidos, Nombres, Nacionalidad, edad, Año_ingreso):
        super()._init_(DNI, Apellidos, Nombres, Nacionalidad)
        self.edad = edad
        self.Año_ingreso = Año_ingreso
    
    def Años_estudio(self):
        return 2023 - int(self.Año_ingreso)

class Curso(Persona):
    def _init_(self, DNI, Apellidos, Nombres, Nacionalidad, docente):
        super()._init_(DNI, Apellidos, Nombres, Nacionalidad)
        self.docente = docente
        self.notas = []

    def AgregarNota(self, nota):
        self.notas.append(nota)

    def CalcularPromedio(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0.0

alumnos = []

# Solicitar información de los alumnos

cursos = []

for i in range(2):
    print(f"CURSO {i + 1}:")
    DNI = input("DNI del docente: ")
    apellidos = input("Apellidos del docente: ")
    nombres = input("Nombres del docente: ")
    nacionalidad = input("Nacionalidad del docente: ") 
    
    curso = Curso(DNI, apellidos, nombres, nacionalidad, docente=True)
    cursos.append(curso)

for curso in cursos:
    print(f"Notas del curso dictado por {curso.Nombres} {curso.Apellidos}:")
    for i in range(1):
        dni_alumno = input(f"Ingrese DNI del alumno {i + 1}: ")
        apellidos_alumno = input(f"Ingrese apellidos del alumno {i + 1}: ")
        nombres_alumno = input(f"Ingrese nombres del alumno {i + 1}: ")
        nacionalidad_alumno = input(f"Ingrese nacionalidad del alumno {i + 1}: ")
        edad_alumno = input(f"Ingrese edad del alumno {i + 1}: ")
        año_ingreso_alumno = input(f"Ingrese año de ingreso del alumno {i + 1}: ")
        
        alumnos.append(Alumno(dni_alumno, apellidos_alumno, nombres_alumno, nacionalidad_alumno, edad_alumno, año_ingreso_alumno))

        notas = []
        for j in range(4):
            nota = float(input(f"Ingrese la nota {j + 1} del alumno {i + 1}: "))
            notas.append(nota)
        curso.AgregarNota(sum(notas) / 4)
    print(f"Promedio del curso: {curso.CalcularPromedio()}\n")