const isPalindrome = (s) => {

  const letters = s.split("").filter(char =>
    (char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90) || (char.charCodeAt(0) >= 97 && char.charCodeAt(0) <= 122) || char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57).join("");

  if (letters.length == 1) return true;

  let l = 0;
  let r = letters.length - 1;


  while (l <= r) {

    if (letters[l].toLowerCase() != letters[r].toLowerCase()) return false

    l++;
    r--;

  }
  return true;
}

