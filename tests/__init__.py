import unittest

from courier_kata.parcel_builder import ParcelBuilder
from courier_kata.order import Order
from courier_kata.heavy_parcel import HeavyParcel


class TestParcelCost(unittest.TestCase):
    def setUp(self):
        self.parcel_builder = ParcelBuilder()

    def test_small(self):
        parcel = self.parcel_builder.build_parcel(5, 5, 5, 1)
        self.assertEqual(parcel.get_delivery_cost(), 3)

    def test_medium(self):
        parcel = self.parcel_builder.build_parcel(20, 20, 20, 2)
        self.assertEqual(parcel.get_delivery_cost(), 8)

    def test_large(self):
        parcel = self.parcel_builder.build_parcel(75, 75, 75, 2)
        self.assertEqual(parcel.get_delivery_cost(), 15)

    def test_xl(self):
        parcel = self.parcel_builder.build_parcel(175, 175, 175, 2)
        self.assertEqual(parcel.get_delivery_cost(), 25)

    def test_heavy(self):
        parcel = self.parcel_builder.build_parcel(2, 2, 2, 50)
        #self.assertEqual(isinstance(parcel.get_delivery_cost(), HeavyParcel), True)
        self.assertEqual(parcel.get_delivery_cost(), 50)


class TestSpeedyOrder(unittest.TestCase):
    def setUp(self):
        self.parcel_builder = ParcelBuilder()

    def test_small(self):
        order = Order(True)
        parcel = self.parcel_builder.build_parcel(1, 5, 9, 1)
        order.add_order(parcel)
        self.assertEqual(order.get_total_cost(), 6)

    def test_medium(self):
        order = Order(True)

        parcel = self.parcel_builder.build_parcel(15, 20, 30, 3)
        order.add_order(parcel)
        self.assertEqual(order.get_total_cost(), 16)

    def test_large(self):
        order = Order(True)
        parcel = self.parcel_builder.build_parcel(70, 75, 75, 6)
        order.add_order(parcel)
        self.assertEqual(order.get_total_cost(), 30)

    def test_heavy(self):
        order = Order(True)
        parcel = self.parcel_builder.build_parcel(2, 2, 2, 50)
        order.add_order(parcel)
        #self.assertEqual(parcel.get_delivery_cost(), 100)
        self.assertEqual(order.get_total_cost(), 100)


class TestNormalOrder(unittest.TestCase):

    def setUp(self):
        self.parcel_builder = ParcelBuilder()

    def test_small(self):
        order = Order(False)
        parcel = self.parcel_builder.build_parcel(1, 5, 9, 2)
        order.add_order(parcel)
        self.assertEqual(order.get_total_cost(), parcel.get_delivery_cost())

    def test_medium(self):
        order = Order(False)
        parcel = self.parcel_builder.build_parcel(15, 20, 30, 2)
        order.add_order(parcel)
        self.assertEqual(order.get_total_cost(), parcel.get_delivery_cost())

    def test_large(self):
        order = Order(False)
        parcel = self.parcel_builder.build_parcel(70, 75, 75, 2)
        order.add_order(parcel)
        self.assertEqual(order.get_total_cost(), parcel.get_delivery_cost())

    def test_xl(self):
        order = Order(False)
        parcel = self.parcel_builder.build_parcel(175, 175, 175, 2)
        order.add_order(parcel)
        self.assertEqual(order.get_total_cost(), parcel.get_delivery_cost())


class TestExtraWeight(unittest.TestCase):
    def setUp(self):
        self.parcel_builder = ParcelBuilder()

    def test_small(self):
        parcel = self.parcel_builder.build_parcel(5, 5, 5, 2)
        self.assertEqual(parcel.get_delivery_cost(), 5)

    def test_medium(self):
        parcel = self.parcel_builder.build_parcel(20, 20, 20, 5)
        self.assertEqual(parcel.get_delivery_cost(), 12)

    def test_large(self):
        parcel = self.parcel_builder.build_parcel(75, 75, 75, 10)
        self.assertEqual(parcel.get_delivery_cost(), 23)

    def test_xl(self):
        parcel = self.parcel_builder.build_parcel(175, 175, 175, 11)
        self.assertEqual(parcel.get_delivery_cost(), 27)


class TestDiscounts(unittest.TestCase):
    def setUp(self):
        self.parcel_builder = ParcelBuilder()

    def test_small(self):
        order = Order(True)
        parcel1 = self.parcel_builder.build_parcel(1, 5, 9, 1)
        parcel2 = self.parcel_builder.build_parcel(1, 5, 9, 1)
        parcel3 = self.parcel_builder.build_parcel(1, 5, 9, 1)
        parcel4 = self.parcel_builder.build_parcel(1, 5, 9, 1)
        order.add_order(parcel1)
        order.add_order(parcel2)
        order.add_order(parcel3)
        order.add_order(parcel4)
        self.assertEqual(order.get_total_cost(), 18)

    def test_medium(self):
        order = Order(False)
        parcel1 = self.parcel_builder.build_parcel(1, 5, 11, 1)
        parcel2 = self.parcel_builder.build_parcel(1, 5, 11, 1)
        parcel3 = self.parcel_builder.build_parcel(1, 5, 11, 1)
        order.add_order(parcel1)
        order.add_order(parcel2)
        order.add_order(parcel3)
        self.assertEqual(order.get_total_cost(), 16)

    def test_mixed(self):
        order = Order(False)
        parcel1 = self.parcel_builder.build_parcel(1, 5, 9, 1)
        parcel2 = self.parcel_builder.build_parcel(1, 5, 11, 1)
        parcel3 = self.parcel_builder.build_parcel(1, 5, 100, 1)
        parcel4 = self.parcel_builder.build_parcel(1, 5, 100, 1)
        parcel5 = self.parcel_builder.build_parcel(1, 5, 100, 1)
        order.add_order(parcel1)
        order.add_order(parcel2)
        order.add_order(parcel3)
        order.add_order(parcel4)
        order.add_order(parcel5)
        self.assertEqual(order.get_total_cost(), 83)

    def test_no_discount(self):
        order = Order(True)
        parcel1 = self.parcel_builder.build_parcel(1, 5, 9, 1)
        parcel2 = self.parcel_builder.build_parcel(1, 5, 9, 1)
        parcel3 = self.parcel_builder.build_parcel(1, 5, 9, 1)
        order.add_order(parcel1)
        order.add_order(parcel2)
        order.add_order(parcel3)
        self.assertEqual(order.get_total_cost(), 18)


if __name__ == '__main__':
    unittest.main()

