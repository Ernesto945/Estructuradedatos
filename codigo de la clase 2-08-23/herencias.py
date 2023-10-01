tipo_especie= " "
nombre_cientifico = " "
class Animal:
    def _init_(self):
        self.tipo_especie = "ninguna"
        self.nonbre_cientifico = nombre_cientifico

    def saludar (self, saludo):
        return print(saludo)

class Perro(Animal):
    def ladrar(self): 
        return"ladrar"
class Gato(Animal):
    def hacer_sonido(self):
        return "maullar"
mi_gato = Gato('gato', 'felino' , 'copito')
mi_perro = Perro('Perro', 'Canino', 'Firulay')

print( mi_gato.numbre + ': '+ mi_gato.hacer_sonido())
print(mi_perro.nombre + ':' +mi_perro.ladrar())