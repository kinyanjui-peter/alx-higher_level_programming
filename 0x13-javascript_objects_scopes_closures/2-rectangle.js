#!/usr/bin/node
/* class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object */

class Rectangle {
  constructor (w, h){
    this.width = w;
    this.height = h;
    function Create_object(){
      if (this.width >= 0 || this.height >= 0) {
	const emptyObject = new Rectangle();
	  return emptyObject;
      }
      else {
	      return {};
      }
      }
  }

}
module.exports = Rectangle;
