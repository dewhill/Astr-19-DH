"""Session 3 Prompt
write funtion: f(x) that returns x**3+8
in main: call f(9) and print result
use if statement to: if result is larger than 27, print 'YAY!' """

def f(x):
    # Create result variable for prompt operations
    result=(x**3)+8
    # Set yay equal to empty string and conditionally overwrite yay to " YAY!" as requested by prompt
    yay=""
    if result>=27:
        yay=" YAY!"
    # return result with conditional " YAY!" statement
    return f"{str(result)+yay}"

# Define main and run it
def main():
    print(f(9))

if __name__=="__main__":
    main()

# I first tried setting yay=None but that brought up some erorrs
# I learned you must use the variable created within the function: in this case x