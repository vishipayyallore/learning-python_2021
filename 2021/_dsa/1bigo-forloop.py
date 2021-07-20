### Find Sum of N Natural Numbers ###

import time
time.time()

timestamp1 = time.time()

end_value = 101
total = 0

for value in range(1, end_value):
    total = total + value

print("The sum is", total)

timestamp2 = time.time()
print('Time take to execute this program: ', (timestamp2 - timestamp1))
