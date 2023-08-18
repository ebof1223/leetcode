impl Solution {
    pub fn remove_vowels(s: String) -> String {
        //create a string
        let mut no_vowels = String::new();
        for c in s.chars() {
            match c {
                 'a'|'e'|'i'|'o'|'u'=> continue,
                _ => no_vowels.push(c),
            } 
        }
        return no_vowels;
    }
}

pub fn main (){
    remove_vowels("leetcodeisacommunityforcoders");
}
