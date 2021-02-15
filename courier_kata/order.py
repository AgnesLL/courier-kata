from courier_kata.small_parcel import SmallParcel
from courier_kata.medium_parcel import MediumParcel
from courier_kata.large_parcel import LargeParcel
from courier_kata.xl_parcel import XLParcel


class Order:

    def __init__(self, speedy):
        """Initialize an order which contains 0 or more orders.
        Orders should be added after initialization.
        """
        super().__init__()
        self.parcels = []
        self.speedy = speedy

    def add_order(self, item):
        """Add one item to the order.
        :param Parcel item: parcel object to be added to orders
        """
        self.parcels.append(item)

    def get_total_cost(self):
        """Calculate total cost of shipping, including bonus for speedy order.
        """
        cost = 0

        # add parcel costs
        for parcel in self.parcels:
            cost += parcel.get_delivery_cost()

        # double cost for speedy delivery
        if self.speedy:
            cost = cost * 2

        return cost
