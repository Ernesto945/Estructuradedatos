# Diagrama de secuencia
``` mermaid
sequenceDiagram
    participant Main
    participant Alumno
    participant Docente
    participant Curso
    activate Main

    Main ->> Alumno: Registrar alumno
    

    Main ->> Docente: Registrar docente
    Main -->> Curso : Registrar Curso
    
    Main ->>Curso: Ingresar notas
    Main ->> Docente: Imprimir docente
    Main ->>Curso: Calcular promedio
    Main -->>Main: Imprimir Reporte
    deactivate Main
