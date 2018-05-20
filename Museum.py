class Museum:

    total_number_of_halls = 0

    def __init__(self, name = "lviv art gallery", type = "historical", location = "Stefanik 3",
                 number_of_exhibits = 60000, year_of_foundation = 1907):

        self.name = name
        self.type = type
        self.location = location
        self.number_of_exhibits = number_of_exhibits
        self.year_of_foundation = year_of_foundation
        Museum.total_number_of_halls += number_of_exhibits

    def to_string(self):
         print("Name:" + self.name, "Type:" + self.type, "Location:" , self.location,
         "Number of exhibits:" , self.number_of_exhibits, "Year of fondation:", self.year_of_foundation)

    def print_sum(self):
                print("Current number of exhibits", self.number_of_exhibits, "at the museum" + self.name) \

    @staticmethod
    def print_static_sum():
         print("Total number of exhibits:", Museum.total_number_of_halls)

if __name__ == "__main__":
        lviv_art_gallery = Museum()
        ivan_trush = Museum("Ivan_Trush", "modern", "Trusha 28", 1000, 1986)
        arsenal =Museum("Arsenal", "historical", "Pidvalna 21", 2300, 1981)

        print("\n")
        lviv_art_gallery.to_string()
        ivan_trush.to_string()
        arsenal.to_string()

        print("\n")
        lviv_art_gallery.print_sum()

        print("\n")
        Museum.print_static_sum()




