#!/usr/bin/node
/* The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You must use a loop (while, for, etc.) */

const process = require('process');
const size = process.argv[2];
const convInt = Number(size);

if (isNaN(convInt)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= convInt; i++) {
    let row = '';
    for (let y = 1; y <= convInt; y++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
