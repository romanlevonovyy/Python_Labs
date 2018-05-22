from performance.Orchestra import *
from performance.RockConcert import *
from ConcertHall import *
from performance.CircusShow import *

if __name__ == '__main__':
    musician = ConcertHall("Opera Theatre", "Lviv", "City centre", "from 9 to 23")

    rock_concert = RockConcert(50.0, 5, 3, 2, 1, 1)
    orchestra = Orchestra(70.0, 1, 4, 10, 12, 11)
    circus_show = CircusShow(30.5, 4, 12, 102, 15, 61, 5)

    musician.performances = [orchestra, circus_show, rock_concert]
    print("Initial list:")
    musician.print_list()

    musician.sort_by_price()
    print("Sorted list")
    musician.print_list()

    musician.performances = musician.find_by_type(PerformanceType.ORCHESTRA)
    print("Found list:")
    musician.print_list()

    pass
