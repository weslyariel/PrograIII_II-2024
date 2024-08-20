"""Ejercicio 3 - Wesly Umanzor"""

class Vehiculo:
    def __init__(self, fabricante, modelo, año_fabricacion, color_exterior, motor, 
                 combustible, recorrido, costo_inicial, 
                 procedencia, tipo_transmision):

        self.fabricante = fabricante
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion
        self.color_exterior = color_exterior
        self.motor = motor
        self.combustible = combustible
        self.recorrido = recorrido
        self.costo_inicial = costo_inicial
        self.procedencia = procedencia  
        self.tipo_transmision = tipo_transmision  
        self.precio_mercado = self.determinar_precio_mercado()
        self.numero_ruedas = 4
        self.capacidad_asientos = 5

    def determinar_precio_mercado(self):
        return self.costo_inicial * 1.4

    def desplegar_informacion(self):
        print(f"\nFabricante: {self.fabricante}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año_fabricacion}")
        print(f"Color Exterior: {self.color_exterior}")
        print(f"Motor: {self.motor}")
        print(f"Combustible: {self.combustible}")
        print(f"Kilometraje: {self.recorrido} km")
        print(f"Transmisión: {self.tipo_transmision}")
        print(f"Procedencia: {self.procedencia}")
        print(f"Costo Inicial: ${self.costo_inicial:.2f}")
        print(f"Precio de Mercado: ${self.precio_mercado:.2f}")
        print(f"Número de Ruedas: {self.numero_ruedas}")
        print(f"Asientos Disponibles: {self.capacidad_asientos}")
        print("---------------------------------------------------")
        print()


vehiculo1 = Vehiculo(
    fabricante="Ford",
    modelo="Mustang",
    año_fabricacion=2023,
    color_exterior="Rojo",
    motor="2.3L Turbo",
    combustible="Gasolina",
    recorrido=0,
    costo_inicial=130000.0,
    procedencia="Nacional",
    tipo_transmision="Automática"
)

vehiculo2 = Vehiculo(
    fabricante="Honda",
    modelo="Civic",
    año_fabricacion=2030,
    color_exterior="Azul",
    motor="2.0L",
    combustible="Gasolina",
    recorrido=0,
    costo_inicial=310000.0,
    procedencia="Importado",
    tipo_transmision="Manual"
)

vehiculo3 = Vehiculo(
    fabricante="Chevrolet",
    modelo="Malibu",
    año_fabricacion=2028,
    color_exterior="Negro",
    motor="1.5L Turbo",
    combustible="Gasolina",
    recorrido=0,
    costo_inicial=100000.0,
    procedencia="Nacional",
    tipo_transmision="Automática" 
)


print("\n****INFORMACIÓN DE LOS VEHÍCULOS****")
vehiculo1.desplegar_informacion()
vehiculo2.desplegar_informacion()
vehiculo3.desplegar_informacion()