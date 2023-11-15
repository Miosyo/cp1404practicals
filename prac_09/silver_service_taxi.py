"""A silver service taxi."""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a silver service taxi instance."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        """Add the flagfall to the fare."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a taxi but with the flagfall appended"""
        return super().__str__() + f" plus a flagfall of ${self.flagfall}"
