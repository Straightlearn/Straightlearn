#!/usr/bin/node
//Prints a message depending on the number of arguments

let message = 'Arguments found';
if (process.argv.length === 2) message = 'No argument';
else if (process.argv.length === 3) message = 'Argument found';
console.log(message);
