#!/usr/bin/node
// pints My number: <first argument converted in integer>

let number = process.argv[2];
if (isNaN(number)) {
	console.log('Not a number');
} else {
	console.log('My number: ' + parseInt(number));
}
