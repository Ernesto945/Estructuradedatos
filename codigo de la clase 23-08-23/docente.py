from persona import Persona

class Docente(Persona):
    codigo_docente = ''
    facultad = ''
    
    def __init__(self, nombre, ap_paterno, ap_materno, dni, codigo, facultad):
        super().__init__(nombre, ap_paterno, ap_materno, dni)
        self.codigo_docente = codigo
        self.facultad = facultad

    def get_codigo(self):
        return self.codigo_docente

    def set_codigo(self, codigo):
        self.codigo_docente = codigo

    def get_facultad(self):
        return self.facultad

    def set_facultad(self, facultad):
        self.facultad = facultad
        
    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre} {self.ap_paterno} {self.ap_materno}"

    def imprimir(self):
        per_data = super().imprimir()
        codigo = self.codigo_docente
        facultad = self.facultad
        año = self.año_ingreso
        return f'datos del docente es : {per_data}, codigo de ingreso {codigo}, {facultad=}'
    @classmethod
    def registrar_docente(cls):
            nombre = input("Ingrese el nombre del docente: ")
            ap_paterno = input("Ingrese el apellido paterno: ")
            ap_materno = input("Ingrese el apellido materno: ")
            dni = input("Ingrese el DNI del docente: ")
            codigo = input("Ingrese el código del docente: ")
            departamento = input("Ingrese el departamento del docente: ")

            docente = cls(nombre, ap_paterno, ap_materno, dni, codigo, departamento)
            print("Docente registrado exitosamente:", docente)
            return docente