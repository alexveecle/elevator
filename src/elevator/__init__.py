import enum
import json


class ElevatorSystem:
    def __init__(self, elevators, floors):
        self.floors = floors
        self.pressed_floor_buttons = [False] * len(self.floors)
        self.elevators = [Elevator(self) for _ in range(0, elevators)]

    def press_floor_button(self, floor, state):
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
                return o.name
        return super().default(o)


def _bool_from_str(s: str) -> bool:
    s = s.lower()
    if s == "true":
        return True
    if s == "false":
        return False
    assert False, f"unknown boolean {s} should be true or false"

class ElevatorStringController:
    def command(self, *cmd):
        match cmd:
            case ["init", elevators, floors]:
                self.elevator_system = ElevatorSystem(int(elevators), list(range(0, int(floors)*10, 10)))
            case ["press_floor_button", floor, state]:
                self.elevator_system.press_floor_button(int(floor), _bool_from_str(state))
            case ["press_elevator_button", elevator, floor, state]:
                self.elevator_system.press_elevator_button(int(elevator), int(floor), _bool_from_str(state))
                return
            case ["set_elevator_state", elevator, state]:
                self.elevator_system.set_elevator_state(int(elevator), ElevatorState[state])
            case ["step"]:
                self.elevator_system.step()
            case ["get_state_json"]:
                return json.dumps(self.elevator_system, cls=JSONEncoder)
            case _:
                assert False, f"unknown cmd {cmd}"
