"""Session 2 Prompt
print two floats added
print the difference between two integers
print the product of a float and an integer
with each - print the typw"""

def s2_part1():
    # Take user input for first number. If it cannot be converted to float, notify user of an error and set equal to 0
    s2_x=input("Enter a floating point number. --- ")
    try:
        s2_x=float(s2_x)
    except ValueError:
        print("Error, not a float. ")
        s2_x=0

    # Same as s2_x
    s2_y=input("Enter another. --- ")
    try:
        s2_y=float(s2_y)
    except ValueError:
        print("Error, not a float. ")
        s2_y=0
    
    # Return added value
    return f"{float(s2_x)+float(s2_y)} and type: {type(float(s2_x)+float(s2_y))}"

def s2_part2():
    # Take user input for first number. If it cannot be converted to integer, notify user of an error and set equal to 0
    s2_z=input("Enter an integer number. --- ")
    try:
        s2_z=int(s2_z)
    except ValueError:
        print("Error, not an integer. ")
        s2_z=0

    # Same as s2_z
    s2_w=input("Enter another. --- ")
    try:
        s2_w=int(s2_w)
    except ValueError:
        print("Error, not an integer. ")
        s2_w=0
    
    # Return subtracted value
    return f"{int(s2_z)-int(s2_w)} and type: {type(int(s2_z)-int(s2_w))}"

def s2_part3():
    # Take user input for first number. If it cannot be converted to a float, notify user of an error and set equal to 0
    s2_q=input("Enter a floating point number. --- ")
    try:
        s2_q=float(s2_q)
    except ValueError:
        print("Error, not a float. ")
        s2_q=0

    # Same as s2_q
    s2_r=input("Enter an integer. --- ")
    try:
        s2_r=int(s2_r)
    except ValueError:
        print("Error, not an integer. ")
        s2_r=0
    
    # Return multiplied value
    return f"{float(s2_q)*int(s2_r)} and type: {type(float(s2_q)*int(s2_r))}"

# Define main and run it
def main():
    print(f"{s2_part1()}")
    print(f"{s2_part2()}")
    print(f"{s2_part3()}")

if __name__=="__main__":
    main()

# I learned the try function to resolve conditional errors
# I learned that type(s2_part1) will output "function" instead of the type of the returned value