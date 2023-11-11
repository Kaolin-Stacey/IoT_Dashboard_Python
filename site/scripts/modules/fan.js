const Gpio = require('onoff').Gpio;

export var fan = new Gpio(17, 'out');
var fanInput1 = new Gpio(4, 'out');
var fanInput2 = new Gpio(27, 'out');

fanInput1.writeSync(1);

export function toggleFan() {
    console.log("toggling fan");
    if (fan.readSync() === 0) { //check the pin state, if the state is 0 (or off)
        fan.writeSync(1); //set pin state to 1 (turn LED on)
    } else {
        fan.writeSync(0); //set pin state to 0 (turn LED off)
    }
}

// https://www.w3schools.com/nodejs/nodejs_raspberrypi_blinking_led.asp#:~:text=the%20following%20code%3A-,blink,-.js