from courier_kata.small_parcel import SmallParcel
from courier_kata.medium_parcel import MediumParcel
from courier_kata.large_parcel import LargeParcel
from courier_kata.xl_parcel import XLParcel


class ParcelBuilder:
    small_dim_cap = 10
    medium_dim_cap = 50
    large_dim_cap = 100

    def __init__(self):
        super().__init__()

    def build_parcel(self, width, height, depth):
        """Return a parcel object according to dimension provided
        :param int or float width: width of parcel
        :param int or float height: height of parcel
        :param int or float depth: depth of parcel
        """
        if width < self.small_dim_cap and height < self.small_dim_cap and depth < self.small_dim_cap:
            return SmallParcel()

        elif width < self.medium_dim_cap and height < self.medium_dim_cap and depth < self.medium_dim_cap:
            return MediumParcel()

        elif width < self.large_dim_cap and height < self.large_dim_cap and depth < self.large_dim_cap:
            return LargeParcel()

        else:
            return XLParcel()

