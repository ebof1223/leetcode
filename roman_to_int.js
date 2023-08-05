const romanToInt = (s) => {

	//IV, IX
	//XL, XC
	//CD, CM
	
	var integer = 0;
	for (let i = 0; i < s.length; i++ ) {
		console.log(integer);
		let numeral = s[i];
		if (numeral == 'I') {
			if  (numeral[i + 1] =='V') {
			integer += 4;
			i++;
			} else if (numeral[i + 1] == 'X') {
				integer += 9;
			i++;
				
			} else {
				integer+= 1;
			}
		} else if (numeral == 'X') {

			if (numeral[i + 1] == 'L') {
				integer +=40;
			i++;
			} else if (numeral[i + 1] == 'C'){
				integer += 90;
			i++;
			} else {
				integer += 10;
			}
		}else if (numeral == 'C') {
			if (numeral[i + 1] == 'D') {
				integer+= 400;
				i++;
			} else if (numeral[i + 1] == 'M') {
				integer += 900;
				i++;
			}else {
				integer += 100;
			}
		} else if (numeral == 'V') {
			integer += 5
		}else if (numeral == 'L') {
			integer += 50
		} else if (numeral == 'D') {
			integer += 500;
		} else if (numeral == 'M') {
			integer += 1000;
		}
		
	}
	return integer;
}

console.log(romanToInt('MCMXCIV'));
