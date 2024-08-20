"""Ejercicio 1 - Wesly Umanzor"""

class Perro:
    def __init__(self, color, raza, nombre, años, peso, alergias):
        self.color = color
        self.raza = raza
        self.nombre = nombre
        self.años = años
        self.peso = peso
        self.alergias = alergias
        self.estado = "NO ATENDIDO"
        self.tipo_perro = "Perro Grande" if peso >= 10 else "Perro Pequeño"

    def registroPerro(self):
        self.estado = "ATENDIDO"
        self.información_perro()

    def información_perro(self):
        print("\nInformación del Perro:")
        print("****************************************")
        print(f"Nombre : {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.años} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Alergias: {self.alergias}")
        print(f"Estado: {self.estado}")
        print(f"Tipo: {self.tipo_perro}")

print("***************************************************")
nombre = input("Por favor ingresa el nombre del canino: ")
raza = input("Por favor ingresa la raza del canino: ")
años = int(input("Por favor ingrese la edad/años que tiene el perro: "))
peso = float(input("Por favor ingresa el peso en kg del perro: "))
color = input("Por favor ingrese el color del perro: ")
alergias = input("El canino tiene alergias (S/N)? ")

perro1 = Perro(color, raza, nombre, años, peso, alergias)
perro1.registroPerro()