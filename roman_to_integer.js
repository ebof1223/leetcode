const romanToInt = (s) =>  {
	
	const numerals = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
		'IV': 4,
		'IX': 9,
		'XL': 40,
		'XC': 90,
		'CD': 400,
		'CM': 900,
	}
	let left = 0;
	let right = left + 1;
	var count = 0;

	while (left < s.length	) {

		const twoNums = numerals[s[left] + s[right]];
		if (twoNums) {
		count += twoNums; 
			left++;
			right++;
		} else {
		count += numerals[s[left]];
		}

		left++;
		right++;
	}
	return count;
};

console.log(romanToInt("MCMXCIV"));

