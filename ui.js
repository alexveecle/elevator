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
});

function initialState(data) {
    for(i=0; i<data.pressed_floor_buttons.length; i++) {
        floor_button = document.importNode(document.getElementById("floor-button").content, true);
        floor_button.querySelector("button").textContent = i;
        floor_button.querySelector("button").addEventListener("click", (e) => {
            floor = e.target.textContent;
            ws.send("press_floor_button " + floor + " true");
        });
        document.getElementById("elevator-system").append(floor_button);
    }
    document.getElementById("initialized").checked = true;
    console.log("Initialized");
}
