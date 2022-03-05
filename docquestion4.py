# QUESTION NO.32   NOT DONE

# QUESTION NO.33
# def a(bmi):
#     while bmi>0:
#         if bmi > 30:
#             return "Obese"
#         elif bmi <= 18.5:
#             return "Underweight"
#         elif bmi <= 25.0:
#             return "Normal"
#         elif bmi <= 30.0 :
#             return "Overweight"
# bmi=int(input("Enter your height:"))
# print(a(bmi))

# QUESTION NO.34  NOT DONE

# QUESTION NO.35 
# Kids drink toddy.
#     Teens drink coke.
#     Young adults drink beer.
#     Adults drink whisky.
#     Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.



# LOGICAL QUESTIONS
# def even_odd(limit):
#     i=1
#     while i<=limit:
#         if i%2==0:
#             print("even no:",i)
#         else:
#             print("odd no.:",i)
#         i+=1
# limit=int(input('enter a  limit :'))
# even_odd(limit)

# 40 

def square():
    a=[9,1,1,9]
    i=0
    while i < len(a):
        if a[i]:
            m=a[i]**2
        i+=1
        print(m,end='')
square()