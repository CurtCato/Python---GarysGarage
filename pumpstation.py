from gasPowered import GasPowered

class PumpStation:

    def __init__(self):
        self.__vehicles = []

    def add_vehicles(self, vehicle):
        # Only allow gas powered vehicles in list

        # if isinstance(vehicle, GasPowered):
        #     self.__vehicles.append(vehicle)

        # if hasattr(vehicle, "gas_level"):
        #     self.__vehicles.append(vehicle)

        try:
            if vehicle.gas_level > -1 and vehicle.fuel_capacity > -1:
                self.__vehicles.append(vehicle)
        except AttributeError:
            print(f"Gas Powered Vehicles Only")

