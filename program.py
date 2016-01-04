def fizz_buzz_answer(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


def for_function(n):
    return ",".join(fizz_buzz_answer(i) for i in xrange(1, n + 1))

if __name__ == '__main__':
    print for_function(100)