from datetime import datetime

class NodoVehiculo:
    def __init__(self, placa, marca, modelo, anio, kilometraje, historial=None):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.historial = historial
        self.siguiente = None

class NodoMantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo
        self.siguiente = None
        self.anterior = None