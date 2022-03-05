# QUESTION NO.8

def check():
    a='The quick Brow Fox'
    i=0
    c=0
    c1=0
    while i<len(a):
        if a[i]>="a" and  a[i]<="z":
            c+=1
        if a[i]>="A" and a[i]<="Z":
            c1+=1
        i+=1
    print("no. of lower character:",c)
    print("no. of upper characters:",c1)
check()

# QUESTIONB NO.9

def square_numbers_1to5():
    i=1
    b=[]
    while i<=5:
        m=i**2
        b.append(m)
        i+=1
    print(b)
def square_numbers_25to30():
    i=25
    c=[]
    while i<=30:
        m=i**2
        c.append(m)
        i+=1
    print(c)
square_numbers_1to5()
square_numbers_25to30()
            #   OR
def square_numbers():
    i=1
    b=[]
    while i<=5:
        m=i**2
        b.append(m)
        i+=1
    print(b)
    i=25
    c=[]
    while i<=30:
        m=i**2
        c.append(m)
        i+=1
    print(c)
square_numbers()

# QUESTION NO.10 ????????????????????????????????
def add_string(a,b):
    c=int(a)
    d=int(b)
    e=c+d
    print(e)
add_string("2","5")


# QUESTION NON.11
def generate_range(min,max,step):
    i=min
    b=[]
    while i<=max:
        if step>0:
            b.append(i)
            i+=step
    print(b)
generate_range(2,10,2)

# QUESTIONS NO.12
# def no_zeroes_at_the_end(a,b,c,d):
#     i=0
    
    
# QUESTION NO.13
def even_odd(a):
    if a%2==0:
        print("even:",a)
    else:
        print("odd:",a)
a=int(input("Enter to check even or not:"))
even_odd(a)

# QUESTION NO.14
def prime_or_not(a):
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c+=1
        i+=1
    if c==2:
        print("prime:",a)
    else:
        print("not a prime:",a)
a=int(input("enter a number to check prime or not:"))
prime_or_not(a)

# QUESTION NO.15
def power_of_number(a):
    if a>0:
        print(a**2)
    else:
        print('write aprropriate value')
a=int(input("enter to check its power:"))
power_of_number(a)


# QUESTION NO.16
def multiplication_of_12():
    i=1
    a=int(input("entet a number for table:"))
    while i<=12:
        print(a,'*',i,'=',a*i)
        i+=1
multiplication_of_12()

# QUESTION NO. 17
def vote_or_not(a):
    if a >=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")
a=int(input("enter your age:"))
vote_or_not(a)