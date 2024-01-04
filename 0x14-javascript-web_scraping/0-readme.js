#!/usr/bin/node
/**
 *  A script that reads and prints the content of a file
 *  The first argument is the file path
 *  The content of the file must be read in utf-8
 *  If an error occurred during the reading,
 *  print the error object
 */
const fs = require('fs');

// Check if the file path is provided as an argument
if (process.argv.length !== 3) {
    console.error('Usage: node 0-readme.js <file-path>');
    process.exit(1);
}
// file to read
const readFile = 'process.argv[2]';

// Read cisfun file
fs.readFile(readFile, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
