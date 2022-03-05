# QUESTION3
# def sum(a,b,c):
#     d=a+b+c
#     print("sum of three numbers",d)
#     def avg(e):
#         print("average",e/3)
#     avg(d)
# a=int(input("enter"))
# b=int(input("enter"))
# c=int(input("enter"))
# sum(a,b,c)

# QUESTION4 EVEN ODD WITHIN LIMIT
# def show_numbers(a):
#     i=0
#     while i<=a: 
#         if i%2==0:
#             print(i,"EVEN")
#         else:
#             print(i,"ODD")
#         i+=1
# a=int(input("enter"))
# show_numbers(a)

# QUESTION5 
# def multiples_of_3_and_5(a):
#     i=1
#     sum=0
#     l=[]
#     while i<=a: 
#         if i%3==0:
#             c=i
#             sum+=c
#             l.append(c)
#         elif i%5==0:
#             d=i
#             sum+=d
#             l.append(d)
#         i+=1
#     print(l)
#     print("Total sum:",sum)
# a=int(input("enter:"))
# multiples_of_3_and_5(a)

# # QUESTIONS 6
# def driver(speed):
#     c=0
#     point=(speed-70)//5
#     warning=0
#     if speed<=70:
#         print("okay")
#     elif speed>70 and speed<130:
#         print(point,":point")
#         c+=point
#     elif speed>12:
#         print("license cancelled")
# speed=int(input("enter"))
# driver(speed)

# # QUESTION7
# def name(a,b):
#     if len(a)<len(b):
#         print(b)
#     elif len(a)>len(b):
#         print(a)
#     elif len(a)==len(b):
#         print(a)
#         print(b)
# a=input("enter the name")
# b=input("enter the second name")
# print("welcome")
# print()
# name(a,b)

# SINGLE ASTRIGS
# def add(*a):
#     print(a)
# add(5,4,6,10)

# DOUBLE ASTRIGS
# def add(**a):
#     print(a)
# add(a=5,b=4,c=6,d=10)

# QUESTIONS8    INCOMPLETE 

def function(**a):
    i=1
    while i<=a:
        if i>0:
            i=a**2
        i+=1
    print(a)
a=int(input("Enter:"))
function(a)