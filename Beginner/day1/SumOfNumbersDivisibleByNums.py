
def calculate(stopValue, value1, value2):
    numbers = []
    
    for i in range(stopValue):
        if (i % value1 == 0) or (i % value2 == 0):
            numbers.append(i)
    
    print('Numbers divisible by ', value1, ' OR ', value2, ' are ', numbers)
    total = sum(numbers)
    
    return total


stopValue = 20
value1 = 5
value2 = 7

print('Sum of all numbers: ', calculate(20, 5, 7))
print('Sum of all numbers: ', calculate(100, 5, 7))
