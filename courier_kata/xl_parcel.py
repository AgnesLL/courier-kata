from courier_kata.parcel import Parcel


class XLParcel(Parcel):
    """XL parcels
    any dimension >= 100cm
    cost $25
    weight limit 10 kg
    +$2/kg over weight limit
    """
    cost = 25
    weight_limit = 10  # kg
    overweight_cost_per_kg = 2

    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def get_delivery_cost(self):
        return self.cost if self.weight <= self.weight_limit else self.cost + (
                    self.weight - self.weight_limit) * self.overweight_cost_per_kg
