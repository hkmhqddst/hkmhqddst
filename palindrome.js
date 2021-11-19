function checkPalindrome(str) {
    //Mencari panjang string
    const len = string.length;

    //loop dengan setengah string
    for (let i = 0; i < len / 2; i++){
        if (string[i] !== string[len - 1 - i]) {
            return 'Not palindrome';
        }
    }
    return 'Is polindrome';
}

const string = prompt('Enter a string:');

const value = checkPalindrome(string);

console.log(value);