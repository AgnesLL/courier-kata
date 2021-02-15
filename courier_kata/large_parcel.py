from courier_kata.parcel import Parcel


class LargeParcel(Parcel):
    """Large parcels
    All dimensions < 100cm
    cost $15
    """
    cost = 15

    def __init__(self):
        super().__init__()

    def get_delivery_cost(self):
        return self.cost
