"""Project class"""


class Project:
    """Contain the data for a project."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize the class variables."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the object"""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate},"
                f" completion: {self.completion_percentage}%")

    def __repr__(self):
        """Returns the string representation of the object wrapped in brackets"""
        return f"({self.__str__()})"

    def is_complete(self):
        """Return true if completion percentage is >= 100"""
        return self.completion_percentage >= 100

    def __lt__(self, other):
        """Compare priority of both object"""
        return self.priority < other.priority
