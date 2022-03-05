#QUESTION 4 PART 1
def add_numbers(num1,num2):
    c=num1+num2
    print(c)
num1=3
num2=6
add_numbers(num1,num2)

# QUESTION 4 PART 2
def add_number_list():
    a=[50,60,10]
    b=[10,20,13]
    i=0
    while i <len(a):
        while i<len(b):
            sum=a[i]+b[i]
            print(sum)
            i+=1
add_number_list()

# QUESTIONS 5 PART 1
def check_numbers(a,b):
    if a%2==0 and b%2==0:
        print("both are even numbers")
    else:
        print("not both are even numbers")
a=int(input("enter a number"))
b=int(input("enter a numbers"))
check_numbers(a,b)

#QUESTION 5 PART2

def check_numbers_list():
    a=[2, 6, 18, 10, 3, 75]
    b=[6, 19, 24, 12, 3, 87] 
    i=0
    while i<len(a):
        while i<len(b):
            if a[i]%2==0 and b[i]%2==0:
                print("both are even numbers")
            else:
                print("not both are even numbers")
            i+=1
check_numbers_list()

# FUNCTIONS RETURN VALUES
def add_numbers(number_x, number_y):
    number_sum = number_x + number_y
    return number_sum

sum1 = add_numbers(20, 40)
print(sum1)
sum2 = add_numbers(560, 23)
a = 1234
b = 12
sum3 = add_numbers(a, b)
print(sum2)
print(sum3)
number_a = add_numbers(20, 40) / add_numbers(5, 1)
print(number_a)