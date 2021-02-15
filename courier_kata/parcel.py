from abc import ABC


class Parcel(ABC):
    """Parcel object containing information about size, type and delivery cost"""

    def __init__(self):
        super().__init__()

