class GasPowered():

    def __init__(self, fuel_cap):
        self.fuel_capacity = fuel_cap
        self.gas_level = 0

    def drive(self, lowerby):
        self.gas_level -= lowerby
        print(f"What the hell, kids drove the gas level down to {self.gas_level} gallons.")

    def refuel(self):
        self.gas_level = self.fuel_capacity
        print(f"Your fuel level is now full at {self.gas_level} gallons.")