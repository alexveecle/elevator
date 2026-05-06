import enum
import json


class ElevatorSystem:
    def __init__(self, elevators, floors):
        self.floors = floors
        self.pressed_floor_buttons = [False] * len(floors)
        self.elevators = [Elevator(self) for _ in range(0, elevators)]


class ElevatorState(enum.Enum):
    CLOSED = 0
    OPEN = 1
    UP = 2
    DOWN = 3


class Elevator:
    def __init__(self, elevator_system):
        self.elevator_system = elevator_system
        self.position = 0
        self.state = ElevatorState.CLOSED
        self.pressed_floor_buttons = [False] * len(elevator_system.floors)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        match o:
            case ElevatorSystem(elevators=elevators, floors=floors, pressed_floor_buttons=pressed_floor_buttons):
                return {
                    "elevators": elevators,
                    "pressed_floor_buttons": pressed_floor_buttons,
                    "floors": floors
                }
            case Elevator(position=position, state=state, pressed_floor_buttons=pressed_floor_buttons):
                return {
                    "position": position,
                    "state": state,
                    "pressed_floor_buttons": pressed_floor_buttons,
                }
            case ElevatorState:
                return str(o)
        return super().default(o)
