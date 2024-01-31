#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments.
 * script that searches the second biggest integer in the list of arguments.
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */
const process = require('process');
const args = process.argv.slice(2);

function secondLargestNumber (n) {
  const length = n.length;

  if (length <= 1) {
    console.log(0);
  } else {
    const list = n.sort((a, b) => b - a);
    const secondLargest = list[1];
    console.log(secondLargest);
  }
}

secondLargestNumber(args);
