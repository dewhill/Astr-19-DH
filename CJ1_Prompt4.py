"""Session 4 Prompt
Create a class that describes your favorite animal
length of arms: float
length of legs: float
number of eyes: integer
does it have a tail: boolean
is it furry: boolean
initialize
create function to print characteristics"""

# Create Animal class and initialize all attributes we'd like to include
class Animal:
    def __init__(self,a_length,l_length,n_eyes,d_tail,i_furry):
        self.a_length=a_length
        self.l_length=l_length
        self.n_eyes=n_eyes
        self.d_tail=d_tail
        self.i_furry=i_furry

# Create a function to print all attributes we'd like to include
    def call_chars(self):
        return f"arm length: {self.a_length}, leg length: {self.l_length}, number of eyes: {self.n_eyes}, it has a tail: {self.d_tail}, it is furry: {self.i_furry}"


# Create main and run it. Create Polar Bear attributes and call it
def main():
    Polar_Bear=Animal(43.0,43.0,2,True,True)
    print(Polar_Bear.call_chars())

if __name__=="__main__":
    main()