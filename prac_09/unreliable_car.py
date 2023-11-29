"""An unreliable car"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Represent an unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Initialize an unreliable car instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive a car a given distance if it passes a reliability test."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
