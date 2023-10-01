class Persona:
    def __init__(self):
        self.dni = 0
        self.apellidos = "apellidos"
        self.nombres = "nombres"
        self.nacionalidad = "nacionalidad"
    
    def cambiarNombre(self, nuevo_nombre):
        self.nombres = nuevo_nombre

    def cambiarApellidos(self, nuevo_apellido):
        self.apellidos = nuevo_apellido

    def to_string(self):
        print(f"Dni: {self.dni}, Apellidos: {self.apellidos}, Nombres: {self.nombres}, Nacionalidad: {self.nacionalidad}")

class Alumnos(Persona):
    def __init__(self, dni, apellidos, nombres, nacionalidad, edad, anoIngreso, anoestudio):
        super().__init__()
        self.dni = dni
        self.apellidos = apellidos
        self.nombres = nombres
        self.nacionalidad = nacionalidad
        self.edad = edad
        self.anoIngreso = anoIngreso
        self.anoestudio = anoestudio

alumnos_array = []

for i in range(15):
    dni = f"Dni {i}"
    nombre = f"Nombre {i}"
    alumno = Alumnos(dni, "Apellido", nombre, "Nacionalidad", 20, 2021, 344)
    alumnos_array.append(alumno)

for alumno in alumnos_array:
    alumno.to_string()