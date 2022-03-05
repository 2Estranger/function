#   QUESTION NO.1
def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr
print(match_words(['abc', 'xyz',"dbc", 'aba', '121']))

#   QUESTION NO.2
# Write a Python function to find the Max of three numbers.
def max(a,b,c):
    if a>b and a>c:
        print('max number')
        return a
    elif b>a and b>c:
        print('max number')
        return b
    elif c>a and c>b:
        print('max number')
        return c
a=int(input("Enter the First number"))
b=int(input("Enter the Second number"))
c=int(input("Enter the Third number"))
print(max(a,b,c))

# # ALL MAX REDO IT
# def max_smax_tmax(a,b,c):
#     if a>b and b>c:
#         print(a,"is max")
#         print(b,"is second max")
#         print(c, "is third max")
#     elif b>a and a>c:
#         print(b,"is max")
#         print(a,"is second max")
#         print(c,"is third max")
#     elif c>a and a>b:
#         print(c,'is max')
#         print(a,"is second max")
#         print(b,"is third max")
#     elif a<b and c>b:
#         print(c,"is max")
#         print(b,"is second max")
#         print(a,"is third max")
#     elif b<a and c>a:
#         print(c,'is max')
#         print(a,"is second max")
#         print(b,"is third max")
#     elif c<b and c<a:
#         print(b,'is max')
#         print(a,'is second max')
#         print(c,'is third max')
# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# c=int(input("Enter the third number"))
# max_smax_tmax(a,b,c)

# QUESTION NO.3

def listsum(a):
    sum=0
    for i in a:
        sum += i
    return sum
print(listsum([8, 2, 3, 0, 7]))

# QUESTION NO.4

def reverse(rev):
    if len(rev) == 0:
        return rev
    else:
        return reverse(rev[1:]) + rev[0]
print(reverse("ily"))
                #   OR


# QUESTION NO.5

def unique(a):
    i=0
    x=[]
    while i<len(a):
        if a[i] not in x:
            x.append(a[i])
        i+=1
    print(x)
a=[1,2,3,3,3,3,4,4,5]
unique(a)

# QUESTION NO.6
#PRINT EVEN NUMBER FROM LIST

def even_no(a):
    i=0
    x=[]
    while i<len(a):
        if a[i]%2==0:
            x.append(a[i])
        i+=1
    print(x)
b=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even_no(b)

# QUESTION NO.7
# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def a(bmi):
    if bmi<=18.5:
        return "underweight"
    if bmi<=25.0:
        return "Normal"
    if bmi<=30.0:
        return "Overwight"
    if bmi>30:
        return "Obese"
bmi=int(input("Enter:"))
print(a(bmi))










