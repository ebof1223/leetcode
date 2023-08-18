impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut str_alt_merged = String::new();
       
        for (i, char) in word1.char_indices(){
            str_alt_merged.push(char);

            if (i + 1 == word1.chars().count()) {
                let word2_remaining = word2[i..word2.chars().count()];
                str_alt_merged.push_str(&word2_remaining);
            } else if i > word2.chars().count() - 1 {
                let word1_remaining = word1[i + 1..word1.chars().count()];
                str_alt_merged.push_str(&word1_remaining);
                break;
            } else {
            str_alt_merged.push(word2.chars().nth(i).unwrap())
            }
        }
        return str_alt_merged;
    }
}
