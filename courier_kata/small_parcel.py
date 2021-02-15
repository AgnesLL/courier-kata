from courier_kata.parcel import Parcel


class SmallParcel(Parcel):
    """Small parcels
    All dimensions < 10cm
    Cost $3
    weight limit 1 kg
    +$2/kg over weight limit
    """
    cost = 3
    weight_limit = 1  # in kg
    overweight_cost_per_kg = 2

    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def get_delivery_cost(self):
        return self.cost if self.weight <= self.weight_limit else self.cost + (
                    self.weight - self.weight_limit) * self.overweight_cost_per_kg
