import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from tire.tire_factory import TireFactory


class TestTire(unittest.TestCase):
    def test_carrigan_should_be_serviced(self):
        tires_wear = [0.1, 0.3, 0.5, 1]
        tires = CarriganTire(tires_wear)
        self.assertTrue(tires.needs_service())

    def test_carrigan_should_not_be_serviced(self):
        tires_wear = [0.1, 0.3, 0.5, 0.6]
        tires = CarriganTire(tires_wear)
        self.assertFalse(tires.needs_service())

    def test_Octoprime_should_be_serviced(self):
        tires_wear = [0.8, 0.8, 0.8, 0.8]
        tires = OctoprimeTire(tires_wear)
        self.assertTrue(tires.needs_service())

    def test_Octoprime_should_not_be_serviced(self):
        tires_wear = [0.7, 0.7, 0.7, 0.7]
        tires = OctoprimeTire(tires_wear)
        self.assertFalse(tires.needs_service())
