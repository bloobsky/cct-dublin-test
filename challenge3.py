"""
    =========== Challenge 3 =============
    THIS CHALLENGE IS HARD, DON'T GET DISCOURADGED
                IF YOU CAN'T DO IT!
    Using the list below print the numbers
    in ascending order. It should look like this: 
    1
    2
    3
    4
    5
    6
    7
    8
    9
    HINTS:
    1. The pattern is that the list is in order where the
        same index on each list is in ascending order.
        i.e. 
        numbers[0][0] is 1
        numbers[1][0] is 2
        numbers[2][0] is 3
        etc.
    2. The simplest (and shortest) way to do this
        is with a loop counter variable, and a while loop.
"""
import numpy
numbers = [
    [1, 4, 7],
    [2 ,5, 8],
    [3, 6, 9]
]

nums = numpy.array([
    [1, 4, 7],
    [2 ,5, 8],
    [3, 6, 9]])

for x in nums:
  for y in x:
    print(y)



number = 0

print(numbers[0][0])
print(numbers[1][0])
print(numbers[2][0])
print(numbers[0][1])
print(numbers[1][1])
print(numbers[2][1])
print(numbers[0][2])
print(numbers[1][2])
print(numbers[2][2])
