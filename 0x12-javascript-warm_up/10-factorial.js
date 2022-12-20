#!/usr/bin/node
// Factorial

function factorial(num) {
	let total = num;
	if (num !== 1) {
		total *= factorial(num - 1);
		num--;
	}
	return total;
}

if (isNaN(process.argv[2])) console.log('1');
else console.log(factorial(parseInt(process.argv[2])));
