from electricPowered import ElectricPowered

class ChargingStation:

    def __init__(self):
        self.__vehicles = []

    def add_vehicles(self, vehicle):
        # Only allow electric powered vehicles in list

        # if isinstance(vehicle, ElectricPowered):
        #     self.__vehicles.append(vehicle)

        # if hasattr(vehicle, "battery_level"):
        #     self.__vehicles.append(vehicle)

        try:
            if vehicle.battery_level > -1 and vehicle.battery_capacity > -1:
                self.__vehicles.append(vehicle)
        except AttributeError:
            print(f"Electric Powered Vehicles Only")
