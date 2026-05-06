import elevator
import json


es = elevator.ElevatorStringController()

es.command("init", "3", "8")
es.command("set_elevator_state", "0", "UP")

while True:
    print(es.command("get_state_json"))
    es.command("step")
