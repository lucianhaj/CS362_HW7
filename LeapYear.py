def leap(n):
    if n < 4:
        return "Not a Leap Year!"
    elif n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return "Leap Year!"
            else:
                return "Not a Leap Year!"
        else:
            return "Leap Year!"
    else:
        return "Not a Leap Year!"
