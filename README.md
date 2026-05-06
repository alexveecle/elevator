# elevator

```
pdm install
pdm run server
```

```
$ uwsc http://127.0.0.1:8765
> init 3 8
Send 'init 3 8'
Server message: 'None'
> get_state_json
Send 'get_state_json'
Server message: '{"elevators": [{"position": 0, "state": "ElevatorState.CLOSED", "pressed_floor_buttons": [false, false, false, false, false, false, false, false]}, {"position": 0, "state": "ElevatorState.CLOSED", "pressed_floor_buttons": [false, false, false, false, false, false, false, false]}, {"position": 0, "state": "ElevatorState.CLOSED", "pressed_floor_buttons": [false, false, false, false, false, false, false, false]}], "pressed_floor_buttons": [false, false, false, false, false, false, false, false], "floors": [0, 10, 20, 30, 40, 50, 60, 70]}'
> set_elevator_state 1 UP
Send 'set_elevator_state 1 UP'
Server message: 'None'
> step
Send 'step'
Server message: 'None'
> get_state_json
Send 'get_state_json'
Server message: '{"elevators": [{"position": 0, "state": "ElevatorState.CLOSED", "pressed_floor_buttons": [false, false, false, false, false, false, false, false]}, {"position": 1, "state": "ElevatorState.UP", "pressed_floor_buttons": [false, false, false, false, false, false, false, false]}, {"position": 0, "state": "ElevatorState.CLOSED", "pressed_floor_buttons": [false, false, false, false, false, false, false, false]}], "pressed_floor_buttons": [false, false, false, false, false, false, false, false], "floors": [0, 10, 20, 30, 40, 50, 60, 70]}'
...
```

```
firefox ui.html
```
