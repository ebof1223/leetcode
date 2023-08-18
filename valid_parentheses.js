const isValid = s => {
	const symbols = {

		'[': ']',
		'(': ')',
		'{': '}',

	}
	
	const stack = [];

	for (const char of s) {

		if (char in symbols) {
			stack.push(symbols[char])

		} else if (char == stack[stack.length - 1]) {
			stack.pop();
		} else {
			return false;
		}
	}

	return stack.length == 0;


}

