# elevator

This repository contains:

* A websocket server that simulates an elevator environment.
* A web interface that displays the status of the elevator environment and that you can use to interact with the environment.

## Running the server

```
pdm install
pdm run server
```

The server listens for websocket connections on `http://127.0.0.1:8765`.

## Interacting with the server

You can use websockets tools such as `uwsc` or `websocat` to interact with the server.

```
$ uwsc http://127.0.0.1:8765
```

The server starts in a nil environment, you initialize the environment by sending the `init x y` command, where `x` is the number of elevators and `y` is the number of floors.

```
> init 3 8
```

You can retrieve the status with the `get_state_json` command, that returns a JSON like the following:

```
{
    "floors": [
        0,
        10,
        20
    ],
    "elevators": [
        {
            "position": 0,
            "state": "CLOSED",
            "pressed_floor_buttons": [
                false,
                false,
                false
            ]
        },
        {
            "position": 0,
            "state": "CLOSED",
            "pressed_floor_buttons": [
                false,
                false,
                false
            ]
        }
    ],
    "pressed_floor_buttons": [
        false,
        false,
        false
    ]
}
```

The `floors` element contains the positions of each floor.
The first floor has position 0, the second floor position 10, the third floor position 20, and so forth.
(Elevators move in discrete positions in steps of 1, so moving one floor requires 10 simulation steps.)

The `elevators` element is an array of the elevator states.
Each elevator has the following values:

* `position`
* `state`: one of `UP`, `DOWN`, `CLOSED`, `OPEN`
* `pressed_floor_buttons`: an array of booleans representing the buttons inside the elevator.

The `pressed_floor_buttons` element is also an array of booleans representing the button on each floor.

You can use the following commands to interact with the simulation (for example, from a user interface or running a test scenario):

* `press_floor_button floor_number true|false`
* `press_elevator_button elevator_number floor_number true|false`

Where:

* `floor_number` and `elevator_number` are a 0-based integers represented as strings.
* `true|false` is `true` to set the button as pressed, `false` to set it as unpressed.

The elevator controller should use the `set_elevator_state elevator_number UP|DOWN|CLOSED|OPEN` command to control the elevators.
Use the following states:

* `UP` and `DOWN` instructs the simulator to move the elevator up or down at one position per simulation step.
* `CLOSED` leaves the elevator stationary with the doors closed.
* `OPEN` leaves the elevator stationary with the doors open.

Finally, the `step` command runs one simulation step.
The `step` command moves the elevator and resets all buttons to the `false` state.

## Visualizing the simulator

```
firefox ui.html
```

`ui.html` displays the simulation state refreshed 10 times per second.
