#!/usr/bin/node
/*a script that prints two arguments passed to it,
 * in the following format: “ is "*/

const{argv} = require('process');
if ((argv.length !== 4))
{
	if (argv[2] !== undefined  && argv[3] !== undefined) 
	{
		console.log(`${argv[2]} is ${argv[3]}`);
	}
	else if  (argv[2] === undefined && argv[3] !== undefined)
	{
		console.log(`undefined is ${argv[3]}`);
	}
	else if ((argv[2] !== undefined && argv[3] === undefined))
	{
		console.log(`${argv[2]} is undefined`);
	}
	else
	{
		console.log('undefined is undefined');
	}
}
