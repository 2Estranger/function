# QUESTION1
# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)
# employee("kartik",30000)
# employee("deepak")

# QUESTION2
def primeorNot(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
                break
    else:
        print(num,"is not a prime number")
num=int(input("enter to check if its prime number or not:"))
primeorNot(num)

# QUESTION3

# def greet(*names):
#     for name in names:
#         print("Hello",name)
# greet("Bedna","Sayjal","Antra",'Deepika')

# QUESTION4
# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number//=10
#     return sum
# print(sumofdigits(123))

# QUESTION5
# def meal(day,time):
#     if day=="monday":
#         if time=="breakfast":
#             return "omelet with rice"
#         elif time=="lunch":
#             return "pizza with sauce"
#         elif time=="dinner":
#             return "meat with rice"
#         else:
#             return "time is not appropriate"
#     elif day=="tuesday":
#         if time=="breakfast":
#             return "bread with butter"
#         elif time=="lunch":
#             return "gundruk ko jhol"
#         elif time=="dinner":
#             return "steak and wine"
#         else:
#             return "time is inappropriate"
#     elif day=="wednesday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "chowmin with sauce"
#         elif time=="dinner":
#             return "momos with achar"
#         else:
#             return "inappropriate time "
# print(meal("monday","lunch"))
# print(meal("tuesday","dinner"))

# QUESTION6
def checkKey():
    car ={
        "brand":  "ford",
        "model":  "mustang",
        "year":  1964
        }
    if "brand" in car:
        print("Yes, 'model' is one of the keys in this dictionary.")
    else:
        print("No, 'model' key is not in this dictionary.")
checkKey()

#DEBUG CODE QUESTION1
def calculate_sum(a,b):
    sum = a+b
    print(sum)
calculate_sum(4,5)

# DEBUG CODE QUESTION2
def multiply(a,b):
    multiply=a*b
    return multiply
print(multiply(3,4))

# DEBUG CODE QUESTION3
def Avg(number1,number2,number3):
    sum=number1+number2+number3/3
    print(sum)
Avg(2,2,2)

# DEBUG CODE QUESTION4
def voter(age):
    if age >= 18:
        print("eligible")
    else:
        print("not eligible")
voter(20)

# DEBUG CODE QUESTION5
def distance(kms):
    if kms <= 20:
        print("close")
    elif kms > 20 and kms <50:
        print("medium")
    else:
        print("far")
distance(29)