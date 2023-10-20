"""Session 1 Prompt
print name and favorite movie/food"""

def s1prompt():
    # Create variables for my name and about me
    s1_x=str(f"Dennis Hill. ")
    s1_y=str(f"My favorite movie is Holes 2003 and my favorite food is pub grub. ")
    return f"{s1_x+s1_y}"

# Define main and run it
def main():
    print(s1prompt())

if __name__=="__main__":
    main()

# I learned that I can add strings together
# I learned to return variables and to print(function()) to output