from storage import JsonStorage
from models import Hotel, Customer, Reservation


class HotelService:
    def __init__(self):
        self.storage = JsonStorage("data/hotels.json")

    def create_hotel(self, hotel: Hotel):
        hotels = self.storage.load()
        hotels.append(hotel.__dict__)
        self.storage.save(hotels)

    def delete_hotel(self, hotel_id):
        hotels = self.storage.load()
        hotels = [h for h in hotels if h["hotel_id"] != hotel_id]
        self.storage.save(hotels)

    def get_hotel(self, hotel_id):
        hotels = self.storage.load()
        return next((h for h in hotels if h["hotel_id"] == hotel_id), None)

    def update_hotel(self, hotel_id, **kwargs):
        hotels = self.storage.load()
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                hotel.update(kwargs)
        self.storage.save(hotels)

    def reserve_room(self, hotel_id):
        hotels = self.storage.load()
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id and hotel["available_rooms"] > 0:
                hotel["available_rooms"] -= 1
        self.storage.save(hotels)

    def cancel_reservation(self, hotel_id):
        hotels = self.storage.load()
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                hotel["available_rooms"] += 1
        self.storage.save(hotels)


class CustomerService:
    def __init__(self):
        self.storage = JsonStorage("data/customers.json")

    def create_customer(self, customer: Customer):
        customers = self.storage.load()
        customers.append(customer.__dict__)
        self.storage.save(customers)

    def delete_customer(self, customer_id):
        customers = self.storage.load()
        customers = [c for c in customers if c["customer_id"] != customer_id]
        self.storage.save(customers)

    def get_customer(self, customer_id):
        customers = self.storage.load()
        return next((c for c in customers if c["customer_id"] == customer_id), None)

    def update_customer(self, customer_id, **kwargs):
        customers = self.storage.load()
        for customer in customers:
            if customer["customer_id"] == customer_id:
                customer.update(kwargs)
        self.storage.save(customers)


class ReservationService:
    def __init__(self):
        self.storage = JsonStorage("data/reservations.json")

    def create_reservation(self, reservation: Reservation):
        reservations = self.storage.load()
        reservations.append(reservation.__dict__)
        self.storage.save(reservations)

    def cancel_reservation(self, reservation_id):
        reservations = self.storage.load()
        reservations = [
            r for r in reservations if r["reservation_id"] != reservation_id
        ]
        self.storage.save(reservations)
