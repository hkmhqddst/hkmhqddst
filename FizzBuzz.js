var check = function (number) {
    var fizz = number % 3 == 0, buzz = number % 5 == 0;
    console.log(fizz ? buzz ? "FizzBuzz" : "Fizz" : buzz ? "Buzz" : number);
    if (number != 0) { return check(number - 1);}
} 
check(15);