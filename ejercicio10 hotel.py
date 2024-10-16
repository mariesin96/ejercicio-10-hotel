class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.reservada = False
        self.huesped = None

    # Método para reservar la habitación
    def reservar(self, huesped):
        if not self.reservada:
            self.reservada = True
            self.huesped = huesped
            print(f"La habitación {self.numero} ha sido reservada por {huesped.nombre}.")
        else:
            print(f"La habitación {self.numero} ya está reservada.")

    # Método para liberar la habitación
    def liberar(self):
        if self.reservada:
            print(f"La habitación {self.numero} ha sido liberada por {self.huesped.nombre}.")
            self.reservada = False
            self.huesped = None
        else:
            print(f"La habitación {self.numero} ya está disponible.")

    # Método para mostrar el estado de la habitación
    def __str__(self):
        estado = "reservada" if self.reservada else "disponible"
        return f"Habitación {self.numero} ({self.tipo}) - Estado: {estado}"


# Clase para representar un Huésped
class Huesped:
    def __init__(self, nombre):
        self.nombre = nombre


# Clase para representar el Hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    # Método para agregar una habitación al hotel
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        print(f"Habitación {habitacion.numero} ({habitacion.tipo}) agregada al hotel {self.nombre}.")

    # Método para mostrar las habitaciones disponibles
    def mostrar_habitaciones_disponibles(self):
        print("Habitaciones disponibles:")
        disponibles = [hab for hab in self.habitaciones if not hab.reservada]
        if disponibles:
            for habitacion in disponibles:
                print(f"- {habitacion}")
        else:
            print("No hay habitaciones disponibles.")

    # Método para reservar una habitación por número
    def reservar_habitacion(self, numero_habitacion, huesped):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                habitacion.reservar(huesped)
                return
        print(f"No se encontró habitación con número {numero_habitacion}.")

    # Método para liberar una habitación por número
    def liberar_habitacion(self, numero_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                habitacion.liberar()
                return
        print(f"No se encontró habitación con número {numero_habitacion}.")


if __name__ == "__main__":
    # Crear un hotel
    hotel = Hotel("Hotel Paraíso")

    # Crear habitaciones y agregarlas al hotel
    habitacion1 = Habitacion(101, "individual")
    habitacion2 = Habitacion(102, "doble")
    habitacion3 = Habitacion(103, "individual")

    hotel.agregar_habitacion(habitacion1)
    hotel.agregar_habitacion(habitacion2)
    hotel.agregar_habitacion(habitacion3)

    # Crear huéspedes
    huesped1 = Huesped("Juan Pérez")
    huesped2 = Huesped("María Gómez")

    # Mostrar habitaciones disponibles
    hotel.mostrar_habitaciones_disponibles()

    # Reservar una habitación
    hotel.reservar_habitacion(101, huesped1)

    # Intentar reservar una habitación ya reservada
    hotel.reservar_habitacion(101, huesped2)

    # Mostrar habitaciones disponibles después de la reserva
    hotel.mostrar_habitaciones_disponibles()

    # Liberar una habitación
    hotel.liberar_habitacion(101)

    # Mostrar habitaciones disponibles después de liberar
    hotel.mostrar_habitaciones_disponibles()