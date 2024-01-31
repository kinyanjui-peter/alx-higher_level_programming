#!/usr/bin/node
/* script that prints the addition of 2 integers
 * first argument is the first integer
 * second argument is the second integer */

const process = require('process');
const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  const numA = parseInt(a);
  const numB = parseInt(b);

  if (isNaN(numA) || isNaN(numB)) {
    console.log('NaN');
  } else {
    console.log(numA + numB);
  }
}
add(a, b);
