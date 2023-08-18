var mergeAlternately = function(word1, word2) {

    var alternative_string = new String();

    for (let i = 0; i < word1.length; i++){
        alternative_string +=  word1[i]
	    if (i === word1.length - 1 ){
		    alternative_string += word2.slice(i);
	    } else if (!word2[i]) {
		alternative_string += word1.slice(i + 1);
		    break
	    } else {
		    alternative_string += word2[i];
	    }
		
    }
	return alternative_string
};
