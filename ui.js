ws = new WebSocket("ws://127.0.0.1:8765/");
ws.addEventListener("open", () => {
    console.log("connected");
    setInterval(() => {
        ws.send("get_state_json");
    }, 100);
});
ws.addEventListener("message", (e) => {
    data = JSON.parse(e.data);
    document.getElementById("state").value = JSON.stringify(data);
    if(!document.getElementById("initialized").checked) {
        initialState(data);
    }
    for(i=0; i<data.elevators.length; i++) {
        elevatorData = data.elevators[i];
        elevator = document.querySelector("#elevator-"+i);
        elevator.querySelector(".position").value = elevatorData.position;
        elevator.querySelector("select").selectedIndex = ["UP", "DOWN", "OPEN", "CLOSED"].findIndex((e) => e == elevatorData.state);
    }
});

function initialState(data) {
    for(i=0; i<data.pressed_floor_buttons.length; i++) {
        floor_button = document.importNode(document.getElementById("floor-button").content, true);
        floor_button.querySelector("button").textContent = i;
        floor_button.querySelector("button").addEventListener("click", (e) => {
            floor = e.target.textContent;
            ws.send("press_floor_button " + floor + " true");
        });
        document.querySelector("floor-buttons").append(floor_button);
    }
    for(i=0; i<data.elevators.length; i++) {
        elevator = document.importNode(document.getElementById("elevator").content, true);
        elevator.querySelector("h2").textContent += i;
        elevator.querySelector("elevator").id = "elevator-" + i;
        for(j=0; j<data.pressed_floor_buttons.length; j++) {
            floor_button = document.importNode(document.getElementById("floor-button").content, true);
            floor_button.querySelector("button").textContent = j;
            floor_button.querySelector("button").addEventListener("click", (e) => {
                floor = e.target.textContent;
                elevator = e.target.parentElement.parentElement.parentElement.id.match(/elevator-(.*)/)[1];
                ws.send("press_elevator_button " + elevator + " " + floor + " true");
            });
            elevator.querySelector("floor-buttons").append(floor_button);
        }
        document.querySelector("elevators").append(elevator);
    }
    document.getElementById("initialized").checked = true;
    console.log("Initialized");
}
