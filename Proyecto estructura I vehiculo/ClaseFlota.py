from ClaseVehiculo import Vehiculo
from ClaseMantenimieto import Mantenimientos
from ClaseNodo import NodoMantenimiento
from ClaseNodo import NodoVehiculo

lista_vehiculos = Vehiculo()

while True:
    print("MENU\n1. Registrar un nuevo vehículo.\n2. Eliminar un vehículo por su placa\n3. Buscar un vehículo por su placa y mostrar su información\n4. Listar todos los vehículos registrados\n5. Salir")
    opcion = input("Ingrese la opción a ejecutar: ")
    
    if opcion == "5":
        print("Saliendo del programa...")
        break
    elif opcion == "1":
        print("Registrar un nuevo vehículo\n___________________________")
        placa = input("Ingrese la placa del vehículo: ")
        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        anio = input("Ingrese el año del vehículo (en números): ")
        kilometraje = input("Ingrese el kilometraje del vehículo (en números): ")

        historial = Mantenimientos()
        while True:
            agregar_mantenimiento = input("Desea agregar un mantenimiento? (SI/NO): ").strip().lower()
            if agregar_mantenimiento == "si":
                fecha = input("Ingrese la fecha de mantenimiento (YYYY-MM-DD): ")
                descripcion = input("Ingrese la descripción del mantenimiento: ")
                costo = input("Ingrese el costo del mantenimiento: ")
                historial.agregar_mantenimiento(fecha, descripcion, costo)
            else:
                break
        lista_vehiculos.agregar_vehiculo(placa, marca, modelo, anio, kilometraje, historial)
        print("Vehículo registrado exitosamente.")
    elif opcion == "2":
        print("Eliminar un vehículo por su placa\n_______________________________")
        placa = input("Ingrese la placa del vehículo: ")
        if lista_vehiculos.eliminar_vehiculo(placa):
            print("Vehículo eliminado con éxito.")
        else:
            print("Vehículo no encontrado.")
    elif opcion == "3":
        print("Buscar vehículo por su placa y mostrar su información\n__________________________________________________________")
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo = lista_vehiculos.buscar_vehiculo(placa)
        if vehiculo:
            print(vars(vehiculo))
        else:
            print("Vehículo no encontrado.")
    elif opcion == "4":
        print("Mostrar todos los vehículos registrados y sus mantenimientos\n_______________________________________________________")
        vehiculos = lista_vehiculos.listar_vehiculos()
        if vehiculos:
            for vehiculo_data in vehiculos:
                vehiculo_args = {k: v for k, v in vehiculo_data.items() if k in NodoVehiculo.__init__.__code__.co_varnames}
                vehiculo = NodoVehiculo(**vehiculo_args)
                print(f"Placa: {vehiculo.placa}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}, Kilometraje: {vehiculo.kilometraje}")
                if vehiculo.historial and vehiculo.historial.cabeza:
                    print("  Historial de Mantenimientos:")
                    for mantenimiento_data in vehiculo.historial.listar_mantenimientos():
                        mantenimiento_args = {k: v for k, v in mantenimiento_data.items() if k in NodoMantenimiento.__init__.__code__.co_varnames}
                        mantenimiento = NodoMantenimiento(**mantenimiento_args)
                        print(f"    - Fecha: {mantenimiento.fecha}, Descripción: {mantenimiento.descripcion}, Costo: {mantenimiento.costo}")
                else:
                    print("  No hay mantenimientos registrados.")
        else:
            print("No hay vehículos registrados.")
    else:
        print("Opción incorrecta, intentelo de nuevo.")







