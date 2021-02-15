from courier_kata.parcel import Parcel


class MediumParcel(Parcel):
    """Medium parcels
    All dimensions < 50cm
    Cost $8
    """
    cost = 8

    def __init__(self):
        super().__init__()

    def get_delivery_cost(self):
        return self.cost
