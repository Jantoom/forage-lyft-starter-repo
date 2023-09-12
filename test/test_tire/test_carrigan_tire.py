import unittest
from src.tire.carrigan_tire import CarriganTire

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0, 0, 0, 0.9]
        tires = CarriganTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0, 0, 0, 0.8]
        tires = CarriganTire(tire_wear)
        self.assertFalse(tires.needs_service())