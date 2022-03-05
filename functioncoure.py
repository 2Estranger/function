# FUNCTION QUESTIONS 5 QUS6

def calculator(a,b,operation):
    if operation=="add":
        c=a+b
        return c
    elif operation=="substract":
        c=a-b
        return c
    elif operation=="multiply":
        c=a*b
        return c
    elif operation=="divide":
        c=a%b
        return c
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
add_result=calculator(a,b,"add")
print(add_result,"addition")
substract_result=calculator(a,b,"substract")
print(substract_result,"substraction")
multiply_result=calculator(a,b,"multiply")
print(multiply_result,"multiplication")
divide_result=calculator(a,a,"divide")
print(divide_result,"division")

# QUESTION PART 3

def list_change():
    a=[5, 10, 50, 20]
    b=[2, 20, 3, 5]
    i=0
    x=[]
    while i<len(a):
        while i<len(b):
            m=a[i]*b[i]
            x.append(m)
            i+=1
    print(x)
list_change()