"""
Below you wil find some challenges to complete. The file is organized
such that each challenge is it's own function that runs when the file
is run. As you go through each challenge you can feel free to comment
out the function call at the bottom of the file and move on to the next
one.
"""


def challenge_one():
    """
    =========== Challenge 1 =============

    TQDM is a third-party module that allows you to create progress
    bars for loops.

    Figure out how to install the python module TQDM with pip and 
    look at the documentation to help figure out how to create a for
    loop with a progress bar that goes through 10 iterations at 1 
    iteration a second.

    I have setup a skeleton version of the code below that will get you
    90% of the way there, all you need to do is figure out the TQDM part.

    Hint: You only need to make an adjustment to line 30

    """
    from tqdm import trange
    import time
    for number in trange(10):
        print(number)
        time.sleep(1) #Waits one second before continuing.
challenge_one()

from my_module import print_backwards
def challenge_two():
    """
    =========== Challenge 2 =============

    Create a python module (another file in this folder) called
    my_module.py
    
    Inside of my_module.py define a function called print_backwards().
    This function should take a string and return the string in reverse.
    For example: print_backwards('hello') # returns 'olleh'

    You will know that you did it right if when you run this challenge_two()
    function it prints 'olleh'.
    """
    # from my_module import print_backwards # Uncommnet when you have made the file
    print(print_backwards("hello")) # Uncommnet when you have made the file

challenge_two()

"""
    =========== Challenge 3 =============

    Go to https://github.com/lcwyo/gifcat, download the repository and
    run the application.
"""


if __name__ == "__main__":
    challenge_one()
    challenge_two() # uncomment after completing challenge_one()