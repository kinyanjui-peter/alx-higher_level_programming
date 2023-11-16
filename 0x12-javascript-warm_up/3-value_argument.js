#!/usr/bin/node

const {argv} = require('process');
if (argv.length === 2)
{
	console.log('No argument');
}
const first_elem = argv[2];
console.log(first_elem);
