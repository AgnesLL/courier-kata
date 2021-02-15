from courier_kata.parcel import Parcel


class XLParcel(Parcel):
    """XL parcels
    any dimension >= 100cm
    cost $25
    """
    cost = 25

    def __init__(self):
        super().__init__()

    def get_delivery_cost(self):
        return self.cost
