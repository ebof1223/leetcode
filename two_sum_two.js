var twoSum = function(numbers, target) {
	let l = 0
	let r = numbers.length - 1;

	while (l < r) {
		const sum = numbers[l] + numbers[r];

		if (sum == target) {
			break;
		}
		else if (sum < target) {
			l++;
		} else if (sum > target) {
			r--;
		}

		console.log('left', l);
		console.log('right', r);
	}
	return [l + 1, r + 1]
};

console.log(twoSum([2, 7, 11, 15], 9))
