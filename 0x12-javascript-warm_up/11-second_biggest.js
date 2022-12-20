#!/usr/bin/node
// second biggest

if (process.argv.length < 4) console.log('0')
else {
	let nums = [];
	for (let i = 2; i < process.argv.length; i++){
		nums.push(process.argv[i]);
	}
	nums = new Set(nums.sort((a, b) => b - a));
	nums = [...nums];
	console.log(nums[1]);
}
