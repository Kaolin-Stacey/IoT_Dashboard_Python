var Gpio = global.Gpio;

export var led = new Gpio(20, 'out');

export function toggleLed() {
    console.log("toggling LED");
    if (led.readSync() === 0) { //check the pin state, if the state is 0 (or off)
        led.writeSync(1); //set pin state to 1 (turn LED on)
    } else {
        led.writeSync(0); //set pin state to 0 (turn LED off)
    }
}