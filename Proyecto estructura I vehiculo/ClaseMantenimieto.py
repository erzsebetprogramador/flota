from datetime import datetime
from ClaseNodo import Nodomantenimientos

class Mantenimientos:
    def __init__(self):
        self.cabeza = None
        self.final = None
        self.contador = 0

    def validar_fecha(self, fecha):
        try:
            return datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")
    
    def validar_costo(self, costo):
        try:
            costo = float(costo)
            if costo < 0:
                raise ValueError("El costo debe ser un número positivo")
            return costo
        except ValueError:
            raise ValueError("El costo debe ser un número válido")

    def agregar_mantenimiento(self, fecha, descripcion, costo):
        fecha = self.validar_fecha(fecha)
        costo = self.validar_costo(costo)
        nuevo_mantenimiento = Nodomantenimientos(fecha, descripcion, costo)

        if not self.cabeza:
            self.cabeza = nuevo_mantenimiento
            self.final = nuevo_mantenimiento
        else:
            self.final.siguiente = nuevo_mantenimiento
            nuevo_mantenimiento.anterior = self.final
            self.final = nuevo_mantenimiento
        self.contador += 1

    def eliminar_mantenimiento(self, fecha):
        actual = self.cabeza
        while actual:
            if actual.fecha == fecha:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                if actual == self.final:
                    self.final = actual.anterior
                self.contador -= 1
                return True
            actual = actual.siguiente
        return False

    def listar_mantenimientos(self):
        mantenimientos = []
        actual = self.cabeza
        while actual:
            mantenimientos.append(vars(actual))
            actual = actual.siguiente
        return mantenimientos
