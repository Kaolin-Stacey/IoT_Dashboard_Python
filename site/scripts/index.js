const { JSDOM } = require( "jsdom" );
const { window } = new JSDOM( "" );
const $ = require( "jquery" )( window );
const Gpio = require('onoff').Gpio;



// import { led, toggleLed } from "./modules/led.js";
// import { fan, toggleFan } from "./modules/fan.js";


// $("#fanInput").click(toggleFan);