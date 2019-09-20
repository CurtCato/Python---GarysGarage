from vehicle import Vehicle
from electricPowered import ElectricPowered

class Leaf(Vehicle, ElectricPowered):

    def __init__(self):
        Vehicle.__init__(self, "Leaf", "Nissan", 395, 4)
        ElectricPowered.__init__(self, 45)

    def drive(self):
        ElectricPowered.drive(self, 6)

    def recharge(self):
        self.battery_level = self.battery_capacity
        print(f"The battery is now full at {self.battery_level} KW.")