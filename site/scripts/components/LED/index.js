import {Gpio} from 'onoff';

export var LED = new Gpio(20, 'out');

export function toggleLed() {
    if (LED.readSync() === 0) { //check the pin state, if the state is 0 (or off)
        LED.writeSync(1); //set pin state to 1 (turn LED on)
    } else {
        LED.writeSync(0); //set pin state to 0 (turn LED off)
    }
}

// https://www.w3schools.com/nodejs/nodejs_raspberrypi_blinking_led.asp#:~:text=the%20following%20code%3A-,blink,-.js