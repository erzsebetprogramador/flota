from datetime import datetime
from ClaseNodo import Nodovehiculo
from ClaseMantenimieto import Mantenimientos
class Vehiculo:
    def __init__(self):
        self.cabeza = None
        self.final = None
        self.contador = 0

    def validar_anio(self, anio):
        if anio.isdigit():
            anio = int(anio)
            if 1886 <= anio <= datetime.now().year:
                return anio
            else:
                raise ValueError(f"Ingrese un año entre 1886 y {datetime.now().year}.")
        else:
            raise ValueError("El año debe ser un número válido.")

    def validar_kilometraje(self, kilometraje):
        try:
            kilometraje = int(kilometraje)
            if kilometraje < 0:
                raise ValueError("El kilometraje no puede ser negativo.")
            return kilometraje
        except ValueError:
            raise ValueError("Kilometraje inválido, ingrese solo números.")

    def agregar_vehiculo(self, placa, marca, modelo, anio, kilometraje, historial=None):
        anio = self.validar_anio(str(anio))
        kilometraje = self.validar_kilometraje(kilometraje)
        if historial is None:
            historial = Mantenimientos()  
        nuevo_nodo = Nodovehiculo(placa, marca, modelo, anio, kilometraje, historial)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.final = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.contador += 1

    def eliminar_vehiculo(self, placa):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.placa == placa:
                if anterior:
                    anterior.siguiente = actual.siguiente
                    if actual == self.final:
                        self.final = anterior
                else:
                    self.cabeza = actual.siguiente
                self.contador -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar_vehiculo(self, placa):
        actual = self.cabeza
        while actual:
            if actual.placa == placa:
                return actual
            actual = actual.siguiente
        return None

    def listar_vehiculos(self):
        vehiculos = []
        actual = self.cabeza
        while actual:
            vehiculos.append(vars(actual))
            actual = actual.siguiente
        return vehiculos


