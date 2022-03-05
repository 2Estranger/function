# QUESTION NO.19
def func(x=1,y=2):                                                                                                                                                                                                                                                                                                                                                                   
    x = x + y
    y += 1
    print(x,y)
func(y = 2, x = 1)

# QUESTION NO.22
num = 1
def func():
    global num
    num = num + 3
    print(num)

func()
print(num)

#QUESTION NO.25

def count_positive_negetive(a):
    i=0
    cp=0
    cn=0
    while i<len(a):
        if a[i]>=0:
            cp+=1
        else:
            cn+=1
        i+=1
    print("positive no:",cp)
    print("negetive no:",cn)
a=[2, -7, 5, -64, -14]
count_positive_negetive(a)


# QUESTION NO.26
def fizz_buzz(a):
    if a%3==0 and a%5==0:
        print("FizzBuzz")
    elif a%3==0:
        print("Fizz")
    elif a%5==0:
        print("Buzz")
    else:
        print(a)
a=int(input("Enter the number:"))
fizz_buzz(a)

# QUESTION NO.27
def speed_of_driver(speed):
    c=0
    point=(speed-70)//5
    if speed <=70:
        print("ok")
    elif speed>70 and speed<=130:
        print("point:",point)
        c+=point 
    elif speed>12:
        print("license cancelled")
speed=int(input("enter:"))
speed_of_driver(speed)

# QUESTION NO.28
def show_functions(a):
    i=0
    while i<=a:
        if i%2==0:
            print("even:",i)
        if i%2!=0:
            print("odd:",i)
        i+=1
a=int(input("enter a number:"))
show_functions(a)

# QUESTION NO.29
def multiple_of_3and5(limit):
    i=1
    a=[]
    while i<=limit:
        if i%3==0 or i%5==0:
            a.append(i)
        i+=1
    print(a)
    j=0
    sum=0
    while j<len(a):
        if a[j]:
           sum+=a[j]
        j+=1 
    print(sum)
limit=int(input("enter a limit:"))
multiple_of_3and5(limit)

# QUESTION NO.30
def prime(limit):
    i=0
    while i<=limit:
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c+=1
            j+=1
        if c==2:
            print(i)
        i+=1
limit=int(input("enter the limit of prime:"))
prime(limit)

# QUESTION NO.31
def multiplication(a):
    i=1
    while i<=10:
        print(i,"*",a,'=',a*i)
        i+=1
a=int(input("enter number"))
multiplication(a)

