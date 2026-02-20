import unittest
from services import ReservationService
from models import Reservation


class TestReservationService(unittest.TestCase):
    def setUp(self):
        self.service = ReservationService()
        self.service.storage.save([])

    def test_create_and_cancel_reservation(self):
        reservation = Reservation("R1", "H1", "C1")
        self.service.create_reservation(reservation)
        self.service.cancel_reservation("R1")
        self.assertEqual(len(self.service.storage.load()), 0)
