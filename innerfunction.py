def f1():
   s = "I Love Navgurukul"
   def f2():
       print(s)
   f2()
f1()

# INNERFUNCTION

def first_function():
    s = 'I love Sikkim'
    def second_function():
        print(s)
    second_function()
first_function()

#EXAMPLE

def first_function():
    s = 'I love Sikkim'
    def second_function():
        x = "MY NAME IS JACK"
        print(x)
    second_function()
    print(s)
first_function()