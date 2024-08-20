"""Ejercicio 4 - Wesly Umanzor"""
class Electronicos:
    def __init__(self, categoria, modelo, tamaño_pantalla, capacidad_almacenamiento, cpu, memoria_ram, costo_adquisicion):
        self.categoria = categoria
        self.fabricante = "PHR"  
        self.modelo = modelo
        self.tamaño_pantalla = tamaño_pantalla
        self.capacidad_almacenamiento = capacidad_almacenamiento
        self.cpu = cpu
        self.memoria_ram = memoria_ram
        self.costo_adquisicion = costo_adquisicion
        self.precio_final = self._determinar_precio_final()
        self.procedencia = "Importado" 

    def _determinar_precio_final(self):
        return self.costo_adquisicion * 1.7

    def desplegar_informacion(self):
        print(f"\nCategoría: {self.categoria}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Modelo: {self.modelo}")
        print(f"Tamaño de Pantalla: {self.tamaño_pantalla} pulgadas")
        print(f"Almacenamiento: {self.capacidad_almacenamiento} GB")
        print(f"Procesador: {self.cpu}")
        print(f"RAM: {self.memoria_ram} GB")
        print(f"Costo de Adquisición: ${self.costo_adquisicion:.2f}")
        print(f"Precio Final: ${self.precio_final:.2f}")
        print(f"Procedencia: {self.procedencia}")

def generar_electronicos():
    electronicos = [
        Electronicos("Smartphone", "X1", 6.5, 128, "Snapdragon 888", 8, 300.0),
        Electronicos("Tableta", "Samsung Galaxy Tab S9", 11, 128, "Qualcomm Snapdragon 8 Gen 2", 8, 480.0),
        Electronicos("Laptop", "ASUS ROG Zephyrus G14", 15.6, 512, "Ryzen 7", 16, 1000.0)
    ]
    return electronicos

def mostrar_electronicos(electronicos):
    for dispositivo in electronicos:
        dispositivo.desplegar_informacion()

if __name__ == "__main__":
    electronicos = generar_electronicos()
    mostrar_electronicos(electronicos)