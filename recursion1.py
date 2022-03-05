# #FIRST 6 NATURAL NUMBER PRINT/

# def natural(n):
#     if n>1:
#         natural(n-1)
#     print(n)
# n=int(input("Enter The ") 
# natural(n)        

# #FIRST 10 WHOLE NUMBER'S: 
# def whole_number(n):
#     if n>0:
#         whole_number(n-1)
#     print(n)
# n=int(input("Enter The Limit:"))
# whole_number(n)

#PERFECT NUMBER

def perfect():
    i=1
    while i<=100:
        a=i
        sum=0
        j=1
        while j<a:
            if a%j==0:
                sum+=j
            j+=1
        if sum==a: 
            print(j,":perfect number")
        i+=1
perfect()

# ASCENDING ORDER
def ascending():
    a=[7,9,3,2,4,0,5,8,1]
    i=0
    while i<len(a):
        j=0
        while j<len(a):
            if a[i]<a[j]:
                s=a[i]
                a[i]=a[j]
                a[j]=s
            j+=1
        i+=1
    print(a)
ascending()            