def fizznbuzz(n):

    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fuzz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    if n % 3 == 0 and n % 5 == 0:
        return ("FizzBuzz")
    elif n % 3 == 0:
        return("Fizz")
    elif n % 5 == 0:
        return("Buzz")
    else:
        return n


fizznbuzz(3)
