import elevator
import json


print(json.dumps(elevator.ElevatorSystem(3, list(range(0, 81, 10))), cls=elevator.JSONEncoder))
