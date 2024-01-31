#!/usr/bin/node

const { argv } = require('process');

const first = argv[2];
const second = argv[3];

if ((argv[2] == null) && (argv[3] == null)) {
  console.log('undefined is undefined');
} else if ((argv[2] == null) && (argv[3] != null)) {
  console.log(`undefined is ${second}`);
} else if ((argv[2] != null) && (argv[3] == null)) {
  console.log(`${first} is undefined`);
} else if ((argv[2] != null) && (argv[3] != null)) {
  console.log(`${first} is ${second}`);
}
