from courier_kata.parcel import Parcel


class HeavyParcel(Parcel):
    """Heavy parcels
    Cost $50
    Weight limit 50 kg
    +$1/kg over weight limit
    """
    cost = 50
    weight_limit = 50  # kg
    overweight_cost_per_kg = 1

    def __init__(self, weight):
        super().__init__()
        self.weight = weight
        self.cost = self.get_delivery_cost()

    def get_delivery_cost(self):
        return self.cost if self.weight <= self.weight_limit else self.cost + (
                    self.weight - self.weight_limit) * self.overweight_cost_per_kg
