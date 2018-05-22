from enums.PerformanceType import *
from performance.Performance import *


class RockConcert(Performance):
    performance_type = PerformanceType.ROCK_CONCERT

    def __init__(self, price, employees, duration, guitarist, pianist, drummer):
        self.price = price
        self.employees = employees
        self.duration = duration
        self.guitarist = guitarist
        self.pianist = pianist
        self.drummer = drummer

    def __str__(self):
        return "Performance type: " + str(self.performance_type.name) + " Price: " + str(self.price) + " Duration: " \
               + str(self.duration) \
               + " Employees: " + str(self.employees)
