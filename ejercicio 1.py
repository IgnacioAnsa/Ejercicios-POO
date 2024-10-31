# 1 -Clase para representar un Libro
# Crear una clase Libro que tenga las características título, autor y año de publicación. Del
# libro se debe poder obtener información, mostrando por mensaje todos sus datos. Se debe
# crear la clase e implementarla.

class Libro:
    
    def __init__ (self, título, autor, año_de_publicacion):
        
        self.título = título
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion

    def mostrar_informacion(self):

        print(f"título: {self.título}")
        print(f"autor: {self.autor}")
        print(f"año de publicacion: {self.año_de_publicacion}")

libro_uno = Libro("Orgullo y prejuicio", "Jane Austen", 1813)
libro_uno.mostrar_informacion()


