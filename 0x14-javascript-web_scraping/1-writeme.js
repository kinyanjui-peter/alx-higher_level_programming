#!/usr/bin/node

/**
 * a script that writes a string to a file.
 * The first argument is the file path
 * The second argument is the string to write
 * The content of the file must be written in utf-8
 * If an error occurred during while writing, print the error object
 */

const fs = require('fs');

// check if process has a argument
if (process.argv.length !== 4) {
  console.error('No argument found');
  process.exit(1);
}
// get file path and string to write
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('file successfully written');
  }
});
