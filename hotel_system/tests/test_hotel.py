# -*- coding: utf-8 -*-
# !/usr/bin/env python

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

    def test_get_hotel_not_found(self):
        result = self.service.get_hotel("NO_EXIST")
        self.assertIsNone(result)

    def test_delete_hotel_not_found(self):
        self.service.delete_hotel("NO_EXIST")
        hotels = self.service.storage.load()
        self.assertEqual(hotels, [])

    def test_update_hotel_not_found(self):
        self.service.update_hotel("NO_EXIST", name="Nuevo")
        hotels = self.service.storage.load()
        self.assertEqual(hotels, [])

    def test_reserve_no_rooms(self):
        hotel = Hotel("H9", "Full Hotel", 1, 0)
        self.service.create_hotel(hotel)
        self.service.reserve_room("H9")

        result = self.service.get_hotel("H9")
        self.assertEqual(result["available_rooms"], 0)

    def test_cancel_reservation_no_hotel(self):
        self.service.cancel_reservation("NO_EXIST")
        self.assertEqual(self.service.storage.load(), [])
