import unittest
from services import CustomerService
from models import Customer


class TestCustomerService(unittest.TestCase):
    def setUp(self):
        self.service = CustomerService()
        self.service.storage.save([])

    def test_create_customer(self):
        customer = Customer("C1", "Alice", "alice@mail.com")
        self.service.create_customer(customer)
        result = self.service.get_customer("C1")
        self.assertEqual(result["name"], "Alice")
