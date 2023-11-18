#!/usr/bin/node

const { argv } = require('process');
if (argv[2] == null) {
  console.log('No argument');
}
const firstElem = argv[2];
console.log(firstElem);
