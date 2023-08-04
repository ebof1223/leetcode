impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let mut x_reversed = String::new();
        let x_string: String = x.to_string();

        for char in x_string.chars().rev() {
          x_reversed.push(char)
        }

        for (i,char) in x_string.char_indices() {
           if char != x_reversed.chars().nth(i).unwrap_or_default() {return false}
        }
        return true
    }

}
