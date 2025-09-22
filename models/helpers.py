from models.refugio import Refugio


def buscar_mascota (nombre_mascota:str, lista_mascota:list):
    
    for mascota in lista_mascota:
        if nombre_mascota in mascota: 
            print (f"La mascota {nombre_mascota} si existe")

        else:return "esta mascota no existe"    

buscar_mascota("pedro", Refugio.lista_disponibles())