#!/usr/bin/node

const { argv } = require('node:process');
let message = 'Arguments found';
if (argv.length === 2) message = 'No argument';
else if (argv.length === 3) message = 'Argument found';
console.log(message);
