from dataclasses import dataclass


@dataclass
class Hotel:
    hotel_id: str
    name: str
    total_rooms: int
    available_rooms: int


@dataclass
class Customer:
    customer_id: str
    name: str
    email: str


@dataclass
class Reservation:
    reservation_id: str
    hotel_id: str
    customer_id: str
