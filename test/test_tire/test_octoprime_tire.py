import unittest
from src.tire.octoprime_tire import OctoprimeTire

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.6, 0.7, 0.8, 0.9]
        tires = OctoprimeTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0, 0, 0, 0.8]
        tires = OctoprimeTire(tire_wear)
        self.assertFalse(tires.needs_service())