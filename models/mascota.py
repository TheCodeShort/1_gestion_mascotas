from typing import Self


class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int , adoptado: bool = False):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.adoptado = adoptado
    
    #metodo donde se define como va a mostrar el mensaje por defecto 
    def __str__(self):

        estado = "adoptado" if self.adoptado else "disponible"
        return f"informacion de las mascota: nombre: {self.nombre}, especie: {self.especie}, edad: {self.edad} años, estado: {estado}"
        


