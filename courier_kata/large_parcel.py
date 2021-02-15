from courier_kata.parcel import Parcel


class LargeParcel(Parcel):
    """Large parcels
    All dimensions < 100cm
    cost $15
    weight limit 6 kg
    +$2/kg over weight limit
    """
    cost = 15
    weight_limit = 6  # kg
    overweight_cost_per_kg = 2

    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def get_delivery_cost(self):
        return self.cost if self.weight <= self.weight_limit else self.cost + (
                    self.weight - self.weight_limit) * self.overweight_cost_per_kg
