#!/usr/bin/node
/**
 * script that gets the contents of a webpage and stores it in a file.
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 * The file must be UTF-8 encoded
 * You must use the module request
 */
const request = require('request');
const fs = require('fs');
// check if there are 2 arguments
if (process.argv.length !== 4) {
  console.error('Arguments Not Found');
  process.exit(1);
}

const url = process.argv[2];
const fileToStore = process.argv[3];

request.get(url, 'utf-8', (error, response, body) => {
  if (error) {
    console.error(`File ${url} cannot be opened`);
  } else {
    fs.writeFile(fileToStore, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(`Cannot write File to ${fileToStore}: ${error.message}`);
      } else {
        console.log(`File succesfully written to ${fileToStore}`);
      }
    });
});
