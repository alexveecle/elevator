import enum
import json


class ElevatorSystem:
    def __init__(self, elevators, floors):
        self.floors = floors
        self.pressed_floor_buttons = [False] * len(self.floors)
        self.elevators = [Elevator(self) for _ in range(0, elevators)]

    def set_floor_button(self, floor, state):
        self.pressed_floor_buttons[floor] = state

    def press_elevator_button(self, elevator, floor, state):
        self.elevators[elevator].pressed_floor_buttons[floor] = state

    def set_elevator_state(self, elevator, state):
        self.elevators[elevator].state = state

    def step(self):
        self.pressed_floor_buttons = [False] * len(self.floors)
        for elevator in self.elevators:
            match elevator.state:
                case ElevatorState.CLOSED:
                    pass
                case ElevatorState.OPEN:
                    pass
                case ElevatorState.UP:
                    elevator.position += 1
                    assert elevator.position <= self.max_position(), f"elevator {elevator} in position {elevator.position} > {self.max_position()}"
                case ElevatorState.DOWN:
                    elevator.position -= 1
                    assert elevator.position >= self.min_position(), f"elevator {elevator} in position {elevator.position} < {self.min_position()}"

    def min_position(self):
        return min(self.floors)

    def max_position(self):
        return max(self.floors)


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
