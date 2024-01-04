#!/usr/bin/node
/**
 *  A script that reads and prints the content of a file 
 *  The first argument is the file path
 *  The content of the file must be read in utf-8
 *  If an error occurred during the reading,
 *  print the error object
 */
 
const fs = require('fs');

// file to read
read_file =  'cisfun';

// Read cisfun file
fs.readFile(read_file, 'utf-8', (err, data) => {
    if (err)
    {
        console.error(`Cannot read file: ${error.message}`);
    }   
    else 
    {
        console.log(`The file ${read_file} contain:\n${data}`);
    }
});
