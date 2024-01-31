#!/usr/bin/node
/* script that computes and prints a factorial
 * first argument is integer
 */

const process = require('process');
const arg = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  } else if (n > 1) {
    return n * factorial(n - 1);
  } else {
    return 'Number less than 0';
  }
}
console.log(factorial(arg));
