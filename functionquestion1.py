# QUESTION1 

def eligible_for_vote(a):
    if a>=18:
        print("you are eligible")
    else:
        print("not eligible")
a=int(input("enter you current age"))
eligible_for_vote(a)

#QUESTION2
# n=int(input('enter'))
# s=0
# i=1
# while i<n:
# 	if n%i==0:
# 		s+=i
# 	i+=1
# if s==n:
# 	print(n,'perfect number')
# else:
# 	print(n, 'not perfect ')

# PERFECT NUMBER
# def perfect(a):
#     s=0
#     i=1
#     while i<a: 
#         if a%i==0:
#             s+=i
#         i+=1
#     if s==a:
#         print(a,"perfect number")
#     else:
#         print(a,"not perfect")
# a=int(input("enter"))
# perfect(a)

# # CHECK FROM 1 TO 1000 PERFECT NUMBER
def perfect():
    i=1
    while i<=1000:
        b=i
        j=1
        sum=0
        while j<i:
            if b%j==0:
                sum+=j
            j+=1 
        if sum==b:
            print(j,"perfect")
        i+=1   
perfect() 