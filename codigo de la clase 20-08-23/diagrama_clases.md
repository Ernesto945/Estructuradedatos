#   Diagrama de clases
``` mermaid
classDiagram
    Persona <|-- Docente:Herencia
    Persona <|-- Alumno:herencia
    Docente <-- Curso:Aciociativa
    
    class Persona{
      -private int id
      -private string nombre
      -private string apellido
      -private string  dni
      -private string dirección
      -private date fecha_nacimiento
      +pulic Persona()
      +public Persona(nombre,apellido,dni,dirección)
      +public string get_nombre()
      +public void  set_nombre(nuevo_nombre)
      +public string get_apellidos()
      +public void  set_apellidos(nuevo_apellido)
      +public string get_dni()
      +public void set_dni()
      +public string mostrar_datos()

    }
    class Docente{
      -private  string codigo_docente
      -private  string facultad
      +Docente(nombre,apellido,dni,dirección,codigo,facultad)
      +public string get_codigo
      +public void set_codigo(nuevo_codigo)
      +public string get_facultad
      public void imprimir()
    }
    class Alumno{
      - private int id_alumno
      - private string codigo_alumno
      - private string facultad
      - private int ano_ingreso
      +Alumno(nombre,apellido,dni,dirección,codigo_alumno,facultad):Persona(nombre,apellido,dni,dirección)
      +public string get_codigo_alumno()
      +public void set_codigo_alumno(nuevo_codigo)
      +public void registrar_curso(curso)
      +public void ingresar_notas(curso)
      +public string eliminar_curso(curso)
      +public string mostrar_datos()
    }

    class Curso{
        -private string codigo
        -private string nombre_curso
        -private float   notas[]
        -private Docente  Docente
        +Curso(codigo,nombre_curso)
        +public void set_codigoCurso(codigo)
        +public string get_codigoCurso()
        +pulic string get_nombre_curso()
        +public void set_nombre_curso(nombre)
        +public void calcular_promedio(notas)
        +public void ingresar_notas()
        +public void asignar_docente()
        +public void reporte()
        +public void set_docente(docente)
        +public docente get_docente()
    }

    class Main{
        +ingresar_alumno(alumno)
        +ingresar_docentes(docentes)
        +ingresar_cursos(cursos)
        +Curso.ingresar_notas()
        +operaciones()
        +guardar()
        +imprimir()    
        
        }
