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

        # discounts
        cost += self.get_discounts()

        # double cost for speedy delivery
        if self.speedy:
            cost = cost * 2

        return cost

    def get_discounts(self):
        num_small = 0
        num_medium = 0
        num_large = 0
        num_xl = 0
        num_heavy = 0

        # self.parcels.sort(key=lambda x: x.cost)
        small_parcel_cost = []
        medium_parcel_cost = []
        other_parcel_cost = []
        for parcel in self.parcels:
            if isinstance(parcel, SmallParcel):
                small_parcel_cost.append(parcel.cost)
                num_small += 1
            elif isinstance(parcel, MediumParcel):
                medium_parcel_cost.append(parcel.cost)
                num_medium += 1
            elif isinstance(parcel, LargeParcel):
                other_parcel_cost.append(parcel.cost)
                num_large += 1
            elif isinstance(parcel, XLParcel):
                other_parcel_cost.append(parcel.cost)
                num_xl += 1
            else:
                other_parcel_cost.append(parcel.cost)
                num_heavy += 1

        num_small_discount = int(num_small / 4)
        num_medium_discount = int(num_medium / 3)

        num_small -= num_small_discount*4
        num_medium -= num_medium_discount*3

        num_total = num_small + num_medium + num_large + num_xl + num_heavy
        num_mixed_discount = int(num_total / 5)

        small_parcel_cost.sort(reverse=True)
        medium_parcel_cost.sort(reverse=True)

        total_cost = 0

        for i in range(num_small_discount):
            total_cost -= small_parcel_cost[-1]
            del small_parcel_cost[-1]

        for i in range(num_medium_discount):
            total_cost -= medium_parcel_cost[-1]
            del medium_parcel_cost[-1]

        other_parcel_cost += small_parcel_cost + medium_parcel_cost
        other_parcel_cost.sort(reverse=True)

        for i in range(num_mixed_discount):
            total_cost -= other_parcel_cost[-1]
            del other_parcel_cost[-1]

        return total_cost
