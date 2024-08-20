"""Ejercicio 2 - Wesly Umanzor"""

class TiendaPapeleria:
    def __init__(self, categoria, detalle, costo_adquisicion):
        self.categoria = categoria
        self.detalle = detalle
        self.costo_adquisicion = costo_adquisicion
        self.fabricante = "HOJITAS" if categoria == "cuaderno" else "RAYAS"
        self.precio_al_publico = self.costo_adquisicion * 1.30

    def desplegar_detalles(self):
        print(f"Categoría: {self.categoria}")
        print(f"Detalle: {self.detalle}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Costo de Adquisición: ${self.costo_adquisicion:.2f}")
        print(f"Precio al Público: ${self.precio_al_publico:.2f}")
        print("----------------------------------------------------")


articulo1 = TiendaPapeleria("cuaderno", "50 hojas", 0.65)
articulo2 = TiendaPapeleria("cuaderno", "100 hojas", 1.10)


articulo3 = TiendaPapeleria("lapiz", "Grafito", 0.25)
articulo4 = TiendaPapeleria("lapiz", "Colores", 0.40)


print("\nITEMS--CUADERNOS")
print("******************************")
articulo1.desplegar_detalles()
articulo2.desplegar_detalles()

print("\nITEMS--LÁPICES")
print("**********************************")
articulo3.desplegar_detalles()
articulo4.desplegar_detalles()