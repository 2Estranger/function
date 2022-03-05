# SIMPLE RETURN VALUES
def sum(value1,value2):
    c=value1+value2
    return c
x=int(input("enter"))
y=int(input("enter"))
print(sum(x,y))

# FUNCTIONS RETURN VALUES
def add(a,b):
    c = a+b
    return c 
sum1 = add(20, 40)
print(sum1)
sum2 = add(560, 23)
x = 1234
y = 12
sum3 = add(x , y)
print(sum2)
print(sum3)
number_a = add(20, 40) / add(5, 1)
print(number_a)

# FRV
def add(a,b):
    c=a + b
    print (c)
d = add(4, 5)
print(d)
print(type(d))

# FRV

def add(a,b):
    c = a + b
    print("Hello from NavGurukul ;)")
    return c 
sum6 = add(100,88)

# FRV
def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"
    print("Kya main print ho payungi? :-(")
mon_menu = menu("monday")
print(mon_menu)
tue_menu = menu("tuesday")
print(tue_menu)
sun_menu = menu("sunday")
print(sun_menu)

# FRV
def menu(day):
    if day == "monday":
        food = "Butter Chicken"
    elif day == "tuesday":
        food = "Mutton Chaap"
    else:
        food = "Chole Bhature"
    print("Kya main print ho payungi? :-(")
    return food
    print("Lekin main toh pakka nahi print hounga :'(")
print(menu("monday"))