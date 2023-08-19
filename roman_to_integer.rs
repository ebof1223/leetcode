use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
    
        let mut numerals = HashMap::new();
        numerals.insert(String::from("I"), 1);
        numerals.insert(String::from("V"), 5);
        numerals.insert(String::from("X"), 10);
        numerals.insert(String::from("L"), 50);
        numerals.insert(String::from("C"), 100);
        numerals.insert(String::from("D"), 500);
        numerals.insert(String::from("M"), 1000);


        numerals.insert(String::from("IV"), 4);
        numerals.insert(String::from("IX"), 9);
        numerals.insert(String::from("XL"), 40);
        numerals.insert(String::from("XC"), 90);
        numerals.insert(String::from("400"), 400);
        numerals.insert(String::from("CM"), 900);
    

        let mut left = 0;
        let mut right = 1;
        let mut count = 0;
    
        while left < s.len() {
            let mut pair = String::new();
            pair.push(s.chars().nth(left).unwrap());
            pair.push(s.chars().nth(right).unwrap());

            if numerals.contains_key(&pair) {
            count += numerals[&pair];
            left += 1;
            right += 1;

            } else {
							let c = s.chars().nth(left).unwrap();
                count += numerals.get(&c).unwrap();
            }

            left += 1;
            right += 1;
            }
		return count;
    }

}
