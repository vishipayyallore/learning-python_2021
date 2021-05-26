def calculate(stopValue):

    total = 0
    a = 0
    b = 1

    while a < stopValue:
        if a % 2 == 0:
            total += a
        a, b = b, a + b

    return total


print(calculate(1000000))
