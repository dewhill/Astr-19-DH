"""Session 5 Prompt
Write a program that writes out a table of function sin(x) vs x
x is tabulated between 0 and 2pi with a thousand entries"""

import math


def main():
    # Create top line of table and show x and y value representation
    print("_____________________________________")
    print(f"|x\t \t ||    \t \t   y|")

    # Set x=0.0 and start iteration for 1000 times
    x=0.0
    for i in range(0,1000):
        # Actual math operation of y=sin(x)
        y=math.sin(x)
        # Format each value to only hold 10 decimal places and print values
        y="{:.10f}".format(y)
        z="{:.10f}".format(x)
        print(f"|{z}\t || \t{y}|")
        # Add pi/1000 for next iteration
        x+=float((math.pi)/(1000))
    # Finally, add the bottom of the table
    print("|________________||_________________|")

if __name__=="__main__":
    main()

# I am impressed with what I can do with python
# This looks very clean but I assure you I had to try many different
# things and ended up deleting it becuase this is most clean.
# I learned I had to set an original value for x, I learned that the
# math module isn't just used for sin but for many other functions.
# I learned hot to += to reuse variables while changing them within
# loops. This Prompt was very fun.