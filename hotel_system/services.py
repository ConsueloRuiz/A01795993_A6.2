# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
este modulo define los servicios para gestionar hoteles, clientes y reservas.
"""
from storage import JsonStorage
from models import Hotel, Customer, Reservation

class HotelService:
    """ Servicio para gestionar hoteles, incluyendo CRUD y reservas. """
    def __init__(self):
        """ Inicializa el servicio de hoteles con un almacenamiento JSON. """
        self.storage = JsonStorage("data/hotels.json")

    def create_hotel(self, hotel: Hotel):
        """ Crea un nuevo hotel y lo guarda en el almacenamiento. """
        hotels = self.storage.load()
        hotels.append(hotel.__dict__)
        self.storage.save(hotels)

    def delete_hotel(self, hotel_id):
        """ Elimina un hotel por su ID, actualizando el almacenamiento. """
        hotels = self.storage.load()
        hotels = [h for h in hotels if h["hotel_id"] != hotel_id]
        self.storage.save(hotels)

    def get_hotel(self, hotel_id):
        """ Obtiene un hotel por su ID, devolviendo su informacion o None si no existe. """
        hotels = self.storage.load()
        return next((h for h in hotels if h["hotel_id"] == hotel_id), None)

    def update_hotel(self, hotel_id, **kwargs):
        """ Actualiza la informacion de un hotel por su ID."""
        hotels = self.storage.load()
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                hotel.update(kwargs)
        self.storage.save(hotels)

    def reserve_room(self, hotel_id):
        """ Reserva una habitacion en un hotel por su ID, actualiza las habitaciones. """
        hotels = self.storage.load()
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id and hotel["available_rooms"] > 0:
                hotel["available_rooms"] -= 1
        self.storage.save(hotels)

    def cancel_reservation(self, hotel_id):
        """ Cancela una reserva en un hotel por su ID, actualiza las habitaciones. """
        hotels = self.storage.load()
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                hotel["available_rooms"] += 1
        self.storage.save(hotels)


class CustomerService:
    """ Servicio para gestionar clientes, incluyendo CRUD. """
    def __init__(self):
        """ Inicializa el servicio de clientes con un almacenamiento JSON. """
        self.storage = JsonStorage("data/customers.json")

    def create_customer(self, customer: Customer):
        """ Crea un nuevo cliente y lo guarda en el almacenamiento. """
        customers = self.storage.load()
        customers.append(customer.__dict__)
        self.storage.save(customers)

    def delete_customer(self, customer_id):
        """ Elimina un cliente por su ID, actualizando el almacenamiento. """
        customers = self.storage.load()
        customers = [c for c in customers if c["customer_id"] != customer_id]
        self.storage.save(customers)

    def get_customer(self, customer_id):
        """ Obtiene un cliente por su ID, devolviendo su informacion o None si no existe. """
        customers = self.storage.load()
        return next((c for c in customers if c["customer_id"] == customer_id), None)

    def update_customer(self, customer_id, **kwargs):
        """ Actualiza la informacion de un cliente por su ID, actualzia informacion """
        customers = self.storage.load()
        for customer in customers:
            if customer["customer_id"] == customer_id:
                customer.update(kwargs)
        self.storage.save(customers)


class ReservationService:
    """ Servicio para gestionar reservas, incluyendo creacion y cancelacion. """
    def __init__(self):
        """ Inicializa el servicio de reservas con un almacenamiento JSON. """
        self.storage = JsonStorage("data/reservations.json")

    def create_reservation(self, reservation: Reservation):
        """ Crea una nueva reserva y la guarda en el almacenamiento. """
        reservations = self.storage.load()
        reservations.append(reservation.__dict__)
        self.storage.save(reservations)

    def cancel_reservation(self, reservation_id):
        """ Cancela una reserva por su ID, eliminandola del almacenamiento. """
        reservations = self.storage.load()
        reservations = [
            r for r in reservations if r["reservation_id"] != reservation_id
        ]
        self.storage.save(reservations)
