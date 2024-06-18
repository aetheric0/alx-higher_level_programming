#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Intentionally empty
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }

  rotate () {
    const holder = this.width;
    this.width = this.height;
    this.height = holder;
  }
}

module.exports = Rectangle;
