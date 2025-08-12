class vehicle:
    def __init__(self, brand, modal):
        self.brand = brand
        self.modal = modal

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Modal : {self.modal}")


class car(vehicle):
    def __init__(self, brand, modal, doors):
        super().__init__(brand, modal)
        self.number_of_doors = doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors : {self.number_of_doors}")


class bike(vehicle):
    def __init__(self, brand, modal, has_sidecar):
        super().__init__(brand, modal)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Has Sidecar : {self.has_sidecar}")


# c1 = car("Audi", "V8", 4)
# c1.display_info()
# b1 = bike("Yamaha", 125, False)
# b1.display_info()
