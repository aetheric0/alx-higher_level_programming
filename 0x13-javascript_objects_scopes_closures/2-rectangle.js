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
}

module.exports = Rectangle;
