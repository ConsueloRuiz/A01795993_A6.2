import unittest
from services import HotelService
from models import Hotel


class TestHotelService(unittest.TestCase):
    def setUp(self):
        self.service = HotelService()
        self.service.storage.save([])

    def test_create_and_get_hotel(self):
        hotel = Hotel("H1", "Test Hotel", 10, 10)
        self.service.create_hotel(hotel)
        result = self.service.get_hotel("H1")
        self.assertIsNotNone(result)

    def test_reserve_room(self):
        hotel = Hotel("H2", "Reserve Hotel", 5, 5)
        self.service.create_hotel(hotel)
        self.service.reserve_room("H2")
        result = self.service.get_hotel("H2")
        self.assertEqual(result["available_rooms"], 4)
