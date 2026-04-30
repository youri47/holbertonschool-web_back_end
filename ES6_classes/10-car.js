export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() { return this._brand; }
  set brand(value) {
    if (typeof value !== 'string') throw new TypeError('Brand must be a string');
    this._brand = value;
  }

  get motor() { return this._motor; }
  set motor(value) {
    if (typeof value !== 'string') throw new TypeError('Motor must be a string');
    this._motor = value;
  }

  get color() { return this._color; }
  set color(value) {
    if (typeof value !== 'string') throw new TypeError('Color must be a string');
    this._color = value;
  }

  cloneCar() {
    const CarSpecies = this.constructor[Symbol.species] || this.constructor;
    return new CarSpecies();
  }
}
