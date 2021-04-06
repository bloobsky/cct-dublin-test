"""
    =========== Exercise 1 =============

    import the math module and use math.sqrt() on
    a user inputted variable.

    NOTE: you have the input converted to an int
    automatically using int(input()).
"""
import math

number = int(input("Give me a number and i give u square of that"))
print (math.sqrt(number))

"""
    =========== Exercise 2 =============

    import the sleep function from the time module as pause
    and run pause(5)
"""
from time import sleep
print("0")
print('pause')
sleep(2)
print('2 secs has passed')

"""
    =========== Exercise 3 (question) =============

    import the sleep function from the time module as pause.

    Write a function called pause() that takes an argument and
    prints it.

    Which pause() will be called, and why?
"""
from time import sleep as pause

def pause(arg):
    from time import sleep
    print(arg)

pause(7)