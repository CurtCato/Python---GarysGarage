from mustang import Mustang
from ram import Ram
from leaf import Leaf
from crosstrek import CrossTreck
from pumpstation import PumpStation
from chargingstation import ChargingStation

ram = Ram()
must = Mustang()
tree = Leaf()

tree.drive()

gas_pump_station = PumpStation()
electric_charging_station = ChargingStation()

gas_pump_station.add_vehicles(ram)
gas_pump_station.add_vehicles(must)
electric_charging_station.add_vehicles(tree)
