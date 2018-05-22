from enums.PerformanceType import *
from performance.Performance import *


class CircusShow(Performance):
    performance_type = PerformanceType.CIRCUS_SHOW

    def __init__(self, price, employees, duration, director, acrobats, participants, lions):
        self.price = price
        self.employees = employees
        self.duration = duration
        self.director = director
        self.acrobats = acrobats
        self.participants = participants
        self.lions = lions

    def __str__(self):
        return "Performance type: " + str(self.performance_type.name) + " Price: " + str(self.price) + " duration: " \
               + str(self.duration) \
               + " Employees: " + str(self.employees)
