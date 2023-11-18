#!/usr/bin/node
/* Write a class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments: w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * Create an instance method called print() that prints the rectangle using
 *               the character X */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
    // will print an empty undefined on the console.
    } else {
      this.width = w;
      this.height = h;
     
      
    }
  }

  print () { 
    for (let c = 1; c <= this.height; c++) {
      let row ='';
      for (let m = 0; m < this.width; m++) {
	row += 'X';
      }
      console.log(row);
    }
  }
  rotate () {
    [this.width, this.height] = [this.height, this.width];
 
    }

  double () {
    this.widtht *= 2;
    this.height *= 2;
  }
};
module.exports = Rectangle;
