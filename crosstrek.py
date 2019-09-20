from vehicle import Vehicle
from gasPowered import GasPowered
from electricPowered import ElectricPowered

class CrossTreck(Vehicle, ElectricPowered, GasPowered):

    def __init__(self):
        Vehicle.__init__(self, "Subaru", "Crosstrek", 60, 4)
        ElectricPowered.__init__(self, 40)
        GasPowered.__init__(self, 6)

    def recharge(self):
        ElectricPowered.recharge(self)

    def refuel(self):
        GasPowered.refuel(self)

    def drive(self):
        ElectricPowered.drive(self, 2)
        GasPowered.drive(self, 0.5)