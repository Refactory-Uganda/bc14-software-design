/*
    Computer class:
    - Can input data
    - can store & retrieve data to memory
    - can process data
    - Can output data
    - can connect to WI-FI
    - can connect bluetooth device
*/
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
// class Keyboard{
//     input(){
//         console.log("Inputing data from keyboard...");
//     }
// }
var InputDevice = /** @class */ (function () {
    function InputDevice() {
    }
    InputDevice.prototype.input = function () {
    };
    return InputDevice;
}());
var Keyboard = /** @class */ (function (_super) {
    __extends(Keyboard, _super);
    function Keyboard() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Keyboard.prototype.input = function () {
        console.log('Inputing from Keyboard');
    };
    return Keyboard;
}(InputDevice));
var Mouse = /** @class */ (function (_super) {
    __extends(Mouse, _super);
    function Mouse() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Mouse.prototype.input = function () {
        console.log('Inputing from Mouse');
    };
    return Mouse;
}(InputDevice));
// supertype 
var Computer = /** @class */ (function () {
    // To use private: define a constructor
    function Computer(InputDevice) {
        this.category = "generic";
        this.internalMemory = {};
        this.InputDevice = InputDevice;
    }
    Computer.prototype.input = function () {
        this.InputDevice.input();
    };
    // method only works for variable input device 
    Computer.prototype.setInputDevice = function (InputDevice) {
        this.InputDevice = InputDevice;
    };
    Computer.prototype.getInputDevice = function () {
        return this.InputDevice;
    };
    Computer.prototype.process = function () {
        console.log('Process with intel processor');
    };
    Computer.prototype.store = function (data) {
        console.log("Storing data into internal memory...");
        this.internalMemory = __assign(__assign({}, this.internalMemory), data);
    };
    Computer.prototype.retrieve = function (key) {
        console.log("Retrieving data from internal memory...");
        return this.internalMemory[key];
    };
    Computer.prototype.output = function (information) {
        console.log(information);
    };
    Computer.prototype.connectToBluetoothDevice = function () {
        console.log("Connecting to Bluetooth Device...");
    };
    return Computer;
}());
// abstract class
var ConnectToEthernet = /** @class */ (function () {
    function ConnectToEthernet() {
    }
    return ConnectToEthernet;
}());
// concrete classes 
var Desktop = /** @class */ (function (_super) {
    __extends(Desktop, _super);
    function Desktop() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    // we can add extra funbctionality but must first conform to teh computer Contract
    Desktop.prototype.deskPlacement = function () { };
    Desktop.prototype.connectToWIFI = function () {
        return "Wi-Fi using a laptop";
    };
    Desktop.prototype.connectToBluetooth = function () {
        console.log("Connect to Bluetooth");
    };
    return Desktop;
}(Computer));
var desktop1 = new Desktop(new Keyboard());
console.log("I am connected to " + desktop1.connectToWIFI());
var Laptop = /** @class */ (function (_super) {
    __extends(Laptop, _super);
    function Laptop() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    // we can add extra funbctionality but must first conform to teh computer Contract
    Laptop.prototype.palmRest = function () { };
    Laptop.prototype.connectToWIFI = function () {
        console.log("Connect to Wifi");
    };
    Laptop.prototype.connectToBluetooth = function () {
        console.log('Connect to bluetooth');
    };
    return Laptop;
}(Computer));
var Phone = /** @class */ (function (_super) {
    __extends(Phone, _super);
    function Phone() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    // we can add extra funbctionality but must first conform to teh computer Contract
    Phone.prototype.screenTouch = function () { };
    Phone.prototype.connectToWIFI = function () {
        console.log("Connect to Wifi");
    };
    return Phone;
}(Computer));
// Violates Liskov since it doesn't conform to the methods in supertype Computer
var OldModel = /** @class */ (function (_super) {
    __extends(OldModel, _super);
    function OldModel() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    // we can add extra funbctionality but must first conform to teh computer Contract
    OldModel.prototype.legacyMethod = function () { };
    return OldModel;
}(Computer));
// Computer Objects
// let computer1 = new Computer();
// computer1.InputDevice = new Keyboard();
// computer1.InputDevice = new Mouse();
// Changes
var computer1 = new Computer(new Keyboard());
// setting the input device after the object is created
// Change input device dynamically using a setter - can set a valye multiple times 
computer1.setInputDevice(new Mouse());
// computer1.setInputDevice(new Keyboard());
// Getters - acess the value of a private variable or field using the getter 
console.log(computer1.getInputDevice());
function testComputer(computer) {
    computer.input();
    computer.retrieve("name");
    // computer.output(computer.category);
    computer.output("just");
    computer.process();
    computer.connectToBluetoothDevice();
}
testComputer(computer1);
