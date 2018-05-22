class ConcertHall:
    performances = []

    def __init__(self, name, surname, address, working_hours):
        self.name = name
        self.surname = surname
        self.address = address
        self.working_hours = working_hours

    def sort_by_price(self):
        self.performances.sort(key=lambda performance: performance.price)

    def find_by_type(self, performance_type):
        found_performances = []

        for performance in self.performances:
            if performance.performance_type == performance_type:
                found_performances.append(performance)

        return found_performances

    def add_performance(self, performance):
        self.performances += performance

    def print_list(self):
        for performance in self.performances:
            print(performance)
        print("\n")
