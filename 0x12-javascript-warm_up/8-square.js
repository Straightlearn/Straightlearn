#!/usr/bin/node
// Square printing with 'X'

if (isNaN(process.argv[2])) console.log('Missing size');
else {
	for (let i = 0; i < parseInt(process.argv[2]); i++) {
		let no = '';
		for (let j = 0; j < parseInt(process.argv[2]); j++) {
			no += 'X';
		}
		console.log(no);
	}
}
