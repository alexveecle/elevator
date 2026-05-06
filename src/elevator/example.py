import elevator
import json


es = elevator.ElevatorSystem(3, list(range(0, 81, 10)))

while True:
    print(json.dumps(es, cls=elevator.JSONEncoder))
    es.set_elevator_state(0, elevator.ElevatorState.UP)
    es.step()
