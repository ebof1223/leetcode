const isPalindrome = (x) => {
	var xReversed = new String();
	const xAsString = x.toString();

	for (let char = xAsString.length - 1; char >= 0; char--) {
		xReversed += xAsString[char];
	}
	
	for (let char = 0; char < xReversed.length; char++) {
		if (xAsString[char] !== xReversed[char]){
			return false;
		}

	}
	return true
}

console.log(isPalindrome(-121))

