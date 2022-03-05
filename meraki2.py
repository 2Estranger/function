# MULTI FUNCTION ARGUMENTS
# def add_numbers(number1, number2):
#     print("Main do numbers ko add karunga.")
#     print(number1 + number2)
# add_numbers(120, 50)
# num_x = 130
# name =5
# add_numbers(num_x, name)

# MFG
def say_hello_people(name_x, name_y, name_z, name_a):
    print("Namaste ", name_x) # hindi mein
    print("Alah hafiz ", name_y) # urdu mein
    print("Bonjour ", name_z) # french mein
    print("Hello ", name_a) # english mein
say_hello_people("praticha","purnii", "sayjal", "antra")
say_hello_people("rabika", "rdc", "paru", "nikita")

# EXERCISE
def icecream(*flavours):
 for flavour in flavours:
  print("i love"+flavour)

icecream("chocolate", "butterscotch","vanilla","strawberry")

# WITHOOUT ARGUMENTS 
def add():
    a=int(input("enter the 1st number"))
    b=int(input("enter a 2nd number"))
    c=a+b
    print(c)
add()
add()

# WITH ARGUMENTS 
def addition(a,b):
    c=a+b
    print("addition=",c)
x=int(input("enter the 1st number"))
y=int(input("enter the 2nd number"))
addition(x,y)

