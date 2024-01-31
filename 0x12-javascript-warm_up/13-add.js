#!/usr/bin/node
/**
 * function that returns the addition of 2 integers.
 * function must be visible from outside
 * name of the function must be add
 * You are not allowed to use var
*/
exports.add = function (a, b) {
  a = parseInt(a);
  b = parseInt(b);

  return (a + b);
}
