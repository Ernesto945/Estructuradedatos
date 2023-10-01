"""Crear una clase persona con DNI Apellidos Nombres
Nacionalidad
definir el constructor
con las funciones
cambiar nombre()
cambiar apellido()
to_string() imprimir todos los datos
clases hijo Alumnos
edad
año de ingreso
años de estudio

array de 15 alumnos"""
class Persona:
    def _init_(self,dni,apellidos,nombres,nacionalidad):
        self.dni = dni
        self.apellidos = apellidos
        self.nombres = nombres
        self.nacionalidad = nacionalidad

    def cambiarNombre(self,nuevo_nombre):
        self.nombres = nuevo_nombre

    def cambiarApellidos(self, nuevo_apellido):
        self.apellidos = nuevo_apellido

    def to_string(self):
        print(f"Dni: {self.dni}, Apellidos: {self.apellidos},Nombres: { self.nombres}, Nacionalidad{self.nacionalidad}")


        
class Alumnos(Persona):
    def _init_(self,dni,apellidos, nombres,nacionalidad,edad, anoIngreso,anoestudio):
        super()._init_(dni,apellidos,nombres,nacionalidad)
        self.anoIngreso = anoIngreso
        self.anoestudio = anoestudio
        self.edad = edad
alumnosaray = []

for i in range(15):
    dni = f"Dni {i}"
    nombre = "Nombre " + str(i)
    alumno = Alumnos(dni , "Apellido",nombre,"Nacionalidad",20,2021,344)
    alumnosaray.appened(alumno)

for alumno in alumnosaray:
    alumno.to_string()

    


