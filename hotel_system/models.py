# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
este modulo define las clases de datos para el sistema de reservas de hoteles.
"""

from dataclasses import dataclass

@dataclass
class Hotel:
    """ Clase que representa un hotel con su informacion basica. """
    hotel_id: str
    name: str
    total_rooms: int
    available_rooms: int


@dataclass
class Customer:
    """ Clase que representa un cliente con su informacion basica. """
    customer_id: str
    name: str
    email: str


@dataclass
class Reservation:
    """ Clase que representa una reserva con su informacion basica. """
    reservation_id: str
    hotel_id: str
    customer_id: str
