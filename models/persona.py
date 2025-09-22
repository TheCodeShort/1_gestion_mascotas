from math import pi
from typing import Self


class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad

    def presentacion(self):
        return f"hola mi nombre es {self.nombre} y tengo {self.edad} años"

#esta clase ereda los atributos de persona
class Adoptante (Persona):
    def __init__(self, nombre: str, edad: int ):
        super().__init__(nombre, edad)
        self.mascota_adoptada = []
    
    def adoptar(self, mascota: str):
        self.mascota_adoptada.append(mascota)
        return f"{self.nombre} adoptó a {mascota}"



