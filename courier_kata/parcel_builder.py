from courier_kata.small_parcel import SmallParcel
from courier_kata.medium_parcel import MediumParcel
from courier_kata.large_parcel import LargeParcel
from courier_kata.xl_parcel import XLParcel
from courier_kata.heavy_parcel import HeavyParcel


class ParcelBuilder:
    small_dim_cap = 10
    medium_dim_cap = 50
    large_dim_cap = 100

    def __init__(self):
        super().__init__()

    def build_parcel(self, width, height, depth, weight):
        """Return a parcel object according to dimension provided
        :param int or float width: width of parcel
        :param int or float height: height of parcel
        :param int or float depth: depth of parcel
        :param int or float weight: weight of parcel in kg
        """
        if width < self.small_dim_cap and height < self.small_dim_cap and depth < self.small_dim_cap:
            small = SmallParcel(weight)
            heavy = HeavyParcel(weight)
            return small if small.cost <= heavy.cost else heavy
        elif width < self.medium_dim_cap and height < self.medium_dim_cap and depth < self.medium_dim_cap:
            medium = MediumParcel(weight)
            heavy = HeavyParcel(weight)
            return medium if medium.cost <= heavy.cost else heavy
        elif width < self.large_dim_cap and height < self.large_dim_cap and depth < self.large_dim_cap:
            large = LargeParcel(weight)
            heavy = HeavyParcel(weight)
            return large if large.cost <= heavy.cost else heavy
        else:
            xl = XLParcel(weight)
            heavy = HeavyParcel(weight)
            return xl if xl.cost <= heavy.cost else heavy

