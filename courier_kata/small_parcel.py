from courier_kata.parcel import Parcel


class SmallParcel(Parcel):
    """Small parcels
    All dimensions < 10cm
    Cost $3
    """
    cost = 3

    def __init__(self):
        super().__init__()

    def get_delivery_cost(self):
        return self.cost
