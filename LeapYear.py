def leap(n):
    if n < 4:
        return "Not a Leap Year!"
    if n % 100 == 0:
        return "Not a Leap Year!"
    elif n % 4 == 0:
        return "Leap Year!"
    else:
        return "Not a Leap Year!"
