class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.reservada = False

class Hotel:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, numero, tipo):
        self.habitaciones.append(Habitacion(numero, tipo))

    def reservar(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero and not habitacion.reservada:
                habitacion.reservada = True
                return f'Habitación {numero} reservada.'
        return 'Habitación no disponible.'

    def liberar(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero and habitacion.reservada:
                habitacion.reservada = False
                return f'Habitación {numero} liberada.'
        return 'Habitación no encontrada o ya libre.'

# Ejemplo de uso
hotel = Hotel()
hotel.agregar_habitacion(101, 'individual')
hotel.agregar_habitacion(102, 'doble')

print(hotel.reservar(101))  # Reserva habitación 101
print(hotel.liberar(101))   # Libera habitación 101
