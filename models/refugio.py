from re import S



class Refugio:

    def __init__(self, nombre:str):
        self.nombre = nombre
        self.__mascotas = []
    
    def registrar_mascota(self, *mascota:str):
        self.__mascotas.append(mascota)
        return(f"{mascota} se registro exitosamente")


    def lista_disponibles(self):
        
        for mascota in self.__mascotas: 
            return print (f"las mascotas disponibles son {mascota}")
                     
    def asignar_mascota (self, nombre_mascota,adoptante):
            
        for mascota in self.__mascotas:
            if nombre_mascota in mascota:
                #falta cambiar el estado de la mascota
                return print(f"La macota {nombre_mascota} se puede adoptar")

            else: return print(f"La mascota: {nombre_mascota} no esta en el refugio")    






