#!/usr/bin/node
/**
 * a script that display the status code of a GET request.
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */
const request = require('request');
// check if arguments are more than 3
if (process.argv.length !== 3) {
  console.error('Arguments are not equal to 3');
  process.exit(1);
}
const reqUrl = process.argv[2];
request.get(reqUrl, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
