class ElectricPowered():

    def __init__(self, battery_cap):
        self.battery_capacity = battery_cap
        self.battery_level = 0

    def drive(self, lowerby):
        self.battery_level -= lowerby
        print(f"The damn kids drove the battery level down to {self.battery_level} KWH.")

    def recharge(self):
        self.battery_level = self.battery_capacity
        print(f"Your battery level is at {self.battery_level} KWH.")