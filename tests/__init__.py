import unittest

from courier_kata.parcel_builder import ParcelBuilder


class TestParcelCost(unittest.TestCase):
    def setUp(self):
        self.parcel_builder = ParcelBuilder()

    def test_small(self):
        parcel = self.parcel_builder.build_parcel(5, 5, 5)
        self.assertEqual(parcel.get_delivery_cost(), 3)

    def test_medium(self):
        parcel = self.parcel_builder.build_parcel(20, 20, 20)
        self.assertEqual(parcel.get_delivery_cost(), 8)

    def test_large(self):
        parcel = self.parcel_builder.build_parcel(75, 75, 75)
        self.assertEqual(parcel.get_delivery_cost(), 15)

    def test_xl(self):
        parcel = self.parcel_builder.build_parcel(175, 175, 175)
        self.assertEqual(parcel.get_delivery_cost(), 25)
