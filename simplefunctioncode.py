# def function(num):
#     return num+25
# print(function(5))

# def function(name,age=20):
#     print(name,age)
# function("emma",25)

# def primeorNot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 break
#             else:
#                 print(num,"is a prime number")
#                 break
#     else:
#         print(num,"is not a prime number")
# num=int(input("enter to check if its prime number or not:"))
# primeorNot(num)

# def loop():
#     for num in range(1,5):
#         print(num,end=" ")
# loop()


# def hello():
#     x="Hello"
#     print(x)
# hello()

# def function(number):
#     # missing function body
# print(function(5))

# num=1
# def function(num):
#     global d
#     num+=3
#     print(num)
# function(6)
# print(num)

def text(x=1,y=2):
    x+=y
    y+=1
    print(x+y)
text()
 
 
def check():
    x=1
    while x<10:
        x+=1
    print(x)
check()