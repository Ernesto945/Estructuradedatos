from persona import Persona
from cursos import Curso

class Alumno(Persona):
    codigo = ''
    facultad = ''
    año_ingreso = 0

    def __init__(self, nombre, ap_paterno, ap_materno, dni, codigo, facultad, año_ingreso):
        super().__init__(nombre, ap_paterno, ap_materno, dni)
        self.codigo = codigo
        self.facultad = facultad
        self.año_ingreso = año_ingreso
        self.cursos_inscritos= []

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_facultad(self):
        return self.facultad

    def set_facultad(self, facultad):
        self.facultad = facultad

    def get_anio_ingreso(self):
        return self.año_ingreso

    def set_anio_ingreso(self, anio):
        self.año_ingreso = anio
    #Funcion para imprimir los datos del alumno
    def imprimir(self):
        per_data = super().imprimir()
        codigo = self.codigo
        facultad = self.facultad
        año = self.año_ingreso
        return f'datos del alumno es : {per_data}, codigo de ingreso {codigo}, {facultad=}, el año de ingreso es: {año}'
    
    ###FUNCION PARA REGISTRAR ALUMNO 
    @classmethod
    def registrar_alumno(cls): #se usa para hacer referencia a la instancia actual de la clase en los métodos de instancia.
        nombre = input("Ingrese el nombre del alumno: ")
        ap_paterno = input("Ingrese el apellido paterno: ")
        ap_materno = input("Ingrese el apellido materno: ")
        dni = input("Ingrese el DNI del alumno: ")
        codigo = input("Ingrese el código del alumno: ")
        facultad = input("Ingrese la facultad del alumno: ")
        año_ingreso = int(input("Ingrese el año de ingreso del alumno: "))

        alumno = Alumno(nombre, ap_paterno, ap_materno, dni, codigo, facultad, año_ingreso)
        return alumno
    
    
#Funcion para agregar cursos
    def agregar_curso(self, curso):
        self.cursos_inscritos.append(curso)
#Funcion para eliminar cursos

    def remover_curso(self, curso_eliminar):
        for curso in self.cursos_inscritos:
            if curso_eliminar.get_codigo() == curso.get_codigo():
                self.cursos_inscritos.remove(curso)
            else:
                print('No se encuentra registrado el curso a eliminar')
                
#Muestra los cursos que el alumno se inscrito
    def mostrar_cursos_inscritos(self): 
        return [curso.get_nombre() for curso in self.cursos_inscritos]
    
    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre} {self.ap_paterno} {self.ap_materno}"
    
    def ingresar_nota(self, curso, nota):
        curso.ingresar_nota(nota)
        print(f"Nota {nota} registrada para el alumno {self.nombre} {self.ap_paterno} en el curso {curso.get_nombre()}.")              

# Mostramos los cursos en la lista
"""for curso in Curso.lista_cursos:
    print(curso.nombre)"""
"""Curso = Curso
        nuevo_curso = input("ingrese nuevo curso")
        curso_nuevo = Curso(nuevo_curso)
        curso.curso.append(curso_nuevo) 
        agregarCursos()"""

