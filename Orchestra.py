from enums.PerformanceType import *
from performance.Performance import *


class Orchestra(Performance):
    performance_type = PerformanceType.ORCHESTRA

    def __init__(self, price, employees, duration, conductor, costumer, violonist):
        self.price = price
        self.employees = employees
        self.duration = duration
        self.conductor = conductor
        self.costumer = costumer
        self.violonist = violonist

    def __str__(self):
        return "Performance type: " + str(self.performance_type.name) + " Price: " + str(self.price) + " Duration: " \
               + str(self.duration) \
               + " Employees: " + str(self.employees)
